package enterprise.qe.web;

import com.microsoft.playwright.*;
import com.microsoft.playwright.options.AriaRole;

/**
 * Playwright Web Automation Example - Real Browser with Playwright Java.
 * Opens VISIBLE Chromium browser (not headless).
 * Tests against Heroku test app: https://the-internet.herokuapp.com/
 */
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

            // Fill username
            page.fill("#username", "tomsmith");
            System.out.println("Entered username: tomsmith");

            // Fill password
            page.fill("#password", "SuperSecretPassword!");
            System.out.println("Entered password");

            // Click login button
            page.click("button.radius");
            System.out.println("Clicked login button");

            // Wait for flash message
            page.waitForSelector("#flash");

            // Verify successful login
            String flashText = page.textContent("#flash");
            System.out.println("Flash message: " + flashText);

            String currentUrl = page.url();
            System.out.println("Current URL: " + currentUrl);

            if (flashText.contains("You logged into a secure area!")) {
                System.out.println("Test PASSED: Successfully logged into Heroku test app with Playwright");
            } else {
                System.out.println("Test FAILED: Login did not succeed");
            }

            // Keep browser open for 5 seconds so you can see it
            System.out.println("Keeping browser open for 5 seconds...");
            page.waitForTimeout(5000);

            browser.close();
            System.out.println("Browser session closed.");
        } catch (Exception e) {
            System.err.println("Test ERROR: " + e.getMessage());
        }
    }
}
