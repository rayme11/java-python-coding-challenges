# Enterprise Azure AI Quality Engineering & Governance Lab

> **Role:** Senior QA Engineering Manager / AI QE Leader  
> **Objective:** A comprehensive, step-by-step master guide to implementing low-cost, production-grade AI test automation, LLM data synthesis, LLM-as-a-Judge validation, Local Model Context Protocol (MCP) servers, and RAG data grounding on Microsoft Azure.

---

## 📑 Table of Contents
1. [Executive Architecture & Cost Control Strategy](#1-executive-architecture--cost-control-strategy)
2. [Step-by-Step Implementation Guide](#-step-by-step-implementation-guide)
3. [Module 1: Step-by-Step Azure AI Portal Setup](#2-module-1-step-by-step-azure-ai-portal-setup)
4. [Module 2: Enterprise Configuration Standards (.env)](#3-module-2-enterprise-configuration-standards-env)
5. [Module 3: Local MCP Server & Internal System Integration](#4-module-3-local-mcp-server--internal-system-integration)
6. [Module 4: UI (Playwright Python) & API Test Automation](#5-module-4-ui-playwright-python--api-test-automation)
7. [Module 5: AI Data Synthesis & LLM-as-a-Judge Governance](#6-module-5-ai-data-synthesis--llm-as-a-judge-governance)
8. [Module 6: Data Grounding (RAG) & Azure AI Search Vector Database](#7-module-6-data-grounding-rag--azure-ai-search-vector-database)
9. [Module 7: GitHub & GitHub Actions CI/CD Pipeline](#8-module-7-github--github-actions-cicd-pipeline)

---

## 1. Executive Architecture & Cost Control Strategy

As an AI Quality Engineering Leader, your objective is to build a robust, defensible test automation pipeline while maintaining strict cost control (paying only pennies for AI inference on your own learning budget).

- **Target Applications:** Publicly available test applications (`https://the-internet.herokuapp.com` and JSONPlaceholder APIs) = **$0 hosting cost**.
- **CI/CD Execution:** GitHub Actions free tier runners = **$0 compute cost**.
- **AI Inference:** Azure OpenAI Service configured with `gpt-4o-mini` on Pay-As-You-Go with low `max_tokens` limits = **<$1/month**.

---

## 🚀 Step-by-Step Implementation Guide

### Step 1: Environment Setup
1. Ensure Python 3.10+ is installed and accessible in your terminal (`python`).
2. Navigate to the `azure-ai-qe-lab` directory:
   ```powershell
   cd azure-ai-qe-lab
   ```
3. Install Python dependencies and Playwright browsers:
   ```powershell
   python -m pip install -r requirements.txt
   python -m playwright install chromium
   ```
4. Set up environment variables for Azure OpenAI (optional for local testing; mock fallback included) by copying `.env.example` to `.env`:
   ```powershell
   Copy-Item .env.example .env
   ```
   Populate your `.env` with your Azure credentials.

### Step 2: Launch Local MCP Server & Inspect Tools
To launch the MCP Server and automatically open the interactive Web UI Inspector:
```powershell
npx.cmd @modelcontextprotocol/inspector python mcp_server/local_mcp_server.py
```

### Step 3: Run UI Automation (Playwright Python)
To run UI tests with step-by-step console print statements visible (`-s`) and watch the browser execute visually (`--headed`):
```powershell
python -m pytest tests/test_ui_playwright.py -v -s --headed
```

### Step 4: Run API Tests
```powershell
python -m pytest tests/test_api_rest.py -v -s
```

### Step 5: Run AI Governance (LLM-as-a-Judge) & Data Synthesis
```powershell
python ai_governance/data_synthesizer.py
python ai_governance/llm_judge.py
```

### Step 6: Run RAG & Vector Data Grounding
```powershell
python ai_governance/rag_test_synthesizer.py
```

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

```env
AZURE_OPENAI_API_KEY="your_actual_azure_openai_key"
AZURE_OPENAI_ENDPOINT="https://your-resource-name.openai.azure.com/"
AZURE_OPENAI_DEPLOYMENT_NAME="gpt-4o-mini"
AZURE_OPENAI_API_VERSION="2024-02-01"
LOCAL_MCP_SERVER_PORT=8000
```

---

## 4. Module 3: Local MCP Server & Internal System Integration

The **Model Context Protocol (MCP)** enables LLM agents to securely query internal enterprise systems (test metrics, bug trackers, CI logs) via standardized JSON-RPC over STDIO.

1. **Launch the Official MCP Inspector UI:**
   ```powershell
   npx.cmd @modelcontextprotocol/inspector python mcp_server/local_mcp_server.py
   ```
2. **Inspect & Test Tools:**
   The MCP Inspector will spin up an interactive web dashboard in your browser where you can view live JSON-RPC messages, prompts, and execute the `get_test_metrics` tool in real time.

---

## 5. Module 4: UI (Playwright Python) & API Test Automation

- **UI Test Suite (`tests/test_ui_playwright.py`):** Uses Python Playwright to test the Heroku secure authentication flow with real-time terminal step logging (`-s` flag).
- **API Test Suite (`tests/test_api_rest.py`):** Validates REST contract compliance and JSON schemas against JSONPlaceholder.

### How to Run UI Tests:
```powershell
python -m pytest tests/test_ui_playwright.py -v -s --headed
```

### How to Run API Tests:
```powershell
python -m pytest tests/test_api_rest.py -v -s
```

---

## 6. Module 5: AI Data Synthesis & LLM-as-a-Judge Governance

- **AI Data Synthesizer (`ai_governance/data_synthesizer.py`):** Leverages Azure OpenAI to generate contextual test payloads.
- **LLM-as-a-Judge (`ai_governance/llm_judge.py`):** Evaluates unstructured outputs against strict enterprise risk rubrics and emits **Trust Architecture** explainability audit logs.

### How to Run AI Governance Scripts:
```powershell
python ai_governance/data_synthesizer.py
python ai_governance/llm_judge.py
```

---

## 7. Module 6: Data Grounding (RAG) & Azure AI Search Vector Database

**Data Grounding / Retrieval-Augmented Generation (RAG)** ensures that AI-generated test scenarios and code comply strictly with internal company guidelines and architecture specs rather than generic training data.

### 📚 Dedicated Vector Search Guide:
For a complete, step-by-step tutorial on uploading existing UI & API automation scripts to **Azure AI Search** as a vector database, please refer to:
👉 **[`VECTOR_SEARCH_AZURE_AI_GUIDE.md`](./VECTOR_SEARCH_AZURE_AI_GUIDE.md)**

### Sample UI & API Vector Dataset:
We have created a ready-to-import sample dataset located at:
📁 **`vector_data/sample_ui_api_specs.json`**

### How to Run the RAG Test Synthesizer:
```powershell
python ai_governance/rag_test_synthesizer.py
```

---

## 8. Module 7: GitHub & GitHub Actions CI/CD Pipeline

The `.github/workflows/azure-qe-lab-ci.yml` workflow automatically runs your Playwright UI tests, REST API tests, and AI governance checks on every push.

### Setting Secrets in GitHub:
1. Go to your GitHub repository -> **Settings** -> **Secrets and variables** -> **Actions**.
2. Add a new repository secret named `AZURE_OPENAI_API_KEY` and paste your key.
3. Add a repository secret named `AZURE_OPENAI_ENDPOINT` and paste your endpoint URL.
