# Module 3: Scaling & Autoscaling (HPA, KEDA, Azure App Service)

> **Objective:** Learn to automatically scale applications based on demand using Horizontal Pod Autoscaler (HPA), Kubernetes Event-driven Autoscaling (KEDA), and Azure App Service auto-scaling.

---

## 🎯 Learning Objectives

By completing this module, you will be able to:

- [ ] Configure Horizontal Pod Autoscaler (HPA) in Kubernetes
- [ ] Configure KEDA for event-driven scaling
- [ ] Configure Azure App Service auto-scaling
- [ ] Understand CPU, memory, and custom metric scaling
- [ ] Test auto-scaling under load
- [ ] Understand scale-down behavior and cool-down periods

---

## 📋 Theory: Scaling Strategies

**Scaling Types:**

| Type | Description |
|------|-------------|
| Vertical Scaling | Increase resources (CPU/RAM) of existing instances |
| Horizontal Scaling | Add more instances (pods/instances) |
| Cluster Autoscaling | Add more nodes to the cluster |

**Scaling Triggers:**
- CPU utilization
- Memory utilization
- Custom metrics (queue length, HTTP requests)
- Scheduled scaling (cron-based)
- External metrics (Prometheus, Datadog)

---

## 🛠️ Step 1: Horizontal Pod Autoscaler (HPA)

**File:** `hpa-configs/hpa-basic.yaml`

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: qe-automation-hpa
  namespace: default
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
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
      - type: Percent
        value: 100
        periodSeconds: 15
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 10
        periodSeconds: 60
```

### Apply HPA

**PowerShell:**
```powershell
cd ai\sre-engineering\module-3-scaling\hpa-configs

# Apply HPA configuration
kubectl apply -f hpa-basic.yaml

# Check HPA status
kubectl get hpa
kubectl get hpa qe-automation-hpa -o yaml

# Watch HPA changes
kubectl get hpa qe-automation-hpa -w
```

**Bash:**
```bash
cd ai/sre-engineering/module-3-scaling/hpa-configs

# Apply HPA configuration
kubectl apply -f hpa-basic.yaml

# Check HPA status
kubectl get hpa
kubectl get hpa qe-automation-hpa -o yaml

# Watch HPA changes
kubectl get hpa qe-automation-hpa -w
```

### Test HPA with Load

**PowerShell:**
```powershell
# Get service IP
$EXTERNAL_IP = (kubectl get service qe-automation-service -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
Write-Host "External IP: $EXTERNAL_IP"

# Generate load using curl in a loop
1..100 | ForEach-Object {
  curl -s "http://$EXTERNAL_IP/" > $null
}

# Wait for HPA to scale up
Write-Host "Waiting for HPA to scale up..."
kubectl get hpa qe-automation-hpa -w

# Check pod count
kubectl get pods -l app=qe-automation-app

# Stop load and watch scale down
Write-Host "Stopping load - watching scale down..."
kubectl get hpa qe-automation-hpa -w
kubectl get pods -l app=qe-automation-app
```

**Bash:**
```bash
# Get service IP
EXTERNAL_IP=$(kubectl get service qe-automation-service -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
echo "External IP: $EXTERNAL_IP"

# Generate load using curl in a loop
for i in {1..100}; do
  curl -s "http://$EXTERNAL_IP/" > /dev/null &
done
wait

# Watch HPA scale up
kubectl get hpa qe-automation-hpa -w

# Check pod count
kubectl get pods -l app=qe-automation-app

# Stop load and watch scale down
kubectl get hpa qe-automation-hpa -w
kubectl get pods -l app=qe-automation-app
```

---

## 🚀 Step 2: KEDA (Kubernetes Event-driven Autoscaling)

**File:** `keda-configs/keda-scaledobject.yaml`

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: qe-api-scaler
  namespace: default
spec:
  scaleTargetRef:
    name: qe-automation-app
  minReplicaCount: 1
  maxReplicaCount: 20
  cooldownPeriod: 300
  pollingInterval: 30
  triggers:
  - type: cpu
    metricType: Utilization
    metadata:
      value: "70"
  - type: external
    metadata:
      serverAddress: https://your-azure-monitor.azure.com
      apiVersion: 2021-05-01-preview
      metricNamespace: microsoft.insights/components
      metricName: requests/duration
      dimension: '{"role":"qe-automation-app"}'
      threshold: '2000'
      operator: GreaterThan
```

### Install KEDA

**PowerShell:**
```powershell
# Add KEDA Helm repository
helm repo add kedacore https://kedacore.github.io/charts
helm repo update

# Install KEDA
helm install kedacore kedacore/keda --namespace keda --create-namespace

# Verify KEDA installation
kubectl get pods -n keda
kubectl get crds | grep keda

# Apply ScaledObject
kubectl apply -f keda-configs/keda-scaledobject.yaml

# Verify ScaledObject
kubectl get scaledobject
kubectl get scaledobject qe-api-scaler -o yaml
```

**Bash:**
```bash
# Add KEDA Helm repository
helm repo add kedacore https://kedacore.github.io/charts
helm repo update

# Install KEDA
helm install kedacore kedacore/keda --namespace keda --create-namespace

# Verify KEDA installation
kubectl get pods -n keda
kubectl get crds | grep keda

# Apply ScaledObject
kubectl apply -f keda-configs/keda-scaledobject.yaml

# Verify ScaledObject
kubectl get scaledobject
kubectl get scaledobject qe-api-scaler -o yaml
```

---

## 🚀 Step 3: Azure App Service Auto-Scaling

**PowerShell:**
```powershell
# Create App Service Plan
az appservice plan create `
    --name asp-qe-lab `
    --resource-group rg-qe-lab `
    --sku S1 `
    --number-of-workers 1 `
    --location eastus

# Create Web App
$APP_NAME = "qe-app-$(Get-Date -Format 'yyyyMMddHHmmss')"
az webapp create `
    --resource-group rg-qe-lab `
    --plan asp-qe-lab `
    --name $APP_NAME `
    --runtime "NODE|18-lts"

# Configure auto-scale rules
az monitor autoscale create `
    --resource-group rg-qe-lab `
    --resource "/subscriptions/$(az account show --query id -otsv)/resourceGroups/rg-qe-lab/providers/Microsoft.Web/serverfarms/asp-qe-lab" `
    --name autoscale-qe-app `
    --min 2 `
    --max 10 `
    --count 2

# Add CPU-based scale rule
az monitor autoscale rule create `
    --resource-group rg-qe-lab `
    --autoscale-name autoscale-qe-app `
    --condition "Percentage CPU > 70 avg 5m" `
    --scale out 1 `
    --cooldown 5 `
    --time-grain 1m `
    --time-window 5m

# Add scale-in rule
az monitor autoscale rule create `
    --resource-group rg-qe-lab `
    --autoscale-name autoscale-qe-app `
    --condition "Percentage CPU < 30 avg 5m" `
    --scale in 1 `
    --cooldown 5 `
    --time-grain 1m `
    --time-window 5m

# Verify autoscale configuration
az monitor autoscale show --resource-group rg-qe-lab --name autoscale-qe-app --output table
```

**Bash:**
```bash
# Create App Service Plan
az appservice plan create \
  --name asp-qe-lab \
  --resource-group rg-qe-lab \
  --sku S1 \
  --number-of-workers 1 \
  --location eastus

# Create Web App
APP_NAME="qe-app-$(date +%s)"
az webapp create \
  --resource-group rg-qe-lab \
  --plan asp-qe-lab \
  --name $APP_NAME \
  --runtime "NODE|18-lts"

# Configure auto-scale rules
az monitor autoscale create \
  --resource-group rg-qe-lab \
  --resource /subscriptions/$(az account show --query id -otsv)/resourceGroups/rg-qe-lab/providers/Microsoft.Web/serverfarms/asp-qe-lab \
  --name autoscale-qe-app \
  --min 2 \
  --max 10 \
  --count 2

# Add CPU-based scale rule
az monitor autoscale rule create \
  --resource-group rg-qe-lab \
  --autoscale-name autoscale-qe-app \
  --condition "Percentage CPU > 70 avg 5m" \
  --scale out 1 \
  --cooldown 5 \
  --time-grain 1m \
  --time-window 5m

# Add scale-in rule
az monitor autoscale rule create \
  --resource-group rg-qe-lab \
  --autoscale-name autoscale-qe-app \
  --condition "Percentage CPU < 30 avg 5m" \
  --scale in 1 \
  --cooldown 5 \
  --time-grain 1m \
  --time-window 5m

# Verify autoscale configuration
az monitor autoscale show --resource-group rg-qe-lab --name autoscale-qe-app --output table
```

---

## 🚀 Step 4: Test Auto-scaling Under Load

**PowerShell:**
```powershell
# Get Application URL
$WEBAPP_URL = (az webapp show --resource-group rg-qe-lab --name qe-app-$(az webapp list --resource-group rg-qe-lab --query "[0].name" -o tsv) --query defaultHostName -otsv)
Write-Host "Web App URL: https://$WEBAPP_URL"

# Generate load using curl in parallel
1..200 | ForEach-Object {
  curl -s "https://$WEBAPP_URL/" > $null
}
Wait-Event -Timeout 60

# Monitor scaling
az monitor autoscale show --resource-group rg-qe-lab --name autoscale-qe-app --output table

# Check instance count
az webapp list-instances --resource-group rg-qe-lab --name qe-app-$(az webapp list --resource-group rg-qe-lab --query "[0].name" -o tsv) --output table
```

**Bash:**
```bash
# Get Application URL
WEBAPP_URL=$(az webapp show --resource-group rg-qe-lab --name qe-app-$(date +%s) --query defaultHostName -o tsv)
echo "Web App URL: https://$WEBAPP_URL"

# Generate load using curl in parallel
for i in {1..200}; do
  curl -s "https://$WEBAPP_URL/" > /dev/null &
done
wait

# Monitor scaling
az monitor autoscale show --resource-group rg-qe-lab --name autoscale-qe-app --output table

# Check instance count
az webapp list-instances --resource-group rg-qe-lab --name qe-app-$(az webapp list --resource-group rg-qe-lab --query "[0].name" -o tsv) --output table
```

---

## 🧪 Verification Checklist

- [ ] Horizontal Pod Autoscaler (HPA) configured
- [ ] HPA scales up under load
- [ ] HPA scales down after load decreases
- [ ] KEDA installed and ScaledObject configured
- [ ] Azure App Service autoscale rules configured
- [ ] Auto-scaling verified with load test
- [ ] Scale-down cooldown working properly

---

## 🔗 Next Steps

Once Phase 3 is complete, proceed to **Module 4: Monitoring & Observability**.

**PowerShell:**
```powershell
cd ../module-4-monitoring
Get-Content README.md
```

**Bash:**
```bash
cd ../module-4-monitoring
cat README.md
```
