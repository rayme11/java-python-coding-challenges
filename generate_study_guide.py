import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def create_study_guide():
    doc = Document()
    
    # Page setup - 1 inch margins
    sections = doc.sections
    for section in sections:
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
        run.font.size = Pt(24)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D) # Navy
        p.paragraph_format.space_after = Pt(6)
        return p

    def add_subtitle(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(text)
        run.font.name = 'Arial'
        run.font.size = Pt(14)
        run.font.italic = True
        run.font.color.rgb = RGBColor(0x5C, 0x76, 0x8D) # Slate Grey
        p.paragraph_format.space_after = Pt(24)
        return p

    def add_h1(text):
        p = doc.add_paragraph()
        run = p.add_run(text)
        run.font.name = 'Arial'
        run.font.size = Pt(18)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(6)
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        run = p.add_run(text)
        run.font.name = 'Arial'
        run.font.size = Pt(14)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x41, 0x74, 0x8D) # Steel Blue
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        return p

    def add_h3(text):
        p = doc.add_paragraph()
        run = p.add_run(text)
        run.font.name = 'Arial'
        run.font.size = Pt(12)
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

    def add_callout(text, title="KEY ENTERPRISE TAKEAWAY"):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = table.cell(0, 0)
        cell.width = Inches(6.5)
        
        # Background shading (light blue-grey)
        shading = parse_xml(r'<w:shd {} w:fill="F4F6F9"/>'.format(nsdecls('w')))
        cell._tc.get_or_add_tcPr().append(shading)
        
        # Left thick border (Navy)
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

    def add_code_snippet(code_text, caption="Code Example"):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = table.cell(0, 0)
        cell.width = Inches(6.5)
        
        # Dark charcoal background for code
        shading = parse_xml(r'<w:shd {} w:fill="2D3748"/>'.format(nsdecls('w')))
        cell._tc.get_or_add_tcPr().append(shading)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
        r_cap = p.add_run(f"💻 {caption}\n")
        r_cap.font.name = 'Courier New'
        r_cap.font.size = Pt(9)
        r_cap.font.bold = True
        r_cap.font.color.rgb = RGBColor(0xA0, 0xAE, 0xC0) # Light grey
        
        p2 = cell.add_paragraph()
        p2.paragraph_format.space_before = Pt(2)
        p2.paragraph_format.space_after = Pt(6)
        r_code = p2.add_run(code_text)
        r_code.font.name = 'Consolas'
        r_code.font.size = Pt(9.5)
        r_code.font.color.rgb = RGBColor(0xE2, 0xE8, 0xF0) # Off white
        
        doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # --- DOCUMENT CONTENT GENERATION ---

    add_title("AI-Enhanced Enterprise Quality Engineering & Governance")
    add_subtitle("Comprehensive Master Study Guide for Senior QA Engineering Managers\n(Aligned with Verizon, Trimble, Palo Alto Networks, and CIBC Leadership Standards)")

    add_callout(
        "This master study guide bridges hands-on multi-language test automation (Java, Python, TypeScript), scalable web/API frameworks (Selenium, Playwright, REST Assured), DevOps quality gates, and advanced AI governance frameworks (LLM-as-a-Judge, Trust Architecture, Shift-Right). Designed for senior engineering leaders.",
        "EXECUTIVE SUMMARY"
    )

    # SECTION 1
    add_h1("1. Executive Overview & Industry Context")
    add_body("Modern enterprise quality engineering has evolved far beyond traditional functional scripting. As organizations scale microservices, mobile apps, and cloud infrastructure, leaders face the 'AI Paradox in QA'—where high AI adoption and massive test case generation coexist with rising software defect rates due to a lack of governance and contextual test validation.")
    add_body("To succeed in senior roles at telecom, IoT, and cloud giants (such as Verizon and Palo Alto Networks), engineering managers must architect resilient automation pipelines, enforce rigorous CI/CD quality gates, and implement defensible AI Trust Architectures.")

    add_h2("Core Competency Matrix")
    add_bullet("Lead enterprise automation strategy across Web, API, and Mobile ecosystems.", "Strategy & Vision: ")
    add_bullet("Deploy Playwright (TypeScript/Python) and Selenium with Page Object Model (POM) patterns.", "Framework Engineering: ")
    add_bullet("Integrate AI/ML tooling for test case scaffolding, data synthesis, and defect prediction.", "AI Integration: ")
    add_bullet("Build MCP servers and LLM agent integrations connecting internal systems (Jira, GitHub, TestRail).", "Agentic Tooling: ")
    add_bullet("Enforce pipeline quality gates, performance SLOs (Locust/JMeter), and board-level governance.", "Governance & DevOps: ")

    # SECTION 2
    add_h1("2. Phase 1: AI Foundations, Developer AI Tools & Agentic Integrations")
    add_body("Phase 1 establishes the theoretical and practical foundation of AI in QE. Rather than viewing AI as a black box, senior managers learn to orchestrate AI agents for test generation, data synthesis, and system integration.")

    add_h2("The AI Paradox & Mitigation Strategies")
    add_body("AI-generated tests often suffer from hallucinations, brittle assertions, and lack of business context. Mitigation requires deterministic quality gates, semantic coverage analysis, and Human-in-the-Loop (HIL) validation.")

    add_h2("Hands-on Example: LLM Test Data Generator & Agentic Integration")
    add_body("Below is a production-grade Python script demonstrating how an LLM agent generates test data based on natural language requirements and interacts with a mock internal database system.")
    
    add_code_snippet(
        """import json

def generate_test_user_data(requirements: str) -> dict:
    # Simulates LLM generating test data based on natural language
    print(f"LLM Processing Requirements: '{requirements}'")
    
    mock_data = {
        "valid_user": {"firstName": "John", "email": "john.doe@example.com", "age": 30},
        "invalid_email_user": {"firstName": "Jane", "email": "invalid-email", "age": 25},
        "minor_user": {"firstName": "Alice", "email": "alice@example.com", "age": 16}
    }
    
    if "invalid email" in requirements.lower():
        return mock_data["invalid_email_user"]
    elif "minor" in requirements.lower():
        return mock_data["minor_user"]
    else:
        return mock_data["valid_user"]

def mock_save_user_to_db(user_data: dict) -> bool:
    # Simulates internal system integration (MCP / DB API)
    if "@" in user_data.get("email", ""):
        print("Internal System: User saved successfully.")
        return True
    print("Internal System: Validation failed.")
        return False
""",
        "Python LLM Agent Test Data Generator"
    )

    # SECTION 3
    add_h1("3. Phase 2: Scalable Web, API & Mobile Test Engineering")
    add_body("Phase 2 covers robust framework engineering across Java and TypeScript, interacting with real external test applications (Heroku The-Internet and JSONPlaceholder APIs).")

    add_h2("Selenium vs. Playwright Comparison")
    add_bullet("JSON Wire Protocol / W3C WebDriver. Requires explicit waits and WebDriverManager.", "Selenium WebDriver: ")
    add_bullet("Modern WebSocket protocol, automatic waiting, multi-context browser isolation, and native mobile emulation.", "Playwright (TypeScript / Python / Java): ")

    add_h2("TypeScript Playwright Page Object Model (POM)")
    add_body("Enterprise test suites mandate clean separation of concerns using POM. Here is the TypeScript implementation used in our training framework:")

    add_code_snippet(
        """import { Page, Locator } from '@playwright/test';

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
}""",
        "TypeScript Playwright Page Object Model (LoginPage.ts)"
    )

    add_h2("API Testing with REST Assured (Java)")
    add_body("Enterprise backend validation requires contract validation, schema checks, and robust status assertions:")
    
    add_code_snippet(
        """package enterprise.qe.api;

import org.junit.jupiter.api.Test;
import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

public class ApiTest {
    @Test
    void testGetPostValidatesSuccessfully() {
        given()
            .baseUri("https://jsonplaceholder.typicode.com")
        .when()
            .get("/posts/1")
        .then()
            .statusCode(200)
            .body("id", equalTo(1))
            .body("title", notNullValue());
    }
}""",
        "REST Assured API Test (ApiTest.java)"
    )

    # SECTION 4
    add_h1("4. Phase 3: DevOps, CI/CD, Performance & Governance Integration")
    add_body("Engineering managers must enforce quality gates in pipelines (GitHub Actions, Azure DevOps, AWS CodePipeline) and establish performance SLAs.")

    add_h2("Pipeline Quality Gate Engine (Java)")
    add_body("A programmatic gate evaluating test execution results, coverage thresholds, and response time SLAs before artifact promotion:")

    add_code_snippet(
        """package enterprise.qe.gates;

public class ReleaseQualityGate {
    public static boolean isReleaseReady(int failedTests, double coverage, int criticalBugs, double avgResponseTime) {
        if (failedTests > 0) return false;
        if (coverage < 80.0) return false;
        if (criticalBugs > 0) return false;
        if (avgResponseTime > 2000) return false;
        return true;
    }
}""",
        "ReleaseQualityGate.java"
    )

    add_h2("Performance Testing with Locust (Python)")
    add_body("Simulating concurrent user load against microservices in pre-prod or CI/CD environments:")

    add_code_snippet(
        """from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_posts(self):
        self.client.get("/posts/1", name="/posts/[id]")

    @task(3)
    def create_post(self):
        payload = {"title": "load-test", "body": "test-body", "userId": 1}
        self.client.post("/posts", json=payload)""",
        "Locust API Performance Test (api_performance_test.py)"
    )

    # SECTION 5
    add_h1("5. Phase 4: Advanced AI Governance Architecture")
    add_body("The cutting edge of enterprise QA leadership requires mastering three pivotal architectural patterns:")

    add_h2("Trust Architecture & Explainability Logs")
    add_body("Corporate boards and regulators require that automated AI pipeline decisions are defensible. Trust Architecture mandates structured audit logs containing model versions, rubrics, input context, and confidence scores.")

    add_h2("LLM-as-a-Judge Evaluation Harness")
    add_body("When testing unstructured AI outputs (e.g., chat assistants, dynamic JSON payloads), traditional assertions fail. We use a foundational model as a programmatic test judge:")

    add_code_snippet(
        """import json

class LLMJudgeEvaluator:
    def evaluate_output(self, system_output: str, risk_rubric: dict) -> dict:
        score = 100
        violations = []
        if "error" in system_output.lower() and not risk_rubric.get("allow_errors", False):
            score -= 40
            violations.append("Uncaught error terminology detected.")
            
        passed = score >= risk_rubric.get("passing_threshold", 70)
        return {
            "score": score,
            "passed": passed,
            "explainability_reasoning": violations if violations else ["Passed safety & quality boundaries."]
        }""",
        "LLM-as-a-Judge Evaluator (llm_judge_evaluator.py)"
    )

    add_h2("Shift-Right Integration & Production Telemetry")
    add_body("Moving beyond staging by integrating automated synthetic canary tests and APM telemetry feedback loops directly into production environments.")

    # SECTION 6
    add_h1("6. Real-World Enterprise Blueprint: Azure, AWS & Agentic Tooling")
    add_body("How Fortune 500 engineering organizations (Verizon, Trimble, CIBC) apply these exact patterns in production today:")

    add_bullet("Deploying Azure OpenAI Service (GPT-4o) behind enterprise private endpoints for test data synthesis and LLM-as-a-Judge validation pipelines.", "Microsoft Azure AI Ecosystem: ")
    add_bullet("Leveraging Amazon Bedrock with Anthropic Claude for secure, cross-region LLM agent integrations and test orchestration.", "AWS Bedrock & Cloud Testing: ")
    add_bullet("Using agentic frameworks (custom Python agents and Model Context Protocol servers) to securely connect LLM agents to internal Jira, GitHub, and CI/CD pipelines.", "Agentic Tooling & MCP Servers: ")

    add_callout(
        "By mastering these frameworks—spanning Python, Java, TypeScript, Playwright, Locust performance testing, and advanced AI Governance—you are fully prepared for senior QA engineering management roles.",
        "READY FOR LEADERSHIP"
    )

    output_path = os.path.abspath("AI_Enterprise_QA_Master_Study_Guide.docx")
    doc.save(output_path)
    print(f"Study guide successfully created at: {output_path}")
    return output_path

if __name__ == "__main__":
    create_study_guide()
