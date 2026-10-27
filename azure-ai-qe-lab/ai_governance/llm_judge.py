import os
import json
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

class AzureLLMJudge:
    """
    Implements LLM-as-a-Judge and Trust Architecture audit logging using Azure OpenAI Service.
    """
    def __init__(self):
        self.api_key = os.getenv("AZURE_OPENAI_API_KEY")
        self.endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o-mini")
        self.api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01")

        if self.api_key and self.endpoint:
            self.client = AzureOpenAI(
                api_key=self.api_key,
                api_version=self.api_version,
                azure_endpoint=self.endpoint
            )
        else:
            self.client = None

    def evaluate_test_output(self, test_name: str, system_output: str, risk_rubric: dict) -> dict:
        print(f"[Azure LLM-as-a-Judge] Evaluating '{test_name}' against risk rubric...")
        
        score = 100
        violations = []

        if "error" in system_output.lower() and not risk_rubric.get("allow_errors", False):
            score -= 50
            violations.append("Error detected in execution output.")

        if len(system_output) < risk_rubric.get("min_length", 5):
            score -= 30
            violations.append("Output fails minimum verbosity/detail threshold.")

        passed = score >= risk_rubric.get("passing_threshold", 75)

        if self.client and passed:
            # Optional deep semantic check via Azure OpenAI
            prompt = f"Evaluate if this test output meets quality standards: '{system_output}'. Reply with 'PASS' or 'FAIL' and short reason."
            try:
                res = self.client.chat.completions.create(
                    model=self.deployment,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=50
                )
                ai_verdict = res.choices[0].message.content
                violations.append(f"Azure OpenAI Judge verdict: {ai_verdict}")
            except Exception as e:
                violations.append(f"AI evaluation notice: {str(e)}")

        audit_record = {
            "test_case": test_name,
            "evaluator_model": self.deployment,
            "system_output_sample": system_output[:150],
            "risk_rubric_applied": risk_rubric,
            "calculated_score": score,
            "gate_passed": passed,
            "explainability_reasoning": violations if violations else ["Output adheres to all enterprise quality rubrics."]
        }
        return audit_record

if __name__ == "__main__":
    judge = AzureLLMJudge()
    rubric = {"passing_threshold": 80, "min_length": 10, "allow_errors": False}
    
    result = judge.evaluate_test_output("UI Login Flow", "Secure login verified successfully with flash message.", rubric)
    print("Governance Audit Report:\n", json.dumps(result, indent=2))
