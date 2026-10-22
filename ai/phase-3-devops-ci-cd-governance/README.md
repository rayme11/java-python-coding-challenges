# Phase 3: DevOps, CI/CD & Governance Integration

## Overview

This phase covers integrating quality gates into CI/CD pipelines, environment management, test data planning, and root cause analysis for production incidents.

**Prerequisites:** Phase 1 & 2 complete, GitHub Actions knowledge, cloud account (Azure/AWS optional)

**Back to:** [Master Track Overview](ai/README.md)

---

## Lesson 3.1: Pipeline Quality Gates

### Theory

| Quality Gate | Purpose | Threshold Example |
|--------------|---------|-------------------|
| Build Gate | Code compiles successfully | 0 compilation errors |
| Unit Test Gate | Unit tests pass | 0 failed tests |
| Coverage Gate | Minimum test coverage | 80% line coverage |
| Integration Gate | Integration tests pass | 0 failed tests |
| Security Gate | No critical vulnerabilities | 0 critical issues |
| Performance Gate | Response time within SLA | < 2 seconds |

### Hands-on Exercise

Create a quality gate evaluator that checks multiple conditions:

**File:** [`ReleaseQualityGate.java`](./java/enterprise/qe/gates/ReleaseQualityGate.java)

```java
package enterprise.qe.gates;

public class ReleaseQualityGate {
    public static boolean isReleaseReady(int failedTests, double coverage, int criticalBugs, double avgResponseTime) {
        if (failedTests > 0) return false;
        if (coverage < 80.0) return false;
        if (criticalBugs > 0) return false;
        if (avgResponseTime > 2000) return false;
        return true;
    }
    
    public static void main(String[] args) {
        boolean ready = isReleaseReady(0, 85.5, 0, 1500);
        System.out.println("Release Ready: " + ready);
    }
}
```

**Steps:**
1. Write the quality gate evaluator
2. Test with various input combinations
3. Document the thresholds used

---

## Lesson 3.2: Environment & Test Data Management

### Theory

| Component | Description | Cloud Option |
|-----------|-------------|--------------|
| Test Environments | Isolated environments for testing | Azure VMs, AWS EC2 |
| Test Data | Representative data for test scenarios | Azure SQL, AWS RDS |
| Data Masking | Protecting sensitive test data | Custom scripts |
| Environment Provisioning | Automated environment setup | Terraform, ARM templates |

### Cost Optimization

- Use Azure free tier for test VMs (up to 750 hours/month)
- Use AWS free tier for EC2 t2.micro (750 hours/month)
- Use local Docker containers when possible
- Schedule test environments to shut down after hours

### Hands-on Exercise

Create environment readiness checklist:

**File:** [`environment-readiness.yaml`](./python/environment-readiness.yaml)

```yaml
environment: staging
services:
  - name: api-service
    url: https://staging-api.example.com
    status: required
  - name: database
    url: jdbc:postgresql://staging-db.example.com:5432
    status: required
testData:
  users: 1000
  products: 500
  orders: 2000
qualityGates:
  minCoverage: 80
  maxResponseTime: 2000
  allowedCriticalBugs: 0
```

---

## Lesson 3.3: Root Cause Analysis & Incident Management

### Theory

**RCA Process:**
1. Detect incident (monitoring/alerting)
2. Contain impact (rollback/feature flag)
3. Investigate root cause (logs, traces, metrics)
4. Implement fix
5. Prevent recurrence (test coverage, monitoring)

**Escaped Defect Categories:**
- Requirements gaps
- Test coverage gaps
- Environment mismatches
- Data issues
- Third-party dependencies

### Hands-on Exercise

Create an incident analysis template:

**File:** [`incident-template.md`](./python/incident-template.md)

```markdown
# Incident Analysis Template

## Incident Details
- **Date:** 
- **Severity:** 
- **Component:** 
- **Reported By:** 

## Timeline
- Detection:
- Containment:
- Resolution:
- Post-mortem:

## Root Cause
- Primary cause:
- Contributing factors:

## Corrective Actions
- Immediate fix:
- Long-term prevention:
- Test coverage added:
- Monitoring improved:
```

---

---

## Lesson 3.4: Performance Testing Integration in CI/CD

### Theory

Performance testing is crucial for ensuring applications remain responsive, scalable, and stable under expected and peak load conditions. Integrating performance tests into CI/CD pipelines allows for early detection of performance regressions.

**Key Concepts:**
-   **Load Testing:** Assessing system behavior under anticipated load.
-   **Stress Testing:** Determining system stability beyond normal operating capacity.
-   **Scalability Testing:** Measuring the system's ability to scale up or down.
-   **Performance Metrics:** Response times, throughput, error rates, resource utilization (CPU, memory, network).

**Common Tools (Conceptual):**
-   **JMeter:** Open-source, Java-based tool for load testing functional behavior and measuring performance.
-   **Locust:** Open-source, Python-based tool for writing load tests with Python code. Ideal for programmatic and customizable scenarios.
-   **LoadRunner/NeoLoad:** Commercial tools offering extensive features for enterprise-level performance testing.

**CI/CD Integration Strategy:**
1.  **Threshold Definition:** Define clear performance SLAs (e.g., response time < 200ms, error rate < 1%).
2.  **Test Script Versioning:** Store performance test scripts in version control alongside application code.
3.  **Automated Execution:** Trigger performance tests automatically in the CI pipeline (e.g., nightly builds, before major releases).
4.  **Reporting & Alerting:** Generate reports (HTML, JSON) and configure alerts for threshold breaches.
5.  **Environment Provisioning:** Use dedicated, stable environments for performance testing, potentially leveraging cloud services (Azure Load Testing, AWS Device Farm for mobile performance).

### Hands-on Exercise: Lightweight Performance Test (Python)

**Objective:** Create a simple Python script using `locust` (or a mock thereof) to simulate basic user load on an API endpoint and integrate its execution into the CI process (conceptually).

**File:** [`./python/api_performance_test.py`](./python/api_performance_test.py)

```python
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)  # Users wait between 1 and 2 seconds between tasks

    @task
    def get_posts(self):
        # Simulate fetching posts from a placeholder API
        self.client.get("/posts/1", name="/posts/[id]")

    @task(3) # This task will be called 3 times more often than other tasks
    def create_post(self):
        # Simulate creating a new post
        headers = {'Content-type': 'application/json; charset=UTF-8'}
        payload = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        self.client.post("/posts", json=payload, headers=headers)

if __name__ == "__main__":
    # In a real CI/CD setup, Locust would be run via command line
    # Example: locust -f api_performance_test.py --host=https://jsonplaceholder.typicode.com
    print("This script defines Locust performance tests.")
    print("To run: pip install locust && locust -f api_performance_test.py --host=https://jsonplaceholder.typicode.com")
    print("Open http://localhost:8089 in browser after running to see results.")
```

**Steps:**
1.  Ensure Python 3.10+ is installed.
2.  Install Locust: `pip install locust`
3.  Create the file `./python/api_performance_test.py` in the Phase 3 Python directory.
4.  Run the Locust test from your terminal (from the Phase 3 directory):
    ```bash
    locust -f python/api_performance_test.py --host=https://jsonplaceholder.typicode.com
    ```
5.  Open your browser to `http://localhost:8089` to observe the performance test running.
6.  (Conceptual) Integrate this into a GitHub Actions workflow that triggers on specific events and reports metrics.

---

## Phase 3 Checklist

```
[ ] Lesson 3.1 - Pipeline quality gates implementation
[ ] Lesson 3.2 - Environment & test data management
[ ] Lesson 3.3 - Root cause analysis & incident management
[ ] Lesson 3.4 - Performance Testing Integration in CI/CD
```

**Next:** Proceed to [Phase 4 - Executive QE Leadership & Culture Building](ai/phase-4-executive-qe-leadership/README.md)
