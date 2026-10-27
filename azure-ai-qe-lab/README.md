# Enterprise Azure AI Quality Engineering & Governance Lab

> **Role:** Senior QA Engineering Manager / AI QE Leader  
> **Objective:** A comprehensive, step-by-step master guide to implementing low-cost, production-grade AI test automation, LLM data synthesis, LLM-as-a-Judge validation, Local Model Context Protocol (MCP) servers, and RAG data grounding on Microsoft Azure.

---

## 📑 Table of Contents
1. [Executive Architecture & Cost Control Strategy](#1-executive-architecture--cost-control-strategy)
2. [Module 1: Step-by-Step Azure AI Portal Setup](#2-module-1-step-by-step-azure-ai-portal-setup)
3. [Module 2: Enterprise Configuration Standards (.env)](#3-module-2-enterprise-configuration-standards-env)
4. [Module 3: Local MCP Server & Internal System Integration](#4-module-3-local-mcp-server--internal-system-integration)
5. [Module 4: UI (Playwright Python) & API Test Automation](#5-module-4-ui-playwright-python--api-test-automation)
6. [Module 5: AI Data Synthesis & LLM-as-a-Judge Governance](#6-module-5-ai-data-synthesis--llm-as-a-judge-governance)
7. [Module 6: Data Grounding (RAG) in Azure OpenAI](#7-module-6-data-grounding-rag-in-azure-openai)
8. [Module 7: GitHub & GitHub Actions CI/CD Pipeline](#8-module-7-github--github-actions-cicd-pipeline)

---

## 1. Executive Architecture & Cost Control Strategy

As an AI Quality Engineering Leader, your objective is to build a robust, defensible test automation pipeline while maintaining strict cost control (paying only pennies for AI inference on your own learning budget).

- **Target Applications:** Publicly available test applications (`https://the-internet.herokuapp.com` and JSONPlaceholder APIs) = **$0 hosting cost**.
- **CI/CD Execution:** GitHub Actions free tier runners = **$0 compute cost**.
- **AI Inference:** Azure OpenAI Service configured with `gpt-4o-mini` on Pay-As-You-Go with low `max_tokens` limits = **<$1/month**.

---

## 2. Module 1: Step-by-Step Azure AI Portal Setup

Follow these exact steps in the Azure Portal to provision your low-cost AI backend:

1. **Log in to Azure Portal:** Navigate to [portal.azure.com](https://portal.azure.com).
2. **Create Azure OpenAI Resource:**
   - Click **Create a resource** -> Search for **Azure OpenAI** -> Click **Create**.
   - Select your subscription and create a new Resource Group (e.g., `rg-ai-qe-lab-prod`).
   - Choose a region close to you (e.g., `East US` or `Sweden Central`).
   - Give your resource a unique name (e.g., `aoai-qe-manager-lab`).
   - Select the **S0** pricing tier (Standard pay-as-you-go). Click **Review + create** -> **Create**.
3. **Deploy the Model (`gpt-4o-mini`):**
   - Once deployment completes, click **Go to resource**.
   - In the left sidebar under *Resource Management*, click **Model deployments** -> Click **Manage Deployments** (opens Azure AI Foundry / OpenAI Studio).
   - Click **Create new deployment**:
     - **Model name:** `gpt-4o-mini` (cost-optimized and exceptionally fast for QE tasks).
     - **Deployment name:** `gpt-4o-mini`
     - Click **Create**.
4. **Retrieve Credentials:**
   - Back in the Azure Portal under your Azure OpenAI resource, click **Keys and Endpoint** in the left sidebar.
   - Copy **Key 1** and your **Endpoint URL**.

---

## 3. Module 2: Enterprise Configuration Standards (.env)

In enterprise environments, hardcoding API keys is a critical security violation. We use `.env` files managed by `python-dotenv`.

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Populate your `.env` with your Azure credentials:
   ```env
   AZURE_OPENAI_API_KEY="your_actual_azure_openai_key"
   AZURE_OPENAI_ENDPOINT="https://your-resource-name.openai.azure.com/"
   AZURE_OPENAI_DEPLOYMENT_NAME="gpt-4o-mini"
   AZURE_OPENAI_API_VERSION="2024-02-01"
   LOCAL_MCP_SERVER_PORT=8000
   ```

---

## 4. Module 3: Local MCP Server & Internal System Integration

The **Model Context Protocol (MCP)** enables LLM agents to securely query internal enterprise systems (test metrics, bug trackers, CI logs).

1. **Start your Local MCP Server:**
   ```bash
   python mcp_server/local_mcp_server.py
   ```
2. **Test the MCP Tool Endpoint:**
   Open your browser or run curl to see the JSON tool response:
   `http://localhost:8000/mcp/tools/get_test_metrics`

---

## 5. Module 4: UI (Playwright Python) & API Test Automation

- **UI Test Suite (`tests/test_ui_playwright.py`):** Uses Python Playwright to test the Heroku secure authentication flow.
- **API Test Suite (`tests/test_api_rest.py`):** Validates REST contract compliance and JSON schemas against JSONPlaceholder.

Run all tests via pytest:
```bash
pytest -v
```

---

## 6. Module 5: AI Data Synthesis & LLM-as-a-Judge Governance

- **AI Data Synthesizer (`ai_governance/data_synthesizer.py`):** Leverages Azure OpenAI to generate contextual test payloads.
- **LLM-as-a-Judge (`ai_governance/llm_judge.py`):** Evaluates unstructured outputs against strict enterprise risk rubrics and emits **Trust Architecture** explainability audit logs.

Run governance scripts:
```bash
python ai_governance/data_synthesizer.py
python ai_governance/llm_judge.py
```

---

## 7. Module 6: Data Grounding (RAG) in Azure OpenAI

**Data Grounding / Retrieval-Augmented Generation (RAG)** ensures that AI-generated test scenarios and code comply strictly with internal company guidelines and architecture specs rather than generic training data.

### How to Implement RAG in Azure:
1. **Vector Store:** Index your internal architectural wikis, acceptance criteria, and compliance docs into **Azure AI Search**.
2. **Retrieval Step:** When generating test cases, query Azure AI Search for relevant design documents matching the user story.
3. **Prompt Grounding:** Inject the retrieved context into the system prompt:
   ```python
   prompt = f"""
   [Internal Architecture Grounding Context]:
   {retrieved_wiki_chunks}

   [Task]:
   Generate test cases for user story #402 strictly adhering to the internal standards above.
   """
   ```

---

## 8. Module 7: GitHub & GitHub Actions CI/CD Pipeline

The `.github/workflows/azure-qe-lab-ci.yml` workflow automatically runs your Playwright UI tests, REST API tests, and AI governance checks on every push.

### Setting Secrets in GitHub:
1. Go to your GitHub repository -> **Settings** -> **Secrets and variables** -> **Actions**.
2. Add a new repository secret named `AZURE_OPENAI_API_KEY` and paste your key.
3. Add a repository secret named `AZURE_OPENAI_ENDPOINT` and paste your endpoint URL.
