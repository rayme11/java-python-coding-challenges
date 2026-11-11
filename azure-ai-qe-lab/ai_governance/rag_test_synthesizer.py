import os
import json
from pathlib import Path
from dotenv import load_dotenv
from openai import AzureOpenAI
import requests

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
        # Azure OpenAI Configuration
        self.openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
        self.openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.openai_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o-mini")
        self.openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01")

        if self.openai_api_key and self.openai_endpoint and "your-resource-name" not in self.openai_endpoint:
            try:
                self.openai_client = AzureOpenAI(
                    api_key=self.openai_api_key,
                    api_version=self.openai_api_version,
                    azure_endpoint=self.openai_endpoint
                )
            except Exception:
                self.openai_client = None
        else:
            self.openai_client = None

        # Azure AI Search Configuration
        self.search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
        self.search_admin_key = os.getenv("AZURE_SEARCH_ADMIN_KEY")
        self.search_index_name = "enterprise-qe-scripts-idx"
        self.search_api_version = "2023-11-01"

        # Simulated Internal Enterprise Architectural Knowledge Base (Local fallback)
        self.local_knowledge_base = [
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

    def retrieve_relevant_docs(self, query: str) -> list:
        """
        Queries Azure AI Search for relevant documents, or falls back to local mock knowledge base.
        """
        if self.search_endpoint and self.search_admin_key and "your-search-service-name" not in self.search_endpoint:
            try:
                print(f"[Azure AI Search (RAG)] Querying enterprise vector index for: '{query}'...")
                url = f"{self.search_endpoint}/indexes/{self.search_index_name}/docs/search?api-version={self.search_api_version}"
                headers = {
                    "Content-Type": "application/json",
                    "api-key": self.search_admin_key
                }
                payload = {
                    "search": query,
                    "queryType": "simple", # Use simple query type for basic keyword search
                    "select": "id, title, content", # Select fields to retrieve
                    "top": 3
                }
                response = requests.post(url, json=payload, headers=headers)
                response.raise_for_status() # Raise an exception for HTTP errors
                search_results = response.json().get("value", [])
                retrieved = []
                for result in search_results:
                    retrieved.append({"id": result["id"], "title": result["title"], "content": result["content"]})
                
                print(f"[Azure AI Search (RAG)] Retrieved {len(retrieved)} relevant document(s) from Azure AI Search.")
                return retrieved if retrieved else self.local_knowledge_base[:1] # Fallback to local if Azure Search returns empty
            except Exception as e:
                print(f"[Azure AI Search Fallback] Connection or search failed ({e}). Using local mock knowledge base.")
        
        # Local mock retrieval based on keyword match
        print(f"[Local Mock RAG] Querying local knowledge base for: '{query}'...")
        retrieved = []
        query_lower = query.lower()
        for doc in self.local_knowledge_base:
            if any(kw in doc["content"].lower() for kw in query_lower.split()):
                retrieved.append(doc)
        
        if not retrieved:
            retrieved = [self.local_knowledge_base[0]] # Default fallback doc
            
        print(f"[Local Mock RAG] Retrieved {len(retrieved)} relevant architectural document(s) locally.")
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

        if self.openai_client:
            try:
                print(f"[Azure OpenAI (RAG Prompt Grounding)] Generating grounded test cases...")
                response = self.openai_client.chat.completions.create(
                    model=self.openai_deployment,
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
