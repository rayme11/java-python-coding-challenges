import os
import json
from pathlib import Path
from dotenv import load_dotenv
from openai import AzureOpenAI

env_path = Path(__file__).resolve().parent.parent / '.env'
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
else:
    load_dotenv()

class AzureAIDataSynthesizer:
    """
    Synthesizes test data using Azure OpenAI Service with automatic fallback to mock data.
    """
    def __init__(self):
        self.api_key = os.getenv("AZURE_OPENAI_API_KEY")
        self.endpoint = os.getenv("AZURE_OPENAI_ENDPOINT") # This is now the base_url
        self.deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
        self.api_version = os.getenv("AZURE_OPENAI_API_VERSION") # Re-enabled

        print(f"DEBUG: OpenAI API Key (first 5 chars): {self.api_key[:5] if self.api_key else 'N/A'}")
        print(f"DEBUG: OpenAI Endpoint (Base URL): {self.endpoint}")
        print(f"DEBUG: OpenAI Deployment Name: {self.deployment}")
        print(f"DEBUG: OpenAI API Version: {self.api_version}") # Re-enabled

        if self.api_key and self.endpoint and self.deployment and self.api_version and "your-resource-name" not in self.endpoint:
            try:
                self.client = AzureOpenAI(
                    api_key=self.api_key,
                    api_version=self.api_version, # Re-enabled
                    base_url=f"{self.endpoint}/deployments/{self.deployment}"
                )
            except Exception as e:
                print(f"DEBUG: AzureOpenAI client initialization failed: {e}")
                self.client = None
        else:
            self.client = None

    def synthesize_test_payload(self, schema_description: str) -> dict:
        if self.client:
            try:
                print(f"[Azure OpenAI] Generating test payload for: '{schema_description}'...")
                response = self.client.chat.completions.create(
                    model=self.deployment, # Model here is actually deployment_name for AzureOpenAI client
                    messages=[
                        {"role": "system", "content": "You are a QA automation expert generating valid JSON test payloads."},
                        {"role": "user", "content": f"Generate a JSON test payload based on this requirement: {schema_description}"}
                    ],
                    max_tokens=150,
                    temperature=0.3
                )
                content = response.choices[0].message.content
                return json.loads(content)
            except Exception as e:
                print(f"[Azure OpenAI Fallback] API connection or generation failed ({e}). Using smart mock synthesizer.")
        
        print(f"[Smart Mock Data Synthesizer] Synthesizing payload for: '{schema_description}'")
        return {
            "username": "synthetic_user_99",
            "email": "synthetic.qa@enterprise.org",
            "role": "QA_MANAGER",
            "requirement_processed": schema_description
        }

if __name__ == "__main__":
    synthesizer = AzureAIDataSynthesizer()
    payload = synthesizer.synthesize_test_payload("Generate user profile schema with valid email and phone number")
    print("Synthesizer Output:\n", json.dumps(payload, indent=2))
