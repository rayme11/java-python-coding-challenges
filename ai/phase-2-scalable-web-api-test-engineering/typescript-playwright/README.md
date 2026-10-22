# Enterprise TypeScript & Playwright Test Automation Framework

## Overview

This module provides a production-grade, enterprise-ready **Playwright with TypeScript** test automation framework adhering directly to the preferred qualifications for Senior QA Automation Manager roles (e.g., Verizon, enterprise tech stacks).

## Project Structure

```
typescript-playwright/
├── package.json          # Node.js dependencies & scripts (@playwright/test, typescript)
├── tsconfig.json         # TypeScript compiler configuration
├── playwright.config.ts  # Playwright global configuration (base URL, headed/headless, reporters)
├── pages/
│   └── LoginPage.ts      # Page Object Model (POM) for login feature
└── tests/
    └── login.spec.ts     # Playwright test specs using POM and assertions
```

## Key Enterprise Practices Demonstrated

1. **Page Object Model (POM):** Separation of test logic from page locators and interaction methods (`LoginPage.ts`).
2. **Strict TypeScript Typing:** Full type safety for page elements, methods, and test fixtures.
3. **Robust Assertions:** Built-in Playwright assertions with auto-retrying (`expect(locator).toContainText(...)`).
4. **Configuration Management:** Centralized configuration in `playwright.config.ts` supporting parallel execution, tracing, video recording on failure, and HTML reporting.

## How to Run (When Node.js is installed)

1. Install dependencies:
   ```bash
   npm install
   ```
2. Install Playwright browsers:
   ```bash
   npx playwright install
   ```
3. Run tests in headed browser mode:
   ```bash
   npm run test:headed
   ```
4. Run tests with Playwright UI:
   ```bash
   npm run test:ui
   ```
