# Module 4: Monitoring & Observability (Azure Monitor, App Insights, Log Analytics)

> **Objective:** Learn to monitor, alert, and diagnose issues in cloud applications using Azure Monitor, Application Insights, and Log Analytics.

---

## 🎯 Learning Objectives

By completing this module, you will be able to:
- [ ] Create and configure Azure Monitor workspace
- [ ] Instrument applications with Application Insights
- [ ] Create custom dashboards with charts and metrics
- [ ] Create alert rules for critical metrics
- [ ] Query logs using KQL (Kusto Query Language)
- [ ] Set up diagnostic settings for resources
- [ ] Create action groups for notifications

---

## 📋 Theory: Observability Pillars

**Three Pillars of Observability:**
| Pillar | Purpose | Tools |
|--------|---------|-------|
| Metrics | Numeric data over time | Azure Monitor Metrics, Prometheus |
| Logs | Structured text events | Log Analytics, Application Insights |
| Traces | Request flow across services | Application Insights, OpenTelemetry |

**Additional:**
- **SLOs:** Service Level Objectives (availability, latency, error rate)
- **SLIs:** Service Level Indicators (measurable metrics)
- **Error Budgets:** Allowable downtime/errors

---

## 🛠️ Step 1: Create Azure Monitor Workspace

```bash
# Create Log Analytics workspace
az monitor log-analytics workspace create \
  --resource-group rg-qe-lab \
  --workspace-name law-qe-lab \
  --location eastus

# Get workspace ID
WORKSPACE_ID=$(az monitor log-analytics workspace show \
  --resource-group rg-qe-lab \
  --workspace-name law-qe-lab \
  --query customerId -otsv)
echo "Workspace ID: $WORKSPACE_ID"

# Get workspace key
WORKSPACE_KEY=$(az monitor log-analytics workspace get-shared-keys \
  --resource-group rg-qe-lab \
  --workspace-name law-qe-lab \
  --query primarySharedKey -otsv)
echo "Workspace Key: $WORKSPACE_KEY"
```

---

## 🚀 Step 2: Enable Application Insights

```bash
# Create Application Insights resource
az monitor app-insights component create \
  --app app-insights-qe-lab \
  --location eastus \
  --resource-group rg-qe-lab \
  --kind web

# Get instrumentation key
APP_INSIGHTS_KEY=$(az monitor app-insights component show \
  --app app-insights-qe-lab \
  --resource-group rg-qe-lab \
  --query instrumentationKey -otsv)
echo "Instrumentation Key: $APP_INSIGHTS_KEY"

# Get connection string
CONNECTION_STRING=$(az monitor app-insights component show \
  --app app-insights-qe-lab \
  --resource-group rg-qe-lab \
  --query connectionString -otsv)
echo "Connection String: $CONNECTION_STRING"
```

### Update Application with Application Insights

**File:** `module-2-containers/dockerfiles/node-app/app.js` (add instrumentation)

```javascript
const appInsights = require("applicationinsights");
appInsights.setup(process.env.APPLICATIONINSIGHTS_INSTRUMENTATIONKEY).start();

const appInsightsClient = appInsights.defaultClient;

app.use((req, res, next) => {
  appInsightsClient.trackRequest({
    name: req.method + ' ' + req.url,
    url: req.url,
    duration: 0,
    resultCode: 200,
    success: true
  });
  res.on('finish', () => {
    appInsightsClient.trackRequest({
      name: req.method + ' ' + req.url,
      url: req.url,
      duration: res.getHeader('X-Response-Time') || 0,
      resultCode: res.statusCode,
      success: res.statusCode < 400
    });
  });
  next();
});

app.use((req, res, next) => {
  const start = Date.now();
  res.setHeader('X-Response-Time', Date.now() - start);
  next();
});
```

Rebuild and deploy:
```bash
docker build -t $ACR_NAME.azurecr.io/qe-automation-app:v2.0.0 .
docker push $ACR_NAME.azurecr.io/qe-automation-app:v2.0.0

kubectl set image deployment/qe-automation-app qe-automation-app=$ACR_NAME.azurecr.io/qe-automation-app:v2.0.0
```

---

## 📊 Step 3: Create Custom Dashboard

**File:** `dashboards/qe-dashboard.json`

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "workspaceName": {
      "type": "string",
      "defaultValue": "law-qe-lab"
    },
    "appInsightsName": {
      "type": "string",
      "defaultValue": "app-insights-qe-lab"
    }
  },
  "resources": [
    {
      "type": "Microsoft.Insights/dashboards",
      "apiVersion": "2021-04-01",
      "name": "qe-dashboard",
      "location": "[resourceGroup().location]",
      "properties": {
        "lenses": {
          "0": {
            "order": 0,
            "parts": [
              {
                "position": {
                  "x": 0,
                  "y": 0,
                  "rowSpan": 3,
                  "colSpan": 4
                },
                "content": {
                  "metadata": {
                    "inputs": [],
                    "type": "Extension",
                    "settings": {}
                  },
                  "properties": {
                    "title": "Request Rate",
                    "query": "requests | summarize count() by bin(timestamp, 1m)",
                    "size": 1,
                    "type": "timechart",
                    "queryType": "1",
                    "resourceId": "/subscriptions/$(az account show --query id -otsv)/resourceGroups/rg-qe-lab/providers/microsoft.insights/components/app-insights-qe-lab"
                  }
                }
              }
            ]
          }
        }
      }
    }
  ]
}
```

**Deploy Dashboard:**

```bash
# Deploy dashboard via Azure CLI
az deployment group create \
  --resource-group rg-qe-lab \
  --template-file ai/sre-engineering/module-4-monitoring/dashboards/qe-dashboard.json \
  --parameters workspaceName=law-qe-lab appInsightsName=app-insights-qe-lab

# View dashboard in Azure Portal
# Navigate to: Monitor -> Dashboards -> qe-dashboard
```

---

## 🚨 Step 4: Create Alert Rules

**File:** `alert-rules/alert-rules.json`

```json
[
  {
    "name": "alert-high-cpu",
    "description": "Alert when CPU usage exceeds 80%",
    "severity": 2,
    "condition": {
      "name": "High CPU",
      "metricName": "Percentage CPU",
      "operator": "GreaterThan",
      "threshold": 80,
      "timeAggregation": "Average",
      "windowSize": "PT5M"
    },
    "actionGroup": "/subscriptions/{subscription-id}/resourceGroups/rg-qe-lab/providers/microsoft.insights/actionGroups/alert-action-group"
  },
  {
    "name": "alert-high-response-time",
    "description": "Alert when response time exceeds 2 seconds",
    "severity": 2,
    "condition": {
      "name": "High Response Time",
      "metricName": "requests/duration",
      "operator": "GreaterThan",
      "threshold": 2000,
      "timeAggregation": "Average",
      "windowSize": "PT5M"
    },
    "actionGroup": "/subscriptions/{subscription-id}/resourceGroups/rg-qe-lab/providers/microsoft.insights/actionGroups/alert-action-group"
  },
  {
    "name": "alert-error-rate",
    "description": "Alert when error rate exceeds 5%",
    "severity": 1,
    "condition": {
      "name": "Error Rate",
      "metricName": "requests/failed",
      "operator": "GreaterThan",
      "threshold": 5,
      "timeAggregation": "Count",
      "windowSize": "PT5M"
    },
    "actionGroup": "/subscriptions/{subscription-id}/resourceGroups/rg-qe-lab/providers/microsoft.insights/actionGroups/alert-action-group"
  }
]
```

**Create Alert Rules:**

```bash
# Create Action Group for email notifications
az monitor action-group create \
  --resource-group rg-qe-lab \
  --name alert-action-group \
  --short-name qe-alerts

# Add email action
az monitor action-group email create \
  --resource-group rg-qe-lab \
  --action-group alert-action-group \
  --name QE-Team-Email \
  --to admin@yourcompany.com

# Create alert rule
az monitor alert rule create \
  --resource-group rg-qe-lab \
  --name alert-high-cpu \
  --action alert-action-group \
  --condition "Percentage CPU > 80 avg 5m" \
  --description "Alert when CPU usage exceeds 80%"

# List alert rules
az monitor alert rule list --resource-group rg-qe-lab --output table
```

---

## 📊 Step 5: KQL Queries for Analysis

**Save as:** `kql-queries.txt`

```kusto
// Request rate over time
requests
| summarize RequestCount = count() by bin(timestamp, 1m)
| render timechart

// Failed requests by operation name
requests
| where resultCode >= 400
| summarize FailedCount = count() by name, resultCode
| order by FailedCount desc

// Slow requests (over 2 seconds)
requests
| where duration > 2000
| project timestamp, name, duration, resultCode
| order by duration desc

// Top slow endpoints
requests
| summarize AvgDuration = avg(duration), MaxDuration = max(duration), Count = count() by name
| order by AvgDuration desc

// Server errors
requests
| where resultCode between (500 .. 599)
| summarize Count = count() by name, resultCode, cloud_RoleName
| order by Count desc

// Dependency failures
dependencies
| where success == false
| project timestamp, name, type, resultCode, duration
| order by duration desc

// CPU usage by container
ContainerInsights
| where ContainerName == "qe-automation-app"
| summarize AvgCPU = avg(ContainerCpuUtilizationPercentage) by bin(TimeGenerated, 5m)
| render timechart

// Memory usage
ContainerInsights
| where ContainerName == "qe-automation-app"
| summarize AvgMemory = avg(ContainerMemoryRssPercentage) by bin(TimeGenerated, 5m)
| render timechart
```

**Run KQL Queries:**

```bash
# Query via Azure CLI
az monitor log-analytics query \
  --resource-group rg-qe-lab \
  --workspace law-qe-lab \
  --analytics-query 'requests | summarize count() by bin(timestamp, 1m) | render timechart' \
  --timespan PT1H \
  --output table
```

---

## 🧪 Verification Checklist

- [ ] Azure Monitor workspace created
- [ ] Application Insights created and instrumenting app
- [ ] Dashboard created with at least 2 charts
- [ ] Alert rules created for CPU, response time, errors
- [ ] Alert actions configured (email notification)
- [ ] KQL queries return results
- [ ] Alerts trigger when thresholds exceeded

---

## 🔗 Next Steps

Once Phase 4 is complete, proceed to **Module 5: Load Testing** to learn how to stress test your application with Azure Load Testing and Locust.

```bash
cd ../module-5-load-testing && cat README.md
```
