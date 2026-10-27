import os
import json
from dotenv import load(load_dotenv)
from openai import AzureOpenAI

load_dotenv()

class AzureAIDataSynthesizer:
    """
    Synthesizes test data using Azure OpenAI Service with python-dotenv configuration.
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

    def synthesize_test_payload(self, schema_description: str) -> dict:
        if self.client:
            print(f"[Azure OpenAI] Generating test payload for: '{schema_description}'...")
            response = self.client.chat.completions.create(
                model=self.deployment,
                messages=[
                    {"role": "system", "content": "You are a QA automation expert generating valid JSON test payloads."},
                    {"role": "user", "content": f"Generate a JSON test payload based on this requirement: {schema_description}"}
                ],
                max_tokens=150,
                temperature=0.3
            )
            content = response.choices[0].message.content
            try:
                return json.loads(content)
            except Exception:
                return {"raw_ai_output": content}
        
        print(f"[Smart Mock Fallback (.env missing)] Synthesizing payload for: '{schema_description}'")
        return {
            "username": "synthetic_user_99",
            "email": "synthetic.qa@enterprise.org",
            "role": "QA_MANAGER"
        }

if __name__ == "__main__":
    synthesizer = AzureAIDataSynthesizer()
    payload = synthesizer.synthesize_test_payload("Generate user profile schema with valid email and phone number")
    print("Synthesizer Output:\n", json.dumps(payload, indent=2))
