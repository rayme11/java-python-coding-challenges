package enterprise.qe.web;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import io.github.bonigarcia.wdm.WebDriverManager;

/**
 * Web Automation Example - Real Selenium WebDriver with Chrome.
 * Opens a VISIBLE Chrome browser window (not headless).
 * Tests against Heroku test app: https://the-internet.herokuapp.com/
 * ChromeDriver is auto-downloaded and managed by WebDriverManager.
 */
public class WebAutomationExample {
    public static void main(String[] args) {
        WebDriver driver = null;
        try {
            // Auto-download ChromeDriver matching installed Chrome version
            WebDriverManager.chromedriver().browserVersion("155").setup();

            ChromeOptions options = new ChromeOptions();
            // NOTE: No --headless argument - browser opens visibly on your screen
            options.addArguments("--no-sandbox");
            options.addArguments("--disable-dev-shm-usage");
            options.addArguments("--disable-gpu");
            options.addArguments("--window-size=1920,1080");
            options.addArguments("--start-maximized");

            System.out.println("Launching real Chrome browser...");
            driver = new ChromeDriver(options);

            System.out.println("Navigating to Heroku test app: https://the-internet.herokuapp.com/login");
            driver.get("https://the-internet.herokuapp.com/login");

            // Enter username
            WebElement usernameField = driver.findElement(By.id("username"));
            usernameField.sendKeys("tomsmith");

            // Enter password
            WebElement passwordField = driver.findElement(By.id("password"));
            passwordField.sendKeys("SuperSecretPassword!");

            // Click login button
            WebElement loginButton = driver.findElement(By.cssSelector("button.radius"));
            loginButton.click();

            // Verify successful login
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
