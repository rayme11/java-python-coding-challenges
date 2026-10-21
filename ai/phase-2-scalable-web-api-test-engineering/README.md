# Phase 2: Scalable Web & API Test Engineering

## Overview

This phase covers enterprise-grade web and API test automation using Selenium, Playwright, BDD frameworks, and stability practices.

**Prerequisites:** Phase 1 complete, Java/Python knowledge, browser drivers installed

**Back to:** [Master Track Overview](ai/README.md)

---

## Lesson 2.1: Web Automation Foundations

### Theory

| Topic | Description |
|-------|-------------|
| Selenium WebDriver | Industry-standard browser automation tool |
| Playwright | Microsoft's modern automation framework with auto-wait |
| Page Object Model | Design pattern for maintainable test code |
| Locator Strategies | ID, name, CSS, XPath selectors |
| Wait Mechanisms | Implicit, explicit, fluent waits |

### Hands-on Exercise

Create a simple Selenium test in Java:

```java
package enterprise.qe.web;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class WebAutomationExample {
    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        driver.get("https://example.com");
        String title = driver.getTitle();
        System.out.println("Page title: " + title);
        driver.quit();
    }
}
```

**File:** [`WebAutomationExample.java`](./java/enterprise/qe/web/WebAutomationExample.java)

**Steps:**
1. Download ChromeDriver matching your Chrome version
2. Add Selenium dependencies to your project
3. Compile and run the test
4. Verify the browser opens and closes

---

## Lesson 2.2: API Testing

### Theory

| Topic | Description |
|-------|-------------|
| REST API Testing | Testing HTTP endpoints and responses |
| Payload Validation | Verifying JSON/XML response structure |
| Schema Checking | Validating response against defined schema |
| Contract Testing | Ensuring consumer-producer compatibility |

### Hands-on Exercise

Create an API test using Java:

```java
package enterprise.qe.api;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class ApiTestExample {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://jsonplaceholder.typicode.com/posts/1"))
            .GET()
            .build();
        
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println("Status: " + response.statusCode());
        System.out.println("Body: " + response.body());
    }
}
```

**File:** [`ApiTestExample.java`](./java/enterprise/qe/api/ApiTestExample.java)

**Steps:**
1. Write the API test code
2. Compile and run
3. Verify 200 status code and valid JSON response

---

## Lesson 2.3: BDD with Gherkin & Robot Framework

### Theory

**Gherkin Syntax:**
```
Feature: User Login
  Scenario: Successful login
    Given the user is on the login page
    When the user enters valid credentials
    Then the user should be redirected to the dashboard
```

**Robot Framework Keyword-Driven:**
```
*** Test Cases ***
Valid Login
    Open Browser    https://example.com    chrome
    Input Text    username_field    testuser
    Input Text    password_field    testpass
    Click Button    login_button
    Page Should Contain    Welcome
```

### Hands-on Exercise

Create a feature file:

**File:** [`login.feature`](./python/features/login.feature)

```
Feature: Enterprise Login
  Scenario: Valid credentials
    Given user navigates to login page
    When user enters valid username and password
    Then dashboard should be displayed
```

---

## Lesson 2.4: Flaky Test Reduction & Stability

### Theory

| Technique | Description |
|-----------|-------------|
| Retry Mechanisms | Automatically retry failed tests |
| Parallel Execution | Run tests concurrently to reduce time |
| Test Data Management | Isolate test data to prevent interference |
| Wait Strategies | Use explicit waits instead of sleep |

### Hands-on Exercise

Create a test with retry logic:

**File:** [`FlakyTestExample.java`](./java/enterprise/qe/stability/FlakyTestExample.java)

```java
package enterprise.qe.stability;

public class FlakyTestExample {
    public static void main(String[] args) {
        int maxRetries = 3;
        boolean success = false;
        
        for (int i = 0; i < maxRetries; i++) {
            try {
                success = executeTest();
                if (success) break;
            } catch (Exception e) {
                System.out.println("Attempt " + (i + 1) + " failed: " + e.getMessage());
            }
        }
        
        System.out.println(success ? "Test passed!" : "Test failed after retries");
    }
    
    static boolean executeTest() {
        return Math.random() > 0.3;
    }
}
```

---

## Phase 2 Checklist

```
[ ] Lesson 2.1 - Web automation with Selenium/Playwright
[ ] Lesson 2.2 - API testing fundamentals
[ ] Lesson 2.3 - BDD with Gherkin & Robot Framework
[ ] Lesson 2.4 - Flaky test reduction strategies
```

**Next:** Proceed to [Phase 3 - DevOps, CI/CD & Governance Integration](ai/phase-3-devops-ci-cd-governance/README.md)
