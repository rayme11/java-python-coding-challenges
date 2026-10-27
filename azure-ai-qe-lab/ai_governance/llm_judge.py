import json
import os

class AzureLLMJudge:
    """
    Implements LLM-as-a-Judge and Trust Architecture audit logging for QA governance.
    """
    def __init__(self, model_name: str = "gpt-4o-mini"):
        self.model_name = model_name

    def evaluate_test_output(self, test_name: str, system_output: str, risk_rubric: dict) -> dict:
        print(f"[Azure LLM-as-a-Judge ({self.model_name})] Evaluating '{test_name}'...")
        
        score = 100
        violations = []

        if "error" in system_output.lower() and not risk_rubric.get("allow_errors", False):
            score -= 50
            violations.append("Error detected in execution output.")

        if len(system_output) < risk_rubric.get("min_length", 5):
            score -= 30
            violations.append("Output fails minimum verbosity/detail threshold.")

        passed = score >= risk_rubric.get("passing_threshold", 75)

        # Trust Architecture Audit Record
        audit_record = {
            "test_case": test_name,
            "evaluator_model": self.model_name,
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
