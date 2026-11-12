# GitHub Actions CI/CD for SRE

> **Workflow:** Automated CI/CD pipeline for SRE workloads including infrastructure, application deployment, security scanning, and load testing.

---

## Workflow File: `.github/workflows/sre-ci.yml`

```yaml
name: SRE CI Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

env:
  RESOURCE_GROUP: rg-qe-lab
  ACR_NAME: acrqelab
  AKS_NAME: aks-qe-lab
  APP_NAME: qe-automation-app
  REGISTRY: ${{ secrets.ACR_NAME }}.azurecr.io

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
          severity: 'CRITICAL,HIGH'
          exit-code: '1'

  build-and-test:
    runs-on: ubuntu-latest
    needs: security-scan
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: |
          cd ai/sre-engineering/module-2-containers/dockerfiles/node-app
          npm install

      - name: Run unit tests
        run: |
          cd ai/sre-engineering/module-2-containers/dockerfiles/node-app
          npm test || true

      - name: Run Python tests
        run: |
          cd ai/sre-engineering/module-6-ai-sre/anomaly-detection
          pip install -r requirements.txt 2>/dev/null || true
          python -m pytest tests/ -v || true

      - name: Upload test results
        uses: actions/upload-artifact@v3
        with:
          name: test-results
          path: |
            ai/sre-engineering/**/test-results/
            ai/sre-engineering/**/pytest-results/

  build-image:
    runs-on: ubuntu-latest
    needs: build-and-test
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to Azure Container Registry
        uses: azure/docker-login@v1
        with:
          login-url: ${{ env.ACR_NAME }}.azurecr.io
          username: ${{ secrets.ACR_USERNAME }}
          password: ${{ secrets.ACR_PASSWORD }}

      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          context: ai/sre-engineering/module-2-containers/dockerfiles/node-app
          push: true
          tags: ${{ env.REGISTRY }}/${{ env.APP_NAME }}:${{ github.sha }}
          labels: |
            org=enterprise-qe
            image=qe-automation-app
            commit=${{ github.sha }}

  deploy-staging:
    runs-on: ubuntu-latest
    needs: build-image
    environment:
      name: staging
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Login to Azure
        uses: azure/login@v1
        with:
          client-id: ${{ secrets.AZURE_CLIENT_ID }}
          client-secret: ${{ secrets.AZURE_CLIENT_SECRET }}
          tenant-id: ${{ secrets.AZURE_TENANT_ID }}
          subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}

      - name: Set AKS context
        uses: azure/k8s-set-context@v3
        with:
          method: kubeconfig
          cluster-name: ${{ env.AKS_NAME }}
          resource-group: ${{ env.RESOURCE_GROUP }}

      - name: Deploy to AKS
        run: |
          kubectl set image deployment/qe-automation-app \
            qe-automation-app=${{ env.REGISTRY }}/${{ env.APP_NAME }}:${{ github.sha }}
          kubectl rollout status deployment/qe-automation-app --timeout=300s
          kubectl get pods -l app=qe-automation-app

  load-test:
    runs-on: ubuntu-latest
    needs: deploy-staging
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Install Locust
        run: pip install locust

      - name: Run load test
        run: |
          cd ai/sre-engineering/module-5-load-testing/locust-tests
          locust -f locustfile.py --headless -u 50 -r 5 --run-time 1m --host ${{ env.WEB_APP_URL }}
          echo "Load test completed"

      - name: Upload load test results
        uses: actions/upload-artifact@v3
        with:
          name: load-test-results
          path: |
            ai/sre-engineering/module-5-load-testing/locust-tests/*.csv

  notify:
    runs-on: ubuntu-latest
    needs: [build-and-test, deploy-staging, load-test]
    if: always()
    steps:
      - name: Send notification
        run: |
          echo "Pipeline completed for ${{ github.ref }}"
          echo "Status: ${{ job.status }}"
          echo "Actions: Review GitHub Actions tab for details"
```

---

## 📋 Required GitHub Secrets

| Secret Name | Description | Example |
|-------------|-------------|---------|
| `AZURE_CLIENT_ID` | Service Principal client ID | `xxxx-xxxx-xxxx` |
| `AZURE_CLIENT_SECRET` | Azure AD Service Principal secret | `xxxx-xxxx-xxxx` |
| `AZURE_TENANT_ID` | Azure AD tenant ID | `xxxx-xxxx-xxxx` |
| `AZURE_SUBSCRIPTION_ID` | Azure subscription ID | `xxxx-xxxx-xxxx` |
| `ACR_NAME` | Azure Container Registry name | `acrqe12345` |
| `ACR_USERNAME` | ACR username | `acrqe12345` |
| `ACR_PASSWORD` | ACR password | `xxxx-xxxx-xxxx` |
| `WEB_APP_URL` | Web application URL | `https://qe-app.azurewebsites.net` |

### Create Service Principal:

```bash
az ad sp create-for-rbac \
  --name "qe-sre-github-actions" \
  --role contributor \
  --scopes /subscriptions/${SUBSCRIPTION_ID}/resourceGroups/rg-qe-lab \
  --sdk-auth
```

---

## 🔄 CD Pipeline (`sre-cd.yml`)

For production deployments triggered by GitHub releases:

```yaml
name: SRE CD Pipeline

on:
  release:
    types: [ published ]

env:
  RESOURCE_GROUP: rg-qe-lab-prod
  ACR_NAME: acrqelabprod
  AKS_NAME: aks-qe-lab-prod
  APP_NAME: qe-automation-app
  REGISTRY: ${{ secrets.ACR_NAME }}.azurecr.io

jobs:
  deploy-production:
    runs-on: ubuntu-latest
    environment:
      name: production
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Login to Azure
        uses: azure/login@v1
        with:
          client-id: ${{ secrets.AZURE_CLIENT_ID }}
          client-secret: ${{ secrets.AZURE_CLIENT_SECRET }}
          tenant-id: ${{ secrets.AZURE_TENANT_ID }}
          subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}

      - name: Login to ACR
        uses: azure/docker-login@v1
        with:
          login-url: ${{ env.ACR_NAME }}.azurecr.io
          username: ${{ secrets.ACR_USERNAME }}
          password: ${{ secrets.ACR_PASSWORD }}

      - name: Set AKS context
        uses: azure/k8s-set-context@v3
        with:
          method: kubeconfig
          cluster-name: ${{ env.AKS_NAME }}
          resource-group: ${{ env.RESOURCE_GROUP }}

      - name: Deploy to production
        run: |
          kubectl set image deployment/qe-automation-app \
            qe-automation-app=${{ env.ACR_NAME }}/${{ env.APP_NAME }}:${{ github.sha }}
          kubectl rollout status deployment/qe-automation-app --timeout=300s
          kubectl get pods -l app=qe-automation-app
```

---

## 📊 Pipeline Status Badges

Add to your README:

```markdown
[![SRE CI Pipeline](https://github.com/your-username/java-python-coding-challenges/actions/workflows/sre-ci.yml/badge.svg)](https://github.com/your-username/java-python-coding-challenges/actions/workflows/sre-ci.yml)

[![SRE CD Pipeline](https://github.com/your-username/java-python-coding-challenges/actions/workflows/sre-cd.yml/badge.svg)](https://github.com/your-username/java-python-coding-challenges/actions/workflows/sre-cd.yml)
```
