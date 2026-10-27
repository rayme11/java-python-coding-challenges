# Azure AI-Enhanced Enterprise Quality Engineering Lab

> **Role:** Lead QA Engineering Manager  
> **Objective:** Implement a production-grade, low-cost AI test automation & governance lab using Python, Playwright, REST APIs, and Azure AI (Azure OpenAI Service) connected to real target applications (`https://the-internet.herokuapp.com`).

---

## 🎯 Lab Architecture & QA Leadership Strategy

As a QA Leader, your goal is to build an intelligent, defensible testing pipeline that solves the **AI Paradox in QA** (high test generation vs. rising defect rates) while keeping cloud and AI inference costs extremely low.

### Cost Control Strategy (Strictly Low Cost / Free Tier)
1. **Target App:** Uses the free, publicly available Heroku test app (`https://the-internet.herokuapp.com`) and JSONPlaceholder APIs—zero hosting costs.
2. **Compute:** GitHub Actions free tier for CI/CD execution.
3. **AI Inference:** Azure OpenAI Service (GPT-4o-mini or GPT-3.5-turbo) configured with low token limits and strict temperature settings. Costs pennies per run (~$0.001 per test evaluation).

---

## 📁 Lab Structure

```
azure-ai-qe-lab/
├── README.md                          # This master lab guide
├── requirements.txt                   # Python dependencies (playwright, pytest, requests, openai)
├── tests/
│   ├── test_ui_playwright.py          # Python Playwright UI automation
│   └── test_api_rest.py               # REST API validation tests
├── ai_governance/
│   ├── data_synthesizer.py            # AI test data generation (Azure OpenAI / Mock)
│   └── llm_judge.py                   # LLM-as-a-Judge evaluation & Trust Architecture logging
└── .github/
    └── workflows/
        └── azure-qe-lab-ci.yml        # CI/CD pipeline executing tests & AI governance
```

---

## 🚀 Step-by-Step Implementation Guide

### Step 1: Environment Setup
1. Install Python 3.10+ and dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```
2. Set up environment variables for Azure OpenAI (optional for local testing; mock fallback included):
   ```powershell
   $env:AZURE_OPENAI_API_KEY="your-azure-openai-key"
   $env:AZURE_OPENAI_ENDPOINT="https://your-resource-name.openai.azure.com/"
   $env:AZURE_OPENAI_DEPLOYMENT="gpt-4o-mini"
   ```

### Step 2: Run UI Automation (Playwright Python)
```bash
pytest tests/test_ui_playwright.py --headed
```

### Step 3: Run API Tests
```bash
pytest tests/test_api_rest.py
```

### Step 4: Run AI Test Data Synthesis & LLM-as-a-Judge Governance
```bash
python ai_governance/data_synthesizer.py
python ai_governance/llm_judge.py
```
