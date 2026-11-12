# Module 5: Load Testing (Azure Load Testing, Locust, JMeter)

> **Objective:** Learn to perform load testing using Azure Load Testing, REST Assured, and Playwright to validate application performance under load.

---

## 🎯 Learning Objectives

By completing this module, you will be able to:

- [ ] Create and configure Azure Load Testing resource
- [ ] Create and run load tests with JMeter scripts
- [ ] Create and run load tests with Locust Python scripts
- [ ] Analyze load test results (response times, error rates, throughput)
- [ ] Identify performance bottlenecks
- [ ] Integrate load testing into CI/CD pipelines

---

## 📋 Theory: Load Testing Types

| Test Type | Purpose | When to Run |
|-----------|---------|-------------|
| Load Test | Assess system behavior under expected load | Before release |
| Stress Test | Find breaking point | Before major release |
| Spike Test | Verify recovery from sudden load | Before production |
| Soak Test | Verify stability over extended time | Before production |
| Smoke Test | Verify basic functionality | Every CI run |

**Key Metrics:**
- **Response Time:** Time to complete a request
- **Throughput:** Requests per second
- **Error Rate:** Percentage of failed requests
- **Concurrent Users:** Number of simultaneous users
- **95th Percentile:** Time below which 95% of requests complete

---

## 🛠️ Step 1: Create Azure Load Testing Resource

**PowerShell:**
```powershell
# Create Azure Load Testing resource
az load create `
    --name alt-qe-lab `
    --resource-group rg-qe-lab `
    --location eastus

# Verify creation
az load show --name alt-qe-lab --resource-group rg-qe-lab --output table

# Get Load Testing URL
$ALT_URL = (az load show --name alt-qe-lab --resource-group rg-qe-lab --query properties.uri -otsv)
Write-Host "Azure Load Testing URL: $ALT_URL"
```

**Bash:**
```bash
# Create Azure Load Testing resource
az load create \
  --name alt-qe-lab \
  --resource-group rg-qe-lab \
  --location eastus

# Verify creation
az load show --name alt-qe-lab --resource-group rg-qe-lab --output table

# Get Load Testing URL
ALT_URL=$(az load show --name alt-qe-lab --resource-group rg-qe-lab --query properties.uri -otsv)
echo "Azure Load Testing URL: $ALT_URL"
```

---

## 🚀 Step 2: Create JMeter Test Plan

**File:** `jmeter-tests/load-test.jmx`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jmeterTestPlan version="1.2" properties="5.0" jmeter="5.4.1">
  <hashTree>
    <TestPlan guiclass="TestPlanGui" testclass="TestPlan" testname="QE Load Test" enabled="true">
      <stringProp name="TestPlan.comments"></stringProp>
      <boolProp name="TestPlan.serialize_threadgroups">false</boolProp>
      <elementProp name="TestPlan.user_defined_variables" elementType="Arguments" guiclass="ArgumentsPanel" testclass="Arguments" testname="User Defined Variables">
        <collectionProp name="Arguments.arguments">
          <elementProp name="BASE_URL" elementType="Argument">
            <stringProp name="Argument.name">BASE_URL</stringProp>
            <stringProp name="Argument.value">https://your-webapp.azurewebsites.net</stringProp>
            <stringProp name="Argument.metadata">=</stringProp>
          </elementProp>
        </collectionProp>
      </elementProp>
    </elementProp>
    <hashTree>
      <ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="HTTP Users" enabled="true">
        <stringProp name="ThreadGroup.num_threads">50</stringProp>
        <stringProp name="ThreadGroup.ramp_time">60</stringProp>
        <longProp name="ThreadGroup.start_time">1</longProp>
        <stringProp name="ThreadGroup.duration">300</stringProp>
        <stringProp name="ThreadGroup.delay">0</stringProp>
        <boolProp name="ThreadGroup.scheduler">true</boolProp>
        <elementProp name="ThreadGroup.main_controller" elementType="LoopController" guiclass="LoopControlPanel" testclass="LoopController" testname="Loop Controller" enabled="true">
          <boolProp name="LoopController.continue_forever">false</boolProp>
          <stringProp name="LoopController.loops">-1</stringProp>
        </elementProp>
        <elementProp name="ThreadGroup.header_manager" elementType="HeaderManager" guiclass="HeaderManager" testclass="HeaderManager" testname="HTTP Header Manager" enabled="true">
          <collectionProp name="HeaderManager.header">
            <elementProp name="Header" elementType="Header">
              <stringProp name="Header.name">Content-Type</stringProp>
              <stringProp name="Header.value">application/json</stringProp>
            </elementProp>
          </collectionProp>
        </elementProp>
        <hashTree>
          <HTTPSamplerProxy guiclass="HttpSampleGui" testclass="HTTPSamplerProxy" testname="GET Homepage" enabled="true">
            <stringProp name="HTTPSampler.domain">${BASE_URL}</stringProp>
            <stringProp name="HTTPSampler.port"></stringProp>
            <stringProp name="HTTPSampler.protocol">https</stringProp>
            <stringProp name="HTTPSampler.method">GET</stringProp>
            <stringProp name="HTTPSampler.path">/</stringProp>
            <stringProp name="HTTPSampler.contentType"></stringProp>
            <stringProp name="HTTPSampler.query"></stringProp>
            <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
            <stringProp name="HTTPSampler.connect_timeout"></stringProp>
            <stringProp name="HTTPSampler.response_timeout"></stringProp>
            <elementProp name="HTTPsampler.Arguments" elementType="Arguments">
              <collectionProp name="Arguments.arguments"/>
            </elementProp>
            <elementProp name="HTTPsampler.HeaderManager" elementType="HeaderManager" testclass="HeaderManager" testname="HTTP Header Manager" enabled="true">
              <collectionProp name="HeaderManager.header">
                <elementProp name="Header" elementType="Header">
                  <stringProp name="Header.name">Content-Type</stringProp>
                  <stringProp name="Header.value">application/json</stringProp>
                </elementProp>
              </collectionProp>
            </elementProp>
          </hashTree>
        </elementProp>
        <HTTPSamplerProxy guiclass="HttpSampleGui" testclass="HTTPSamplerProxy" testname="GET Health" enabled="true">
          <stringProp name="HTTPSampler.domain">${BASE_URL}</stringProp>
          <stringProp name="HTTPSampler.port"></stringProp>
          <stringProp name="HTTPSampler.protocol">https</stringProp>
          <stringProp name="HTTPSampler.method">GET</stringProp>
          <stringProp name="HTTPSampler.path">/health</stringProp>
          <stringProp name="HTTPSampler.contentType"></stringProp>
          <stringProp name="HTTPSampler.query"></stringProp>
          <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          <stringProp name="HTTPSampler.connect_timeout"></stringProp>
          <stringProp name="HTTPSampler.response_timeout"></stringProp>
          <elementProp name="HTTPsampler.Arguments" elementType="Arguments">
            <collectionProp name="Arguments.arguments"/>
          </elementProp>
          <elementProp name="HTTPsampler.HeaderManager" elementType="HeaderManager" testclass="HeaderManager" testname="HTTP Header Manager" enabled="true">
            <collectionProp name="HeaderManager.header">
              <elementProp name="Header" elementType="Header">
                <stringProp name="Header.name">Content-Type</stringProp>
                <stringProp name="Header.value">application/json</stringProp>
              </elementProp>
            </collectionProp>
          </elementProp>
          <hashTree/>
        </elementProp>
      </hashTree>
      <ResultCollector guiclass="ViewResultsFullVisualizer" testclass="ResultCollector" testname="View Results Tree" enabled="false">
        <stringProp name="ResultCollector.error_logging">
          <value>
          </value>
        </stringProp>
        <objProp>
          <name>saveResults</name>
          <value class="SampleSaveConfiguration">
            <time>true</value>
            <latency>true</value>
            <timestamp>true</value>
            <connectTime>true</value>
            <code>true</value>
            <message>true</value>
            <threadName>true</value>
            <dataType>true</value>
            <assertions>true</value>
            <subresults>true</value>
            <samplerData>true</value>
            <responseHeaders>false</value>
            <requestHeaders>true</value>
            <responseData>false</value>
            <requestHeaders>true</value>
            <samplerData>true</value>
          </value>
        </objProp>
        <stringProp name="filename"></stringProp>
      </stringProp>
      <hashTree/>
      <SummaryReport guiclass="SummaryReport" testclass="ResultCollector" testname="Summary Report" enabled="true">
        <stringProp name="ResultCollector.error_logging">
          <value>
          </value>
        </stringProp>
        <objProp>
          <name>saveResults</name>
          <value class="SampleSaveConfiguration">
            <time>true</value>
            <latency>true</value>
            <timestamp>true</value>
            <connectTime>true</value>
            <code>true</value>
            <message>true</value>
            <threadName>true</value>
            <dataType>true</value>
            <assertions>true</value>
            <subresults>true</value>
            <samplerData>true</value>
            <responseHeaders>true</value>
            <requestHeaders>true</value>
            <responseData>false</value>
            <requestHeaders>true</value>
            <samplerData>true</value>
          </value>
        </objProp>
        <stringProp name="filename"></stringProp>
      </stringProp>
      <hashTree/>
      <AggregateReport guiclass="AggregateReport" testclass="ResultCollector" testname="Aggregate Report" enabled="true">
        <stringProp name="ResultCollector.error_logging">
          <value>
          </value>
        </stringProp>
        <objProp>
          <name>saveResults</name>
          <value class="SampleSaveConfiguration">
            <time>true</value>
            <latency>true</value>
            <timestamp>true</value>
            <connectTime>true</value>
            <code>true</value>
            <message>true</value>
            <threadName>true</value>
            <dataType>true</value>
            <assertions>true</value>
            <subresults>true</value>
            <samplerData>true</value>
            <responseHeaders>true</value>
            <requestHeaders>true</value>
            <responseData>false</value>
            <requestHeaders>true</value>
            <samplerData>true</value>
          </value>
        </objProp>
        <stringProp name="filename"></stringProp>
      </stringProp>
      <hashTree/>
    </hashTree>
  </hashTree>
</jmeterTestPlan>
```

---

## 🚀 Step 3: Create Locust Test

**File:** `locust-tests/locustfile.py`

```python
from locust import HttpUser, task, between

class QEApiUser(HttpUser):
    wait_time = between(1, 2)

    @task(2)
    def get_homepage(self):
        self.client.get("/")

    @task(1)
    def get_health(self):
        self.client.get("/health")

    @task(1)
    def get_ready(self):
        self.client.get("/ready")

    @task(1)
    def post_data(self):
        self.client.post("/api/data", json={"key": "value"})
```

**Run Locust Locally:**

**PowerShell:**
```powershell
# Install Locust
pip install locust

# Run Locust test
locust -f locustfile.py --headless -u 50 -r 5 --run-time 1m --host https://your-webapp.azurewebsites.net

# Run Locust with web UI
locust -f locustfile.py --host https://your-webapp.azurewebsites.net
# Open http://localhost:8089 in browser
```

**Bash:**
```bash
# Install Locust
pip install locust

# Run Locust test
locust -f locustfile.py --headless -u 50 -r 5 --run-time 1m --host https://your-webapp.azurewebsites.net

# Run Locust with web UI
locust -f locustfile.py --host https://your-webapp.azurewebsites.net
# Open http://localhost:8089 in browser
```

---

## 🚀 Step 4: Create Azure Load Testing Resource

**PowerShell:**
```powershell
# Create Azure Load Testing resource
az load create `
    --name alt-qe-lab `
    --resource-group rg-qe-lab `
    --location eastus

# Verify creation
az load show --name alt-qe-lab --resource-group rg-qe-lab --output table

# Get Load Testing URL
$ALT_URL = (az load show --name alt-qe-lab --resource-group rg-qe-lab --query properties.uri -otsv)
Write-Host "Azure Load Testing URL: $ALT_URL"
```

**Bash:**
```bash
# Create Azure Load Testing resource
az load create \
  --name alt-qe-lab \
  --resource-group rg-qe-lab \
  --location eastus

# Verify creation
az load show --name alt-qe-lab --resource-group rg-qe-lab --output table

# Get Load Testing URL
ALT_URL=$(az load show --name alt-qe-lab --resource-group rg-qe-lab --query properties.uri -otsv)
echo "Azure Load Testing URL: $ALT_URL"
```

---

## 🚀 Step 5: Upload and Run JMeter Test via Azure Load Testing

**PowerShell:**
```powershell
# Upload JMeter test to Azure Load Testing
az load test create `
    --resource-group rg-qe-lab `
    --name load-test-qe `
    --test-type jmeter `
    --test-configuration @ai/sre-engineering/module-5-load-testing/jmeter-tests/load-test.jmx `
    --display-name "QE Load Test - JMeter" `
    --description "Load test for QE automation app"

# Run the load test
az load test-run create `
    --resource-group rg-qe-lab `
    --name load-test-run-1 `
    --test-name load-test-qe `
    --display-name "First Load Test Run" `
    --description "Initial load test for QE application" `
    --vuser-count 50 `
    --duration 300

# Check test run status
az load test-run show --resource-group rg-qe-lab --name load-test-run-1 --output table

# Wait for test completion
while ($true) {
    $status = (az load test-run show --resource-group rg-qe-lab --name load-test-run-1 --query status -otsv)
    Write-Host "Status: $status"
    if ($status -eq "Completed") { break }
    Start-Sleep -Seconds 30
}

# Get test results
az load test-run show --resource-group rg-qe-lab --name load-test-run-1 --output json
```

**Bash:**
```bash
# Upload JMeter test to Azure Load Testing
az load test create \
  --resource-group rg-qe-lab \
  --name load-test-qe \
  --test-type jmeter \
  --test-configuration ai/sre-engineering/module-5-load-testing/jmeter-tests/load-test.jmx \
  --display-name "QE Load Test - JMeter" \
  --description "Load test for QE automation app"

# Run the load test
az load test-run create \
  --resource-group rg-qe-lab \
  --name load-test-run-1 \
  --test-name load-test-qe \
  --display-name "First Load Test Run" \
  --description "Initial load test for QE application" \
  --vuser-count 50 \
  --duration 300

# Check test run status
az load test-run show --resource-group rg-qe-lab --name load-test-run-1 --output table

# Wait for test completion
while true; do
  STATUS=$(az load test-run show --resource-group rg-qe-lab --name load-test-run-1 --query status -otsv)
  echo "Status: $STATUS"
  if [ "$STATUS" == "Completed" ]; then
    break
  fi
  sleep 30
done

# Get test results
az load test-run show --resource-group rg-qe-lab --name load-test-run-1 --output json
```

---

## 🧪 Verification Checklist

- [ ] Azure Load Testing resource created
- [ ] JMeter test plan created and uploaded
- [ ] Locust test created and run locally
- [ ] Azure Load Testing test run completed
- [ ] Test results show response times, error rates
- [ ] Identified performance bottlenecks
- [ ] Load test integrated into CI/CD pipelines

---

## 🔗 Next Steps

Once Phase 5 is complete, proceed to **Module 6: AI for SRE** to learn about anomaly detection and automated remediation.

**PowerShell:**
```powershell
cd ../module-6-ai-sre
Get-Content README.md
```

**Bash:**
```bash
cd ../module-6-ai-sre
cat README.md
```
