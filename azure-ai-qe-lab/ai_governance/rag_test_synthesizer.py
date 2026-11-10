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

class AzureRAGTestSynthesizer:
    """
    Implements Retrieval-Augmented Generation (RAG) and Vector Data Grounding
    for AI-driven test case and test data generation.
    """
    def __init__(self):
        self.api_key = os.getenv("AZURE_OPENAI_API_KEY")
        self.endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o-mini")
        
        # Simulated Internal Enterprise Architectural Knowledge Base (Vector Store / Azure AI Search index)
        self.knowledge_base = [
            {
                "id": "doc-001",
                "title": "Authentication Security Specification v2.4",
                "content": "Rule SEC-01: Passwords must be at least 12 characters long, contain uppercase, lowercase, numbers, and special symbols. Rule SEC-02: Accounts must lock out after 5 consecutive failed login attempts for 30 minutes."
            },
            {
                "id": "doc-002",
                "title": "API Rate Limiting & Payload Compliance",
                "content": "Rule API-09: All REST endpoints must return HTTP 429 Too Many Requests when request rate exceeds 100 req/min per API key. Payload must include standard error schema { error_code, timestamp, message }."
            },
            {
                "id": "doc-003",
                "title": "Session Management & Token Expiry",
                "content": "Rule SES-04: JWT access tokens expire in 15 minutes. Refresh tokens expire in 7 days. Inactive browser sessions must terminate after 20 minutes of idle time."
            }
        ]

        if self.api_key and self.endpoint and "your-resource-name" not in self.endpoint:
            try:
                self.client = AzureOpenAI(
                    api_key=self.api_key,
                    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01"),
                    azure_endpoint=self.endpoint
                )
            except Exception:
                self.client = None
        else:
            self.client = None

    def retrieve_relevant_docs(self, query: str) -> list:
        """
        Simulates Vector Search / Azure AI Search retrieval step based on semantic keyword match.
        In production Azure AI Search, this performs approximate nearest neighbor (ANN) vector search.
        """
        print(f"[Azure AI Search (RAG)] Querying vector index for: '{query}'...")
        retrieved = []
        query_lower = query.lower()
        for doc in self.knowledge_base:
            if any(kw in doc["content"].lower() for kw in query_lower.split()):
                retrieved.append(doc)
        
        if not retrieved:
            retrieved = [self.knowledge_base[0]] # Default fallback doc
            
        print(f"[Azure AI Search (RAG)] Retrieved {len(retrieved)} relevant architectural document(s).")
        return retrieved

    def synthesize_grounded_test_cases(self, user_story: str) -> dict:
        # Step 1: Retrieval
        retrieved_docs = self.retrieve_relevant_docs(user_story)
        context_chunks = "\n\n".join([f"[{doc['title']}]: {doc['content']}" for doc in retrieved_docs])

        # Step 2: Prompt Grounding
        grounded_prompt = f"""
[Internal Enterprise Architectural Grounding Context]:
{context_chunks}

[Task]:
Generate structured QA test cases and synthetic test data for the following user story, strictly adhering to the internal architectural rules provided in the grounding context above.

[User Story]:
{user_story}

Return the response in valid JSON format containing:
1. "test_cases": list of test scenarios with title, pre_conditions, steps, and expected_results.
2. "synthetic_test_data": valid inputs matching the rules.
"""

        if self.client:
            try:
                print(f"[Azure OpenAI (RAG Prompt Grounding)] Generating grounded test cases...")
                response = self.client.chat.completions.create(
                    model=self.deployment,
                    messages=[
                        {"role": "system", "content": "You are an expert QA Enterprise Architect using RAG to ensure 100% compliance with internal security specifications."},
                        {"role": "user", "content": grounded_prompt}
                    ],
                    max_tokens=600,
                    temperature=0.2
                )
                content = response.choices[0].message.content
                return json.loads(content)
            except Exception as e:
                print(f"[Azure OpenAI Fallback] RAG API call failed ({e}). Using smart grounded mock generator.")

        # Smart grounded mock response adhering strictly to retrieved rules
        return {
            "grounding_sources_used": [doc['id'] for doc in retrieved_docs],
            "test_cases": [
                {
                    "title": "Verify Password Complexity Enforcement (SEC-01)",
                    "pre_conditions": "User is on registration page",
                    "steps": ["Enter password with < 12 chars", "Verify validation error"],
                    "expected_result": "System rejects password and enforces SEC-01 rule."
                },
                {
                    "title": "Verify Account Lockout After 5 Failed Logins (SEC-02)",
                    "pre_conditions": "Valid user account exists",
                    "steps": ["Enter incorrect password 5 consecutive times"],
                    "expected_result": "Account is locked for 30 minutes per SEC-02 specification."
                }
            ],
            "synthetic_test_data": {
                "valid_password": "SecurePassword123!",
                "invalid_password": "weak",
                "max_failed_attempts": 5
            }
        }

if __name__ == "__main__":
    print("=== Azure OpenAI RAG & Vector Data Grounding QE Harness ===")
    rag_synthesizer = AzureRAGTestSynthesizer()
    
    story = "As a user, I want secure authentication with lockout protection and strict password rules."
    result = rag_synthesizer.synthesize_grounded_test_cases(story)
    print("\nGrounded RAG Output:\n", json.dumps(result, indent=2))
