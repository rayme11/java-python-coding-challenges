# Phase 2: Scalable Web & API Test Engineering

## Overview

This phase covers enterprise-grade web and API test automation using Selenium, Playwright, BDD frameworks, and stability practices.

**Prerequisites:** Phase 1 complete, Java/Python knowledge, Chrome browser installed, Maven installed.

**Back to:** [Master Track Overview](ai/README.md)

---

## Lesson 2.1: Web Automation Foundations (Real Selenium & Playwright)

### Objective
Understand and implement real web automation using Selenium and Playwright against a live Heroku test application, with visible browser execution.

### Theory

| Topic | Description |
|-------|-------------|
| Selenium WebDriver | Industry-standard browser automation tool. Uses `ChromeDriver` to control Chrome. |
| Playwright | Microsoft's modern automation framework with auto-wait. Supports Chromium, Firefox, WebKit. |
| Page Object Model | Design pattern for maintainable test code. |
| Locator Strategies | ID, name, CSS, XPath selectors. |
| Wait Mechanisms | Implicit, explicit, fluent waits (crucial for stable UI tests). |

### Hands-on Exercise: Real Selenium Automation (Visible Browser)

**Goal:** Automate a login flow on the Heroku App with a visible Chrome browser.

**File:** [`WebAutomationExample.java`](ai/phase-2-scalable-web-api-test-engineering/java/enterprise/qe/web/WebAutomationExample.java)

```java
package enterprise.qe.web;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import io.github.bonigarcia.wdm.WebDriverManager;

public class WebAutomationExample {
    public static void main(String[] args) {
        WebDriver driver = null;
        try {
            WebDriverManager.chromedriver().browserVersion("155").setup(); // Auto-download ChromeDriver

            ChromeOptions options = new ChromeOptions();
            // No --headless argument - browser opens visibly on your screen
            options.addArguments("--no-sandbox");
            options.addArguments("--disable-dev-shm-usage");
            options.addArguments("--disable-gpu");
            options.addArguments("--window-size=1920,1080");
            options.addArguments("--start-maximized");

            System.out.println("Launching real Chrome browser...");
            driver = new ChromeDriver(options);

            System.out.println("Navigating to Heroku test app: https://the-internet.herokuapp.com/login");
            driver.get("https://the-internet.herokuapp.com/login");

            WebElement usernameField = driver.findElement(By.id("username"));
            usernameField.sendKeys("tomsmith");

            WebElement passwordField = driver.findElement(By.id("password"));
            passwordField.sendKeys("SuperSecretPassword!");

            WebElement loginButton = driver.findElement(By.cssSelector("button.radius"));
            loginButton.click();

            String currentUrl = driver.getCurrentUrl();
            System.out.println("Current URL: " + currentUrl);

            WebElement flashMessage = driver.findElement(By.id("flash"));
            String flashText = flashMessage.getText();
            System.out.println("Flash message: " + flashText);

            if (flashText.contains("You logged into a secure area!")) {
                System.out.println("Test PASSED: Successfully logged into Heroku test app");
            } else {
                System.out.println("Test FAILED: Login did not succeed");
            }
            
            // In a real test, you'd use explicit waits instead of Thread.sleep
            // System.out.println("Keeping browser open for 5 seconds...");
            // Thread.sleep(5000);

        } catch (Exception e) {
            System.err.println("Test ERROR: " + e.getMessage());
            System.err.println("Ensure Chrome browser is installed.");
        } finally {
            if (driver != null) {
                driver.quit();
                System.out.println("Browser session closed.");
            }
        }
    }
}
```

**To Run (from `ai/phase-2-scalable-web-api-test-engineering/maven`):**
```bash
mvn clean install exec:java -Dexec.mainClass="enterprise.qe.web.WebAutomationExample"
```

### Hands-on Exercise: Playwright Automation (Visible Browser)

**Goal:** Automate a login flow on the Heroku App with a visible Chromium browser using Playwright.

**File:** [`PlaywrightExample.java`](ai/phase-2-scalable-web-api-test-engineering/java/enterprise/qe/web/PlaywrightExample.java)

```java
package enterprise.qe.web;

import com.microsoft.playwright.*;
import com.microsoft.playwright.options.AriaRole;

public class PlaywrightExample {
    public static void main(String[] args) {
        try (Playwright playwright = Playwright.create()) {
            // Launch VISIBLE browser (headless: false so you can see it)
            Browser browser = playwright.chromium().launch(new BrowserType.LaunchOptions()
                .setHeadless(false)
                .setArgs(java.util.Arrays.asList("--no-sandbox", "--disable-dev-shm-usage", "--disable-gpu"))
            );

            BrowserContext context = browser.newContext(new Browser.NewContextOptions()
                .setViewportSize(1920, 1080)
            );

            Page page = context.newPage();

            System.out.println("Launching real Playwright Chromium browser...");
            System.out.println("Navigating to Heroku test app: https://the-internet.herokuapp.com/login");
            page.navigate("https://the-internet.herokuapp.com/login");

            page.fill("#username", "tomsmith");
            System.out.println("Entered username: tomsmith");

            page.fill("#password", "SuperSecretPassword!");
            System.out.println("Entered password");

            page.click("button.radius");
            System.out.println("Clicked login button");

            page.waitForSelector("#flash");

            String flashText = page.textContent("#flash");
            System.out.println("Flash message: " + flashText);

            String currentUrl = page.url();
            System.out.println("Current URL: " + currentUrl);

            if (flashText.contains("You logged into a secure area!")) {
                System.out.println("Test PASSED: Successfully logged into Heroku test app with Playwright");
            } else {
                System.out.println("Test FAILED: Login did not succeed");
            }

            System.out.println("Keeping browser open for 5 seconds...");
            page.waitForTimeout(5000);

            browser.close();
            System.out.println("Browser session closed.");
        } catch (Exception e) {
            System.err.println("Test ERROR: " + e.getMessage());
        }
    }
}
```

**To Run (from `ai/phase-2-scalable-web-api-test-engineering/maven`):**
```bash
mvn clean install exec:java -Dexec.mainClass="enterprise.qe.web.PlaywrightExample"
```

---

## Lesson 2.2: API Testing (Real REST Assured)

### Objective
Implement robust API testing against a live public API (JSONPlaceholder for now, could be Heroku API).

### Theory

| Topic | Description |
|-------|-------------|
| REST API Testing | Testing HTTP endpoints and responses using libraries like REST Assured. |
| Payload Validation | Verifying JSON/XML response structure and data correctness. |
| Schema Checking | Validating responses against a predefined schema (e.g., JSON Schema). |
| Contract Testing | Ensuring API consumer and producer contracts remain compatible. |

### Hands-on Exercise: Real API Testing with REST Assured

**Goal:** Perform GET and POST requests against `https://jsonplaceholder.typicode.com/`.

**File:** [`ApiTest.java`](ai/phase-2-scalable-web-api-test-engineering/maven/src/test/java/enterprise/qe/api/ApiTest.java)

```java
package enterprise.qe.api;

import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import static org.junit.jupiter.api.Assertions.*;

public class ApiTest {

    @Test
    @DisplayName("GET /posts/1 should return 200 with valid JSON")
    void testGetPost() {
        Response response = RestAssured.get("https://jsonplaceholder.typicode.com/posts/1");

        assertEquals(200, response.getStatusCode(), "Should return 200 OK");
        assertTrue(response.getBody().asString().contains("title"), "Response should contain 'title'");
        assertTrue(response.getBody().asString().contains("body"), "Response should contain 'body'");
        assertTrue(response.getBody().asString().contains("userId"), "Response should contain 'userId'");

        System.out.println("API Test PASSED: GET /posts/1 returned valid response");
    }

    @Test
    @DisplayName("GET /posts/1 should contain expected fields")
    void testPostFields() {
        Response response = RestAssured.get("https://jsonplaceholder.typicode.com/posts/1");

        int userId = response.jsonPath().getInt("userId");
        int id = response.jsonPath().getInt("id");
        String title = response.jsonPath().getString("title");
        String body = response.jsonPath().getString("body");

        assertTrue(userId > 0, "userId should be positive");
        assertTrue(id > 0, "id should be positive");
        assertNotNull(title, "title should not be null");
        assertNotNull(body, "body should not be null");
        assertFalse(title.isEmpty(), "title should not be empty");
        assertFalse(body.isEmpty(), "body should not be empty");

        System.out.println("API Test PASSED: All fields present and valid");
    }

    @Test
    @DisplayName("POST /posts should create a new resource")
    void testCreatePost() {
        String requestBody = "{\"title\":\"foo\",\"body\":\"bar\",\"userId\":1}";

        Response response = RestAssured.given()
            .header("Content-Type", "application/json")
            .body(requestBody)
            .post("https://jsonplaceholder.typicode.com/posts");

        assertEquals(201, response.getStatusCode(), "Should return 201 Created");
        assertEquals("foo", response.jsonPath().getString("title"));
        assertEquals("bar", response.jsonPath().getString("body"));
        assertEquals(1, response.jsonPath().getInt("userId"));

        System.out.println("API Test PASSED: POST /posts created new resource");
    }
}
```

**To Run (from `ai/phase-2-scalable-web-api-test-engineering/maven`):**
```bash
mvn test -Dtest=ApiTest
```

---

## Lesson 2.3: BDD with Gherkin & Robot Framework

### Objective
Understand Behavior-Driven Development (BDD) principles using Gherkin syntax and how to implement tests with Robot Framework.

### Theory

**Gherkin Syntax:** A plain-language parser that describes software behavior in a human-readable format.
```gherkin
Feature: User Login
  Scenario: Successful login
    Given the user is on the login page
    When the user enters valid credentials
    Then the user should be redirected to the dashboard
```

**Robot Framework Keyword-Driven:** An open-source, keyword-driven test automation framework. Can be extended with Python libraries.
```robotframework
*** Test Cases ***
Valid Login
    Open Browser    https://the-internet.herokuapp.com/login    chrome
    Input Text    username_field    tomsmith
    Input Text    password_field    SuperSecretPassword!
    Click Button    login_button
    Page Should Contain    You logged into a secure area!
```

### Hands-on Exercise: Create a Gherkin Feature File

**File:** [`login.feature`](ai/phase-2-scalable-web-api-test-engineering/python/features/login.feature)

```gherkin
Feature: Enterprise Login
  Scenario: Valid credentials
    Given user navigates to login page
    When user enters valid username and password
    Then dashboard should be displayed

  Scenario: Invalid credentials
    Given user navigates to login page
    When user enters invalid username or password
    Then error message should be displayed

  Scenario: Empty credentials
    Given user navigates to login page
    When user leaves username and password empty
    Then validation error should be shown
```

**Next Steps (Future lessons):**
- Install Robot Framework with SeleniumLibrary.
- Implement Python keywords to map Gherkin steps.
- Integrate Robot Framework tests into CI/CD.

---

## Lesson 2.4: Flaky Test Reduction & Stability (Real JUnit)

### Objective
Understand common causes of flaky tests and implement strategies to reduce them, using JUnit 5.

### Theory

| Technique | Description |
|-----------|-------------|
| Retry Mechanisms | Automatically re-execute failed tests a configurable number of times. |
| Parallel Execution | Run tests concurrently to reduce execution time, but manage shared resources carefully. |
| Test Data Management | Isolate test data per test to prevent interference and ensure idempotency. |
| Wait Strategies | Use explicit waits (e.g., `WebDriverWait` in Selenium, `page.waitFor...` in Playwright) instead of `Thread.sleep()`. |

### Hands-on Exercise: Real JUnit Stability Tests

**Goal:** Demonstrate retry logic for an unstable test and verify retry limits.

**File:** [`StabilityTest.java`](ai/phase-2-scalable-web-api-test-engineering/maven/src/test/java/enterprise/qe/stability/StabilityTest.java)

```java
package enterprise.qe.stability;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import static org.junit.jupiter.api.Assertions.*;

public class StabilityTest {

    @Test
    @DisplayName("Retry logic handles flaky test scenarios")
    void testRetryLogic() {
        int maxRetries = 3;
        boolean success = false;

        for (int i = 0; i < maxRetries; i++) {
            try {
                success = executeUnstableTest();
                if (success) {
                    System.out.println("Test PASSED on attempt " + (i + 1));
                    return;
                }
            } catch (Exception e) {
                System.out.println("Attempt " + (i + 1) + " failed: " + e.getMessage());
            }
        }

        if (!success) {
            fail("Test FAILED after " + maxRetries + " retries");
        }
    }

    @Test
    @DisplayName("Verify retry counter does not exceed maximum")
    void testRetryCounterLimit() {
        int maxRetries = 5;
        int attempts = 0;

        for (int i = 0; i < maxRetries; i++) {
            attempts++;
            if (Math.random() > 0.5) break;
        }

        assertTrue(attempts <= maxRetries, "Should not exceed max retries");
        System.out.println("Stability Test PASSED: Completed in " + attempts + " attempts");
    }

    @Test
    @DisplayName("Stable test always passes")
    void testStable() {
        assertTrue(true, "Stable test should always pass");
        System.out.println("Stability Test PASSED: Stable test executed");
    }

    private boolean executeUnstableTest() {
        return Math.random() > 0.3;
    }
}
```

**To Run (from `ai/phase-2-scalable-web-api-test-engineering/maven`):**
```bash
mvn test -Dtest=StabilityTest
```

---

## Phase 2 Checklist

```
[ ] Lesson 2.1 - Web automation with Selenium/Playwright (Visible Browser)
[ ] Lesson 2.2 - API testing fundamentals (Real REST Assured)
[ ] Lesson 2.3 - BDD with Gherkin & Robot Framework
[ ] Lesson 2.4 - Flaky test reduction strategies (Real JUnit)
```

**Next:** Proceed to [Phase 3 - DevOps, CI/CD & Governance Integration](ai/phase-3-devops-ci-cd-governance/README.md)
