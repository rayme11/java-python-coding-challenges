# Module 2: Containers (Docker & Kubernetes)

> **Objective:** Learn containerization with Docker, container orchestration with Kubernetes (AKS), and deployment patterns for microservices.

---

## 🎯 Learning Objectives

By completing this module, you will be able to:

- [ ] Write Dockerfiles for containerized applications
- [ ] Build and push container images to Azure Container Registry (ACR)
- [ ] Deploy containers to Azure Kubernetes Service (AKS)
- [ ] Use Helm charts for application deployment
- [ ] Configure Kubernetes Services, Deployments, and ConfigMaps
- [ ] Debug containerized applications in production

---

## 📋 Theory: Containerization & Orchestration

**Why Containers?**

| Benefit | Description |
|---------|-------------|
| Consistency | "Works on my machine" → "Works everywhere" |
| Isolation | Each service runs in its own isolated environment |
| Density | More efficient resource utilization than VMs |
| Portability | Run anywhere Docker/Kubernetes is supported |

**Docker vs Kubernetes:**

| Feature | Docker | Kubernetes (AKS) |
|---------|--------|------------------|
| Purpose | Build & run containers | Orchestrate containers |
| Scope | Single host | Multi-node cluster |
| Complexity | Low | Medium-High |
| Use case | Development, CI/CD | Production workloads |

---

## 🛠️ Step 1: Dockerize a Sample Application

### Create Application Code

**File:** `app.js`

```javascript
const express = require('express');
const os = require('os');

const app = express();
const PORT = process.env.PORT || 3000;
const HOSTNAME = os.hostname();

app.get('/', (req, res) => {
  res.json({
    message: 'Hello from QE Automation Lab!',
    hostname: HOSTNAME,
    timestamp: new Date().toISOString(),
    version: '1.0.0'
  });
});

app.get('/health', (req, res) => {
  res.json({ status: 'healthy', timestamp: new Date().toISOString() });
});

app.get('/ready', (req, res) => {
  res.json({ status: 'ready', timestamp: new Date().toISOString() });
});

app.listen(PORT, () => {
  console.log(`Server running on ${HOSTNAME}:${PORT}`);
});
```

**File:** `package.json`

```json
{
  "name": "qe-automation-app",
  "version": "1.0.0",
  "description": "QE Automation Demo Application",
  "main": "app.js",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  }
}
```

**File:** `.dockerignore`

```
node_modules
npm-debug.log
README.md
.git
.gitignore
```

**File:** `Dockerfile`

```dockerfile
# Use official Node.js image
FROM node:18-alpine

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package*.json ./
RUN npm install --only=production

# Bundle app source
COPY . .

# Expose port
EXPOSE 3000

# Run the application
CMD ["node", "app.js"]
```

---

## 🚀 Step 2: Build and Run Locally

### Install Dependencies

**PowerShell:**
```powershell
cd ai\sre-engineering\module-2-containers\dockerfiles\node-app
npm install
npm start
```

**Bash:**
```bash
cd ai/sre-engineering/module-2-containers/dockerfiles/node-app
npm install
npm start
```

### Test the Application Locally

**PowerShell:**
```powershell
curl http://localhost:3000/
curl http://localhost:3000/health
curl http://localhost:3000/ready
```

**Bash:**
```bash
curl http://localhost:3000/
curl http://localhost:3000/health
curl http://localhost:3000/ready
```

**Expected Output:**
```json
{
  "message": "Hello from QE Automation Lab!",
  "hostname": "your-machine-name",
  "timestamp": "2024-01-15T10:30:00.000Z",
  "version": "1.0.0"
}
```

---

## 🚀 Step 3: Build Docker Image

**PowerShell:**
```powershell
cd ai\sre-engineering\module-2-containers\dockerfiles\node-app

# Build Docker image
docker build -t qe-automation-app:latest .

# Verify image was created
docker images | Select-String "qe-automation"

# Run container locally
docker run -d -p 3000:3000 --name qe-app qe-automation-app:latest

# Test the running container
curl http://localhost:3000/

# Stop and remove container
docker stop qe-app
docker rm qe-app
```

**Bash:**
```bash
cd ai/sre-engineering/module-2-containers/dockerfiles/node-app

# Build Docker image
docker build -t qe-automation-app:latest .

# Verify image was created
docker images | grep qe-automation

# Run container locally
docker run -d -p 3000:3000 --name qe-app qe-automation-app:latest

# Test the running container
curl http://localhost:3000/

# Stop and remove container
docker stop qe-app
docker rm qe-app
```

---

## 🚀 Step 4: Push to Azure Container Registry (ACR)

**PowerShell:**
```powershell
# Login to Azure
az login

# Create or select resource group
az group create --name rg-qe-lab --location eastus

# Create Azure Container Registry
$ACR_NAME = "acrqe$(Get-Date -Format 'yyyyMMddHHmmss')"
az acr create `
    --name $ACR_NAME `
    --resource-group rg-qe-lab `
    --location eastus `
    --sku Basic

# Get ACR login server name
$ACR_LOGIN_SERVER = (az acr show --name $ACR_NAME --query loginServer -o tsv)
echo "ACR Login Server: $ACR_LOGIN_SERVER"

# Login to ACR
az acr login --name $ACR_NAME

# Tag image for ACR
docker tag qe-automation-app:latest $ACR_NAME.azurecr.io/qe-automation-app:v1.0.0

# Push image to ACR
docker push $ACR_NAME.azurecr.io/qe-automation-app:v1.0.0

# Verify image in ACR
az acr repository list --name $ACR_NAME --output table
az acr repository show-tags --name $ACR_NAME --repository qe-automation-app --output table
```

**Bash:**
```bash
# Login to Azure
az login

# Create or select resource group
az group create --name rg-qe-lab --location eastus

# Create Azure Container Registry
ACR_NAME=acrqe$(date +%s)
az acr create \
  --name $ACR_NAME \
  --resource-group rg-qe-lab \
  --location eastus \
  --sku Basic

# Get ACR login server name
ACR_LOGIN_SERVER=$(az acr show --name $ACR_NAME --query loginServer -o tsv)
echo "ACR Login Server: $ACR_LOGIN_SERVER"

# Login to ACR
az acr login --name $ACR_NAME

# Tag image for ACR
docker tag qe-automation-app:latest $ACR_NAME.azurecr.io/qe-automation-app:v1.0.0

# Push image to ACR
docker push $ACR_NAME.azurecr.io/qe-automation-app:v1.0.0

# Verify image in ACR
az acr repository list --name $ACR_NAME --output table
az acr repository show-tags --name $ACR_NAME --repository qe-automation-app --output table
```

---

## 🚀 Step 5: Deploy to Kubernetes (AKS)

### Create AKS Cluster

**PowerShell:**
```powershell
# Create AKS cluster
az aks create `
    --resource-group rg-qe-lab `
    --name aks-qe-lab `
    --node-count 2 `
    --node-vm-size Standard_D2s_v3 `
    --enable-addons monitoring `
    --generate-ssh-keys

# Get kubectl credentials
az aks get-credentials --resource-group rg-qe-lab --name aks-qe-lab

# Verify cluster connectivity
kubectl get nodes
kubectl get nodes -o wide
```

**Bash:**
```bash
# Create AKS cluster
az aks create \
  --resource-group rg-qe-lab \
  --name aks-qe-lab \
  --node-count 2 \
  --node-vm-size Standard_D2s_v3 \
  --enable-addons monitoring \
  --generate-ssh-keys

# Get kubectl credentials
az aks get-credentials --resource-group rg-qe-lab --name aks-qe-lab

# Verify cluster connectivity
kubectl get nodes
kubectl get nodes -o wide
```

### Deploy Application to Kubernetes

**File:** `k8s-manifests/deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: qe-automation-app
  labels:
    app: qe-automation-app
    environment: dev
spec:
  replicas: 2
  selector:
    matchLabels:
      app: qe-automation-app
  template:
    metadata:
      labels:
        app: qe-automation-app
    spec:
      containers:
      - name: qe-automation-app
        image: ${ACR_NAME}.azurecr.io/qe-automation-app:v1.0.0
        ports:
        - containerPort: 3000
        resources:
          requests:
            cpu: "100m"
            memory: "128Mi"
          limits:
            cpu: "200m"
            memory: "256Mi"
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 10
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 3000
          initialDelaySeconds: 5
          periodSeconds: 5
```

**File:** `k8s-manifests/service.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: qe-automation-service
  labels:
    app: qe-automation-app
spec:
  type: LoadBalancer
  selector:
    app: qe-automation-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 3000
```

**File:** `k8s-manifests/hpa.yaml`

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: qe-automation-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: qe-automation-app
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

### Deploy to Kubernetes

**PowerShell:**
```powershell
cd ai\sre-engineering\module-2-containers\k8s-manifests

# Apply all Kubernetes resources
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml

# Check deployment status
kubectl get deployments
kubectl get pods
kubectl get services

# Wait for external IP
kubectl get service qe-automation-service -w

# Once EXTERNAL-IP has an IP address, test the application
$EXTERNAL_IP = (kubectl get service qe-automation-service -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
curl http://$EXTERNAL_IP/
curl http://$EXTERNAL_IP/health
```

**Bash:**
```bash
cd ai/sre-engineering/module-2-containers/k8s-manifests

# Apply all Kubernetes resources
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml

# Check deployment status
kubectl get deployments
kubectl get pods
kubectl get services

# Wait for external IP
kubectl get service qe-automation-service -w

# Once EXTERNAL_IP has an IP address, test the application
EXTERNAL_IP=$(kubectl get service qe-automation-service -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
curl http://$EXTERNAL_IP/
curl http://$EXTERNAL_IP/health
```

---

## 🚀 Step 6: Helm Chart (Optional - Advanced)

**File:** `k8s-manifests/helm/qe-automation/Chart.yaml`

```yaml
apiVersion: v2
name: qe-automation
description: QE Automation Application Helm Chart
type: application
version: 1.0.0
appVersion: "1.0.0"
```

**File:** `k8s-manifests/helm/qe-automation/values.yaml`

```yaml
replicaCount: 2

image:
  repository: acrqe.azurecr.io/qe-automation-app
  pullPolicy: IfNotPresent
  tag: "v1.0.0"

service:
  type: LoadBalancer
  port: 80
  targetPort: 3000

resources:
  limits:
    cpu: 200m
    memory: 256Mi
  requests:
    cpu: 100m
    memory: 128Mi

autoscaling:
  enabled: true
  minReplicas: 2
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70
```

**Deploy with Helm:**

**PowerShell:**
```powershell
cd ai\sre-engineering\module-2-containers\k8s-manifests\helm

# Install Helm chart
helm install qe-automation ./qe-automation

# Check deployment
helm list
kubectl get pods

# Upgrade deployment
helm upgrade qe-automation ./qe-automation

# Uninstall
helm uninstall qe-automation
```

**Bash:**
```bash
cd ai/sre-engineering/module-2-containers/k8s-manifests/helm

# Install Helm chart
helm install qe-automation ./qe-automation

# Check deployment
helm list
kubectl get pods

# Upgrade deployment
helm upgrade qe-automation ./qe-automation

# Uninstall
helm uninstall qe-automation
```

---

## 🧪 Verification Checklist

- [ ] Docker image built successfully
- [ ] Docker image pushed to Azure Container Registry
- [ ] AKS cluster created successfully
- [ ] `kubectl get nodes` shows running nodes
- [ ] `kubectl get pods` shows running pods
- [ ] `kubectl get services` shows external IP
- [ ] Application responds to HTTP requests via external IP
- [ ] Health endpoint returns healthy status
- [ ] HPA is configured and visible
- [ ] Helm chart can deploy/upgrade/uninstall

---

## 🔗 Next Steps

Once Phase 2 is complete, proceed to **Module 3: Scaling & Autoscaling**.

**PowerShell:**
```powershell
cd ../module-3-scaling
Get-Content README.md
```

**Bash:**
```bash
cd ../module-3-scaling
cat README.md
```
