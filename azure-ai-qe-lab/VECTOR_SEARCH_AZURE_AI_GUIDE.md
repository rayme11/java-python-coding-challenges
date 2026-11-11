# Master Guide: Indexing UI & API Automation Scripts into Azure AI Search for Enterprise RAG

## Overview

As an AI Quality Engineering Leader, one of the most powerful architectural patterns you can build is a **Self-Learning Test Strategy Engine**. Instead of writing test cases from scratch, your AI pipeline queries a vector database containing all your existing UI scripts (Playwright/Selenium), API contracts (REST Assured/Requests), and compliance rules. 

This guide walks you step-by-step through provisioning Azure AI Search, importing our sample UI & API dataset (`vector_data/sample_ui_api_specs.json`), and connecting it to your local RAG synthesizer.

---

## 📁 1. The Sample Dataset (`vector_data/sample_ui_api_specs.json`)

In your repository (`azure-ai-qe-lab/vector_data/sample_ui_api_specs.json`), we have prepared a structured JSON dataset representing real enterprise artifacts:
- **UI Automation Scripts:** Playwright login Page Object models and E-commerce checkout flows with CSS selectors and assertions.
- **API Test Specifications:** REST contract tests for GET `/posts/{id}` and POST `/users` with expected schemas and rate-limiting rules.

---

## ☁️ 2. Step-by-Step Azure AI Search Portal Setup

Follow these exact steps in the Azure Portal to set up your vector database:

### Step A: Provision Azure AI Search Service
1. Log in to [portal.azure.com](https://portal.azure.com).
2. Click **Create a resource** -> Search for **AI Search** (or Azure Cognitive Search) -> Click **Create**.
3. Configure the service:
   - **Subscription:** Select your Azure subscription.
   - **Resource Group:** Select your lab resource group (e.g., `rg-ai-qe-lab-prod`).
   - **Service Name:** Give it a unique name (e.g., `search-qe-manager-lab`).
   - **Location:** Choose a region close to you (e.g., `East US`).
   - **Pricing Tier:** Select **Free** or **Basic** (Free tier is $0/month and fully supports vector search for learning).
4. Click **Review + create** -> **Create**.

### Step B: Import Sample Data into an Index
1. Once deployment completes, click **Go to resource**.
2. On the Overview page, click the **Import data** button at the top toolbar.
3. **Connect to your data:**
   - Data Source: Select **Upload a file** (or JSON / Cosmos DB).
   - Upload the file: Select `azure-ai-qe-lab/vector_data/sample_ui_api_specs.json`.
   - Click **Next: Add cognitive skills (Optional)** -> Skip and click **Next: Customize target index**.
4. **Customize Target Index:**
   - **Index name:** `enterprise-qe-scripts-idx`
   - **Key:** Select `id` (Edm.String).
   - Check **Retrievable**, **Searchable**, and **Filterable** for fields like `title`, `component`, `description`, `selectors`, and `endpoint`.
5. **Create Indexer:**
   - Click **Next: Create an indexer** -> Name it `qe-scripts-indexer`.
   - Click **Submit**. Azure AI Search will instantly parse, index, and vectorize your UI/API script specs!

### Step C: Retrieve API Key & Endpoint
1. Go back to your Search Service overview page.
2. Click **Keys** in the left sidebar.
3. Copy your **Primary admin key** and your **Service URL** (e.g., `https://search-qe-manager-lab.search.windows.net`).

---

## 💻 3. What Happens Locally: Connecting Python RAG to Azure AI Search

When your AI agent needs to generate a new test case for a user story, it queries Azure AI Search using semantic keyword/vector search to find related existing scripts. 

### Local Python Integration Snippet:
```python
import os
import requests

def query_azure_ai_search(user_story: str):
    search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT") # e.g. https://search-qe-manager-lab.search.windows.net
    search_key = os.getenv("AZURE_SEARCH_ADMIN_KEY")
    index_name = "enterprise-qe-scripts-idx"
    
    url = f"{search_endpoint}/indexes/{index_name}/docs/search?api-version=2023-11-01"
    headers = {
        "Content-Type": "application/json",
        "api-key": search_key
    }
    payload = {
        "search": user_story,
        "top": 3
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json().get("value", [])
```

---

## 🎯 4. Summary: The Enterprise Value
By indexing your existing UI and API automation scripts into Azure AI Search:
1. **Zero Duplication:** AI checks existing test assets before generating new ones.
2. **Pattern Reuse:** AI adopts your team's exact Page Object selectors and assertion libraries.
3. **Continuous Growth:** Every new test added to CI/CD expands the vector database, compounding your test engineering intelligence over time.
