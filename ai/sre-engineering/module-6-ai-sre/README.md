# Module 6: AI for SRE (AIOps) - Anomaly Detection & Automated Remediation

> **Objective:** Learn to implement AI-driven operations for anomaly detection, automated remediation, and predictive scaling using Python, Azure AI, and ML.

---

## 🎯 Learning Objectives

By completing this module, you will be able to:

- [ ] Implement anomaly detection using statistical methods
- [ ] Train and deploy ML models for anomaly detection
- [ ] Integrate Azure Monitor with Python for automated alerting
- [ ] Build automated remediation workflows
- [ ] Implement self-healing infrastructure patterns
- [ ] Use Azure AI for predictive scaling

---

## 📋 Theory: AIOps

**AIOps Components:**

| Component | Purpose | Tools |
|-----------|---------|-------|
| Anomaly Detection | Detect unusual patterns | Isolation Forest, Z-Score, LSTM |
| Root Cause Analysis | Identify failure sources | Dependency mapping, correlation |
| Automated Remediation | Fix issues automatically | Runbooks, Azure Functions |
| Predictive Analytics | Forecast capacity needs | Time series forecasting |

**Benefits:**
- Faster MTTR (Mean Time to Resolution)
- Reduced alert fatigue
- Proactive issue prevention
- Reduced manual toil

---

## 🛠️ Step 1: Anomaly Detection with Python

**File:** `anomaly-detection/anomaly_detector.py`

```python
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
from datetime import datetime, timedelta

class AnomalyDetector:
    def __init__(self, contamination=0.1):
        self.model = IsolationForest(
            contamination=contamination,
            random_state=42,
            n_estimators=100
        )
        self.scaler = None
        self.feature_columns = None

    def prepare_features(self, df):
        """Extract features from time series data"""
        df = df.copy()
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values('timestamp')

        # Rolling statistics
        df['cpu_rolling_mean'] = df['cpu_percent'].rolling(window=10, min_periods=1).mean()
        df['cpu_rolling_std'] = df['cpu_percent'].rolling(window=10, min_periods=1).std()
        df['cpu_pct_change'] = df['cpu_percent'].pct_change()

        df['mem_rolling_mean'] = df['memory_percent'].rolling(window=10, min_periods=1).mean()
        df['mem_rolling_std'] = df['memory_percent'].rolling(window=10, min_periods=1).std()

        # Time features
        df['hour'] = df['timestamp'].dt.hour
        df['day_of_week'] = df['timestamp'].dt.dayofweek

        self.feature_columns = [
            'cpu_percent', 'cpu_rolling_mean', 'cpu_rolling_std', 'cpu_pct_change',
            'memory_percent', 'mem_rolling_mean', 'mem_rolling_std',
            'hour', 'day_of_week'
        ]

        return df[self.feature_columns].fillna(0)

    def train(self, df):
        """Train the anomaly detection model"""
        features = self.prepare_features(df)
        self.model.fit(features)
        print(f"Model trained on {len(features)} samples")
        return self

    def predict(self, df):
        """Predict anomalies in new data"""
        if self.model is None:
            raise ValueError("Model not trained. Call train() first.")

        features = self.prepare_features(df)
        predictions = self.model.predict(features)
        scores = self.model.decision_function(features)

        df = df.copy()
        df['is_anomaly'] = predictions == -1
        df['anomaly_score'] = scores

        return df

    def save(self, path):
        """Save model to disk"""
        joblib.dump({
            'model': self.model,
            'feature_columns': self.feature_columns
        }, path)
        print(f"Model saved to {path}")

    @classmethod
    def load(cls, path):
        """Load model from disk"""
        data = joblib.load(path)
        detector = cls()
        detector.model = data['model']
        detector.feature_columns = data['feature_columns']
        return detector


# Example usage
if __name__ == "__main__":
    # Generate synthetic data
    np.random.seed(42)
    n_samples = 1000

    # Normal data
    normal_data = pd.DataFrame({
        'timestamp': pd.date_range('2024-01-01', periods=n_samples, freq='5T'),
        'cpu_percent': np.random.normal(50, 10, n_samples),
        'memory_percent': np.random.normal(60, 15, n_samples)
    })

    # Inject anomalies
    anomaly_indices = np.random.choice(n_samples, size=20, replace=False)
    normal_data.loc[anomaly_indices, 'cpu_percent'] = np.random.uniform(90, 100, 20)

    # Train and predict
    detector = AnomalyDetector()
    detector.train(normal_data)

    results = detector.predict(normal_data)
    anomalies = results[results['is_anomaly']]
    print(f"Detected {len(anomalies)} anomalies out of {len(results)} samples")
    print(anomalies[['timestamp', 'cpu_percent', 'anomaly_score']].head(10))

    # Save model
    detector.save('anomaly_detector_model.pkl')
```

---

## 🚀 Step 2: Train and Run Anomaly Detection

**PowerShell:**
```powershell
cd ai\sre-engineering\module-6-ai-sre\anomaly-detection

# Install dependencies
pip install pandas scikit-learn joblib

# Run anomaly detection
python anomaly_detector.py

# Expected output:
# Model trained on 1000 samples
# Detected 20 anomalies out of 1000 samples
# Model saved to anomaly_detector_model.pkl
```

**Bash:**
```bash
cd ai/sre-engineering/module-6-ai-sre/anomaly-detection

# Install dependencies
pip install pandas scikit-learn joblib

# Run anomaly detection
python anomaly_detector.py

# Expected output:
# Model trained on 1000 samples
# Detected 20 anomalies out of 1000 samples
# Model saved to anomaly_detector_model.pkl
```

---

## 🚀 Step 3: Azure AI Integration

**Create Azure OpenAI Resource:**

**PowerShell:**
```powershell
# Create Azure OpenAI resource
az cognitiveservices account create `
    --name aoai-qe-lab `
    --resource-group rg-qe-lab `
    --location eastus `
    --kind OpenAI `
    --sku S0

# Deploy a model
az cognitiveservices account deployment create `
    --resource-group rg-qe-lab `
    --name aoai-qe-lab `
    --deployment-name gpt-4o-mini `
    --model-name gpt-4o-mini `
    --model-version "0301" `
    --capacity 1

# Get API key
az cognitiveservices account keys list `
    --resource-group rg-qe-lab `
    --name aoai-qe-lab `
    --query key1 -otsv
```

**Bash:**
```bash
# Create Azure OpenAI resource
az cognitiveservices account create \
  --name aoai-qe-lab \
  --resource-group rg-qe-lab \
  --location eastus \
  --kind OpenAI \
  --sku S0

# Deploy a model
az cognitiveservices account deployment create \
  --resource-group rg-qe-lab \
  --name aoai-qe-lab \
  --deployment-name gpt-4o-mini \
  --model-name gpt-4o-mini \
  --model-version "0301" \
  --capacity 1

# Get API key
az cognitiveservices account keys list \
  --resource-group rg-qe-lab \
  --name aoai-qe-lab \
  --query key1 -otsv
```

**File:** `anomaly-detection/azure_ai_integration.py`

```python
import os
import json
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

class AzureAIIntegration:
    def __init__(self):
        self.api_key = os.getenv("AZURE_OPENAI_API_KEY")
        self.endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

        if self.api_key and self.endpoint:
            self.client = AzureOpenAI(
                api_key=self.api_key,
                api_version="2024-02-01",
                azure_endpoint=self.endpoint
            )
        else:
            self.client = None

    def analyze_anomaly(self, metric_name, value, threshold, context):
        """Analyze anomaly using Azure OpenAI"""
        prompt = f"""
        As a Site Reliability Engineer, analyze this anomaly:

        Metric: {metric_name}
        Value: {value}
        Threshold: {threshold}
        Context: {context}

        Provide:
        1. Likely root cause
        2. Immediate remediation steps
        3. Long-term prevention
        4. Severity assessment (Critical/High/Medium/Low)

        Keep response concise and actionable.
        """

        try:
            response = self.client.chat.completions.create(
                model=self.deployment_name,
                messages=[
                    {"role": "system", "content": "You are an expert QA Enterprise Architect using RAG to ensure compliance with internal security specifications."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"AI analysis failed: {str(e)}"

    def generate_runbook(self, alert_name, metric, threshold):
        """Generate runbook for alert"""
        prompt = f"""
        Create an automated runbook for the following alert:

        Alert: {alert_name}
        Metric: {metric}
        Threshold: {threshold}

        Include:
        1. Detection criteria
        2. Investigation steps
        3. Remediation steps
        4. Escalation contacts
        5. Prevention measures

        Format as markdown.
        """

        try:
            response = self.client.chat.completions.create(
                model=self.deployment_name,
                messages=[
                    {"role": "system", "content": "You are an expert QA Enterprise Architect using RAG to ensure compliance with internal security specifications."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=600,
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Runbook generation failed: {str(e)}"


# Example usage
if __name__ == "__main__":
    assistant = AzureAIIntegration()

    # Analyze anomaly
    result = assistant.analyze_anomaly(
        metric_name="CPU Utilization",
        value=95.5,
        threshold=80,
        context="Production web application experiencing high traffic"
    )
    print("=== Anomaly Analysis ===")
    print(result)

    # Generate runbook
    runbook = assistant.generate_runbook(
        alert_name="High CPU Usage",
        metric="Percentage CPU",
        threshold="80%"
    )
    print("\n=== Runbook ===")
    print(runbook)
```

---

## 🚀 Step 4: Automated Remediation

**File:** `automated-remediation/auto_remediator.py`

```python
import subprocess
import json
from datetime import datetime
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

class AutoRemediator:
    def __init__(self, subscription_id, resource_group):
        self.subscription_id = subscription_id
        self.resource_group = resource_group
        self.credential = DefaultAzureCredential()
        self.resource_client = ResourceManagementClient(self.credential, self.subscription_id)

    def restart_web_app(self, app_name):
        """Restart Azure Web App"""
        try:
            import requests
            result = self.credential.get_token("https://management.azure.com/.default")
            url = f"https://management.azure.com/subscriptions/{self.subscription_id}/resourceGroups/{self.resource_group}/providers/Microsoft.Web/sites/{app_name}/restart?api-version=2022-03-01"
            headers = {
                "Authorization": f"Bearer {result.token}",
                "Content-Type": "application/json"
            }
            response = requests.post(url, headers=headers)
            if response.status_code == 200:
                print(f"Successfully restarted {app_name}")
                return True
            else:
                print(f"Failed to restart {app_name}: {response.text}")
                return False
        except Exception as e:
            print(f"Error restarting {app_name}: {e}")
            return False

    def scale_app_service(self, app_name, instance_count):
        """Scale App Service to specified instance count"""
        try:
            import requests
            result = self.credential.get_token("https://management.azure.com/.default")
            url = f"https://management.azure.com/subscriptions/{self.subscription_id}/resourceGroups/{self.resource_group}/providers/Microsoft.Web/sites/{app_name}/config/web?api-version=2022-03-01"
            headers = {
                "Authorization": f"Bearer {result.token}",
                "Content-Type": "application/json"
            }
            body = {
                "properties": {
                    "numberOfWorkers": instance_count
                }
            }
            response = requests.put(url, headers=headers, json=body)
            if response.status_code == 200:
                print(f"Successfully scaled {app_name} to {instance_count} instances")
                return True
            else:
                print(f"Failed to scale {app_name}: {response.text}")
                return False
        except Exception as e:
            print(f"Error scaling {app_name}: {e}")
            return False

    def execute_remediation(self, alert_name, metric_value, threshold):
        """Execute automated remediation based on alert"""
        print(f"Alert: {alert_name}")
        print(f"Value: {metric_value}, Threshold: {threshold}")

        actions_taken = []

        if "CPU" in alert_name and metric_value > threshold:
            print("Taking action: Scaling up application...")
            success = self.scale_app_service("qe-app", 5)
            actions_taken.append(f"Scale app to 5 instances: {'Success' if success else 'Failed'}")

        if "Memory" in alert_name and metric_value > threshold:
            print("Taking action: Restarting application...")
            success = self.restart_web_app("qe-app")
            actions_taken.append(f"Restart app: {'Success' if success else 'Failed'}")

        print("\nActions Taken:")
        for action in actions_taken:
            print(f"  - {action}")

        return actions_taken


# Example usage
if __name__ == "__main__":
    remediator = AutoRemediator(
        subscription_id="your-subscription-id",
        resource_group="rg-qe-lab"
    )

    # Simulate alert
    remediator.execute_remediation(
        alert_name="High CPU Usage",
        metric_value=95.5,
        threshold=80
    )
```

---

## 🧪 Verification Checklist

- [ ] Anomaly detection model trained and saved
- [ ] Anomaly detection detects anomalies in test data
- [ ] Azure AI integration configured
- [ ] AI-generated recommendations for anomalies
- [ ] Automated remediation script created
- [ ] Remediation actions (scale, restart) functional
- [ ] End-to-end flow: detection analysis remediation

---

## 🔗 Next Steps

Once Phase 6 is complete, proceed to **Module 7: CI/CD Pipelines** to integrate everything into automated pipelines.

**PowerShell:**
```powershell
cd ../module-7-cicd
Get-Content README.md
```

**Bash:**
```bash
cd ../module-7-cicd
cat README.md
```
