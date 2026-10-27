import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def create_extended_study_guide():
    doc = Document()
    
    # Page setup - 1 inch margins
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Styling Helper Functions
    def add_title(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(text)
        run.font.name = 'Arial'
        run.font.size = Pt(22)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D) # Navy
        p.paragraph_format.space_after = Pt(4)
        return p

    def add_subtitle(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(text)
        run.font.name = 'Arial'
        run.font.size = Pt(13)
        run.font.italic = True
        run.font.color.rgb = RGBColor(0x5C, 0x76, 0x8D) # Slate Grey
        p.paragraph_format.space_after = Pt(18)
        return p

    def add_h1(text):
        p = doc.add_paragraph()
        run = p.add_run(text)
        run.font.name = 'Arial'
        run.font.size = Pt(16)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        run = p.add_run(text)
        run.font.name = 'Arial'
        run.font.size = Pt(13)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x41, 0x74, 0x8D) # Steel Blue
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        return p

    def add_h3(text):
        p = doc.add_paragraph()
        run = p.add_run(text)
        run.font.name = 'Arial'
        run.font.size = Pt(11.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x2C, 0x3E, 0x50)
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        return p

    def add_body(text, bold_prefix=None):
        p = doc.add_paragraph()
        if bold_prefix:
            r_bold = p.add_run(bold_prefix)
            r_bold.font.name = 'Calibri'
            r_bold.font.size = Pt(11)
            r_bold.font.bold = True
            r_bold.font.color.rgb = RGBColor(0x2C, 0x3E, 0x50)
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        return p

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        if bold_prefix:
            r_bold = p.add_run(bold_prefix)
            r_bold.font.name = 'Calibri'
            r_bold.font.size = Pt(11)
            r_bold.font.bold = True
            r_bold.font.color.rgb = RGBColor(0x2C, 0x3E, 0x50)
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        return p

    def add_callout(text, title="KEY ENTERPRISE ARCHITECTURE INSIGHT"):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = table.cell(0, 0)
        cell.width = Inches(6.5)
        
        shading = parse_xml(r'<w:shd {} w:fill="F4F6F9"/>'.format(nsdecls('w')))
        cell._tc.get_or_add_tcPr().append(shading)
        
        tcPr = cell._tc.get_or_add_tcPr()
        borders = parse_xml(r'<w:tcBorders {}><w:left w:val="single" w:sz="36" w:space="0" w:color="1B365D"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>'.format(nsdecls('w')))
        tcPr.append(borders)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
        r_title = p.add_run(f"📌 {title}\n")
        r_title.font.name = 'Arial'
        r_title.font.size = Pt(10)
        r_title.font.bold = True
        r_title.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
        
        r_text = p.add_run(text)
        r_text.font.name = 'Calibri'
        r_text.font.size = Pt(10.5)
        r_text.font.italic = True
        r_text.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
        
        doc.add_paragraph().paragraph_format.space_after = Pt(6)

    def add_code_snippet(code_text, caption="Source Code Implementation"):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = table.cell(0, 0)
        cell.width = Inches(6.5)
        
        shading = parse_xml(r'<w:shd {} w:fill="2D3748"/>'.format(nsdecls('w')))
        cell._tc.get_or_add_tcPr().append(shading)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
        r_cap = p.add_run(f"💻 {caption}\n")
        r_cap.font.name = 'Courier New'
        r_cap.font.size = Pt(9)
        r_cap.font.bold = True
        r_cap.font.color.rgb = RGBColor(0xA0, 0xAE, 0xC0)
        
        p2 = cell.add_paragraph()
        p2.paragraph_format.space_before = Pt(2)
        p2.paragraph_format.space_after = Pt(6)
        r_code = p2.add_run(code_text)
        r_code.font.name = 'Consolas'
        r_code.font.size = Pt(9.5)
        r_code.font.color.rgb = RGBColor(0xE2, 0xE8, 0xF0)
        
        doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ==================== DOCUMENT GENERATION ====================

    add_title("AI-Enhanced Enterprise Quality Engineering & Governance")
    add_subtitle("Comprehensive Master Study Guide & Architectural Reference Manual\nPrepared for Senior QA Engineering Managers (Verizon, Trimble, Palo Alto Networks, CIBC)")

    add_callout(
        "This master manual provides exhaustive technical depth across multi-language automation (Python, Java, TypeScript), advanced framework engineering (Selenium, Playwright, REST Assured), DevOps pipeline governance, and cutting-edge AI architectures (Trust Architecture, LLM-as-a-Judge, and Shift-Right telemetry). Designed to serve as an authoritative reference for enterprise engineering leaders.",
        "EXECUTIVE COMPREHENSIVE STUDY GUIDE"
    )

    # ----------------------------------------------------
    add_h1("Chapter 1: The Evolution of Quality Engineering & The AI Paradox")
    # ----------------------------------------------------
    add_body("Modern software delivery operates at unprecedented velocity. Microservices, event-driven architectures, and continuous deployment have made manual quality assurance obsolete. Enterprise organizations like Verizon, CIBC, and Palo Alto Networks demand automated, AI-augmented quality engineering that scales across millions of daily active users and multi-cloud environments.")
    
    add_h2("1.1 The AI Paradox in Quality Assurance")
    add_body("A pervasive phenomenon in modern engineering is the 'AI Paradox in QA': organizations experience a massive surge in AI adoption, automatic test case generation, and code coverage metrics, yet simultaneously suffer from rising production defect rates. This occurs because raw test volume does not equal semantic test validity. Foundational models generate hundreds of redundant, surface-level assertions while failing to comprehend nuanced business domain logic, race conditions, or complex multi-tenant data dependencies.")
    add_body("To overcome this paradox, senior QA engineering managers must implement rigorous governance frameworks, contextual test validation, semantic deduplication, and automated fault injection (mutation testing).")

    add_h2("1.2 Strategic Pillars of AI-Enhanced QE")
    add_bullet("Transitioning from reactive defect detection after release to proactive quality engineering embedded directly into user story creation and architecture design.", "Shift-Left & Continuous Validation: ")
    add_bullet("Using AI models to synthesize synthetic user data, predict brittle test paths, and self-heal element locators.", "Autonomous Test Augmentation: ")
    add_bullet("Enforcing non-negotiable pipeline gates that block artifact promotion if unit, integration, security, or performance thresholds are violated.", "Automated Governance: ")
    add_bullet("Maintaining strict audit logs, model explainability, and Human-in-the-Loop (HIL) sign-offs for high-risk modules.", "Defensible Compliance: ")

    # ----------------------------------------------------
    add_h1("Chapter 2: Phase 1 - AI Test Orchestration, Developer AI Tools & MCP Servers")
    # ----------------------------------------------------
    add_body("Phase 1 establishes how senior engineering leaders leverage artificial intelligence and developer tooling not just as code-generation novelties, but as integrated systems connected directly to enterprise engineering workflows.")

    add_h2("2.1 Developer AI Tools in Enterprise QE")
    add_body("Tools like GitHub Copilot, Cursor, and Devin AI transform day-to-day engineering productivity. In a QE context, managers establish guidelines for how engineers utilize these tools:")
    add_bullet("Accelerating test scaffolding, boilerplate generation, data-driven test structures, and complex mocking stubs.", "Test Code Scaffolding: ")
    add_bullet("Analyzing stack traces, flaky test failure patterns, and container logs to surface root causes in seconds.", "Automated Debugging Support: ")
    add_bullet("Refactoring legacy automation suites for maintainability, parallel execution readiness, and reduced flakiness.", "TestSuite Optimization: ")

    add_h2("2.2 Model Context Protocol (MCP) & LLM Agent Integrations")
    add_body("Enterprise AI automation requires secure, bidirectional communication between Large Language Models and internal systems (Jira, GitHub, TestRail, Snowflake). Model Context Protocol (MCP) and custom agentic orchestration layers allow LLMs to query schemas, fetch requirements, and report test results programmatically.")

    add_h2("2.3 Code Implementation: LLM Test Data Generator (Python)")
    add_body("Below is the production-grade Python script implemented in our training track, illustrating how an AI orchestration layer synthesizes structured test data and simulates interaction with an internal database API.")
    
    add_code_snippet(
        """import json
import random

def generate_test_user_data(requirements: str) -> dict:
    \"\"\"
    Simulates an LLM agent generating contextual test data based on natural language requirements.
    In enterprise deployments, this interfaces with Azure OpenAI or AWS Bedrock APIs.
    \"\"\"
    print(f"[LLM Agent] Processing Natural Language Requirements: '{requirements}'")

    mock_data = {
        "valid_user": {
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@enterprise.com",
            "age": 30,
            "isActive": True
        },
        "invalid_email_user": {
            "firstName": "Jane",
            "lastName": "Smith",
            "email": "invalid-email-format",
            "age": 25,
            "isActive": True
        },
        "minor_user": {
            "firstName": "Alice",
            "lastName": "Wonder",
            "email": "alice.wonder@enterprise.com",
            "age": 16,
            "isActive": False
        }
    }

    if "invalid email" in requirements.lower():
        return mock_data["invalid_email_user"]
    elif "minor" in requirements.lower():
        return mock_data["minor_user"]
    else:
        return mock_data["valid_user"]

def mock_save_user_to_internal_system(user_data: dict) -> bool:
    \"\"\"
    Simulates interaction with internal backend systems (MCP Connector / Database API).
    \"\"\"
    email = user_data.get('email', '')
    print(f"[Internal System API] Saving user record: {email}")
    if email and '@' in email and '.' in email.split('@')[1]:
        print("[Internal System API] Success: User record persisted.")
        return True
    else:
        print("[Internal System API] Error: Persistence rejected due to data validation rules.")
        return False

if __name__ == "__main__":
    print("=== Enterprise LLM Test Data Generation & Integration Harness ===")
    
    reqs = ["Standard valid user", "User with invalid email format", "Minor user under 18"]
    for req in reqs:
        data = generate_test_user_data(req)
        print(f"Generated Payload:\\n{json.dumps(data, indent=2)}")
        mock_save_user_to_internal_system(data)
        print("-" * 50)
""",
        "llm_test_data_generator.py"
    )

    # ----------------------------------------------------
    add_h1("Chapter 3: Phase 2 - Scalable Web, API & Mobile Test Engineering Frameworks")
    # ----------------------------------------------------
    add_body("Phase 2 bridges multi-language framework engineering, comparing Selenium WebDriver and Playwright across Java and TypeScript, while establishing robust API test suites.")

    add_h2("3.1 Selenium WebDriver vs. Playwright Architectural Analysis")
    add_bullet("Communicates via JSON Wire Protocol / W3C WebDriver specification over HTTP. Requires browser-specific driver binaries (ChromeDriver, GeckoDriver) and explicit wait strategies.", "Selenium WebDriver: ")
    add_bullet("Communicates directly over WebSocket protocol with browser binaries. Features auto-waiting on elements before interactions, multi-context browser isolation (ideal for testing multi-user chat or roles), and built-in network interception.", "Playwright (TypeScript / Python / Java): ")

    add_h2("3.2 TypeScript Playwright Page Object Model (POM)")
    add_body("Our enterprise TypeScript Playwright framework enforces strict separation of concerns, ensuring maintainability across large-scale UI test suites.")

    add_code_snippet(
        """import { Page, Locator } from '@playwright/test';

/**
 * Page Object Model for Heroku Secure Authentication Feature
 */
export class LoginPage {
  readonly page: Page;
  readonly usernameInput: Locator;
  readonly passwordInput: Locator;
  readonly loginButton: Locator;
  readonly flashMessage: Locator;

  constructor(page: Page) {
    this.page = page;
    this.usernameInput = page.locator('#username');
    this.passwordInput = page.locator('#password');
    this.loginButton = page.locator('button.radius');
    this.flashMessage = page.locator('#flash');
  }

  async goto() {
    await this.page.goto('/login');
  }

  async login(username: string, password: string) {
    await this.usernameInput.fill(username);
    await this.passwordInput.fill(password);
    await this.loginButton.click();
  }

  async getFlashMessageText(): Promise<string> {
    return await this.flashMessage.textContent() || '';
  }
}
""",
        "LoginPage.ts (TypeScript Playwright POM)"
    )

    add_h2("3.3 Enterprise API Testing with REST Assured (Java)")
    add_body("Backend microservices validation requires robust contract testing, JSON payload parsing, and schema validation.")

    add_code_snippet(
        """package enterprise.qe.api;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

/**
 * Enterprise API Test Suite using REST Assured against JSONPlaceholder
 */
public class ApiTest {

    @Test
    @DisplayName("Validate GET /posts/1 returns valid schema and resource ID")
    void testGetPostValidatesSuccessfully() {
        given()
            .baseUri("https://jsonplaceholder.typicode.com")
            .header("Accept", "application/json")
        .when()
            .get("/posts/1")
        .then()
            .statusCode(200)
            .body("id", equalTo(1))
            .body("userId", notNullValue())
            .body("title", notNullValue())
            .body("body", notNullValue());
            
        System.out.println("API Test PASSED: GET /posts/1 validated successfully.");
    }

    @Test
    @DisplayName("Validate POST /posts successfully creates a new resource")
    void testPostResourceCreation() {
        String jsonBody = "{\"title\": \"Enterprise QE\", \"body\": \"Automation Track\", \"userId\": 42}";

        given()
            .baseUri("https://jsonplaceholder.typicode.com")
            .contentType("application/json; charset=UTF-8")
            .body(jsonBody)
        .when()
            .post("/posts")
        .then()
            .statusCode(201)
            .body("id", notNullValue())
            .body("title", equalTo("Enterprise QE"));
            
        System.out.println("API Test PASSED: POST /posts resource created successfully.");
    }
}
""",
        "ApiTest.java (REST Assured API Test Suite)"
    )

    # ----------------------------------------------------
    add_h1("Chapter 4: Phase 3 - DevOps Quality Gates, Environment Management & Performance Engineering")
    # ----------------------------------------------------
    add_body("Phase 3 integrates automated quality gates into CI/CD pipelines (GitHub Actions, Azure DevOps) and establishes performance engineering discipline.")

    add_h2("4.1 Pipeline Quality Gate Architecture")
    add_body("Quality gates act as automated circuit breakers in continuous delivery pipelines. If code quality, test pass rates, code coverage, or response time thresholds are breached, artifact promotion is immediately halted.")

    add_code_snippet(
        """package enterprise.qe.gates;

/**
 * Programmatic Enterprise Release Quality Gate Evaluator
 */
public class ReleaseQualityGate {

    public static boolean isReleaseReady(int failedTests, double coveragePercentage, int criticalBugs, double avgResponseTimeMs) {
        if (failedTests > 0) {
            System.out.println("Gate Failed: Outstanding test failures detected.");
            return false;
        }
        if (coveragePercentage < 80.0) {
            System.out.println("Gate Failed: Test coverage below enterprise minimum (80%).");
            return false;
        }
        if (criticalBugs > 0) {
            System.out.println("Gate Failed: Unresolved critical defects present.");
            return false;
        }
        if (avgResponseTimeMs > 2000.0) {
            System.out.println("Gate Failed: Response time SLA breached (>2000ms).");
            return false;
        }
        System.out.println("Gate PASSED: Release candidate meets all quality criteria.");
        return true;
    }

    public static void main(String[] args) {
        boolean ready = isReleaseReady(0, 85.5, 0, 1450.0);
        System.out.println("Deployment Approved: " + ready);
    }
}
""",
        "ReleaseQualityGate.java (Java Quality Gate Engine)"
    )

    add_h2("4.2 API Performance Engineering with Locust (Python)")
    add_body("Performance testing verifies system scalability, throughput, and latency under heavy concurrent user load.")

    add_code_snippet(
        """from locust import HttpUser, task, between

class EnterpriseApiUser(HttpUser):
    wait_time = between(1, 2)  # Think time between user requests

    @task(2)
    def get_post_details(self):
        # Simulate high-frequency read traffic
        self.client.get("/posts/1", name="/posts/[id]")

    @task(1)
    def create_new_record(self):
        # Simulate write/creation transaction load
        payload = {
            "title": "Enterprise Load Test",
            "body": "Performance validation under concurrency",
            "userId": 99
        }
        headers = {"Content-Type": "application/json; charset=UTF-8"}
        self.client.post("/posts", json=payload, headers=headers, name="/posts (Create)")
""",
        "api_performance_test.py (Locust Load Testing)"
    )

    # ----------------------------------------------------
    add_h1("Chapter 5: Phase 4 - Advanced AI Governance Architecture")
    # ----------------------------------------------------
    add_body("The bleeding edge of enterprise QA leadership requires mastering advanced governance architectures that make automated AI decisions defensible and reliable.")

    add_h2("5.1 Trust Architecture & Explainability Audit Logs")
    add_body("When an enterprise AI pipeline automatically blocks a deployment or synthesizes compliance data, corporate boards, internal auditors, and external regulators demand absolute explainability. Trust Architecture mandates that every AI-driven gate decision produces an immutable audit record containing:")
    add_bullet("Exact model identifier and prompt hash used during evaluation.", "Model Provenance: ")
    add_bullet("The precise risk rubric, coverage threshold, or safety boundary applied.", "Rubric & Thresholds: ")
    add_bullet("Granular reasoning explaining why an artifact was approved or rejected.", "Explainability Trail: ")

    add_h2("5.2 LLM-as-a-Judge Evaluation Pattern")
    add_body("Traditional programmatic assertions (`assertEquals`, `regex match`) fail when evaluating unstructured AI outputs (e.g., conversational assistant responses, dynamic JSON microservice payloads). The 'LLM-as-a-Judge' architectural pattern deploys a robust foundational model as a programmatic test assertion.")

    add_code_snippet(
        """import json

class LLMJudgeEvaluator:
    \"\"\"
    Implements the 'LLM-as-a-Judge' architectural pattern and 'Trust Architecture'
    governance logging for evaluating complex system outputs against enterprise risk rubrics.
    \"\"\"
    def __init__(self, model_identifier: str = "enterprise-eval-llm-v2"):
        self.model_identifier = model_identifier

    def evaluate_output(self, system_output: str, risk_rubric: dict) -> dict:
        print(f"[{self.model_identifier}] Evaluating system output against enterprise risk rubric...")
        
        score = 100
        violations = []

        if "error" in system_output.lower() and not risk_rubric.get("allow_errors", False):
            score -= 40
            violations.append("Uncaught error or exception terminology detected in output.")

        if len(system_output) < risk_rubric.get("min_length", 10):
            score -= 30
            violations.append("Output fails minimum length and detail threshold.")

        passed = score >= risk_rubric.get("passing_threshold", 80)

        # Trust Architecture Audit Log Record
        audit_record = {
            "evaluator_model": self.model_identifier,
            "input_sample": system_output[:120],
            "rubric_applied": risk_rubric,
            "calculated_score": score,
            "gate_passed": passed,
            "explainability_reasoning": violations if violations else ["Output successfully complies with all safety and quality boundaries."]
        }
        return audit_record

if __name__ == "__main__":
    print("=== LLM-as-a-Judge & Trust Architecture Enterprise Harness ===")
    
    judge = LLMJudgeEvaluator()
    rubric = {"passing_threshold": 80, "min_length": 15, "allow_errors": False}

    output_pass = "Welcome to enterprise support. Your request #9021 has been successfully processed and verified."
    result1 = judge.evaluate_output(output_pass, rubric)
    print("Evaluation 1 Report:\\n", json.dumps(result1, indent=2))
    print("-" * 60)

    output_fail = "Internal Server Error 500."
    result2 = judge.evaluate_output(output_fail, rubric)
    print("Evaluation 2 Report:\\n", json.dumps(result2, indent=2))
    print("-" * 60)
""",
        "llm_judge_evaluator.py (LLM-as-a-Judge Harness)"
    )

    add_h2("5.3 Shift-Right Integration & Production Telemetry")
    add_body("Traditional testing stops at pre-production staging. Shift-Right integration extends quality validation directly into live production environments using OpenTelemetry, synthetic canary testing, real-time error budget tracking, and automated feedback loops that convert production incidents into regression test suites.")

    # ----------------------------------------------------
    add_h1("Chapter 6: Real-World Enterprise Cloud Topologies (Azure, AWS, OpenClaw)")
    # ----------------------------------------------------
    add_body("To succeed in interviews and executive leadership at companies like Verizon, Trimble, CIBC, and Palo Alto Networks, engineering managers must understand how cloud ecosystems implement these exact patterns in production:")

    add_h2("6.1 Microsoft Azure AI Ecosystem")
    add_bullet("Deploying Azure OpenAI Service (GPT-4o) behind private virtual network endpoints. This ensures zero data leakage while allowing enterprise QE teams to synthesize synthetic test data, generate automated unit tests, and execute LLM-as-a-Judge evaluations securely within corporate compliance boundaries.", "Azure OpenAI & Private Endpoints: ")
    add_bullet("Automating infrastructure provisioning, test runners, and performance test nodes using Azure Container Instances and Azure Pipelines.", "Azure DevOps & Containerization: ")

    add_h2("6.2 Amazon Web Services (AWS) Bedrock & Serverless QA")
    add_bullet("Leveraging Amazon Bedrock for cross-region model inference, choosing optimal foundational models (Anthropic Claude 3.5 Sonnet) for test orchestration and automated code review.", "AWS Bedrock & Multi-Model Inference: ")
    add_bullet("Executing serverless test workers using AWS Lambda and ECS Fargate to scale out distributed test execution across thousands of parallel threads without managing infrastructure.", "Serverless Test Infrastructure: ")

    add_h2("6.3 Agentic Tooling & OpenClaw Frameworks")
    add_body("Modern engineering organizations utilize custom Python agentic frameworks (often integrating open-source agent runtimes like OpenClaw) to create autonomous QE co-pilots that continuously monitor code repositories, triage flaky tests, automatically open Jira bug tickets with full reproduction steps, and verify pull request compliance.")

    # ----------------------------------------------------
    add_h1("Chapter 7: Executive QE Leadership, Cultural Transformation & Metrics")
    # ----------------------------------------------------
    add_body("Technical mastery must be paired with executive leadership, stakeholder management, and team coaching.")

    add_h2("7.1 The Automation-First Culture & Developer-Owned Quality")
    add_body("Senior managers drive a culture where quality is a shared engineering responsibility. Developers own unit and integration tests, while QE leadership focuses on E2E strategy, performance architecture, governance, and coaching.")

    add_h2("7.2 Stakeholder Communication & Executive Dashboards")
    add_body("Communicating technical risk to business leaders requires translating flaky tests and coverage percentages into business impact, risk mitigation metrics, and ROI trends.")

    add_callout(
        "By mastering Python, Java, TypeScript, Playwright, Locust, CI/CD DevOps pipelines, Trust Architecture, and LLM-as-a-Judge governance, you possess the complete blueprint for Senior QA Engineering Management leadership.",
        "MASTER STUDY GUIDE CONCLUSION"
    )

    output_path = os.path.abspath("AI_Enterprise_QA_Master_Study_Guide.docx")
    doc.save(output_path)
    print(f"Extended master study guide successfully created at: {output_path}")
    return output_path

if __name__ == "__main__":
    create_extended_study_guide()
