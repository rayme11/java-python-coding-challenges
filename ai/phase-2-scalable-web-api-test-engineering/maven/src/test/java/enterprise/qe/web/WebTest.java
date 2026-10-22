package enterprise.qe.web;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import io.github.bonigarcia.wdm.WebDriverManager;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Web automation tests using real Selenium WebDriver with Chrome.
 * Opens VISIBLE Chrome browser windows (not headless).
 * Tests against Heroku test app: https://the-internet.herokuapp.com/
 * ChromeDriver is auto-managed by WebDriverManager.
 */
public class WebTest {

    @Test
    @DisplayName("Heroku login page loads correctly (Real Selenium - Visible Browser)")
    void testHerokuLoginPage() {
        WebDriverManager.chromedriver().browserVersion("155").setup();

        ChromeOptions options = new ChromeOptions();
        // No --headless - browser opens visibly
        options.addArguments("--no-sandbox");
        options.addArguments("--disable-dev-shm-usage");
        options.addArguments("--disable-gpu");
        options.addArguments("--window-size=1920,1080");

        WebDriver driver = new ChromeDriver(options);
        try {
            driver.get("https://the-internet.herokuapp.com/login");
            String title = driver.getTitle();
            System.out.println("Page title: " + title);
            assertTrue(title.contains("The Internet"), "Title should contain 'The Internet'");
            System.out.println("Web Test PASSED: Heroku login page loaded with real visible Selenium");

            // Keep browser open briefly so you can see it
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            driver.quit();
        }
    }

    @Test
    @DisplayName("Heroku secure area accessible after login (Real Selenium - Visible Browser)")
    void testHerokuSecureLogin() {
        WebDriverManager.chromedriver().browserVersion("155").setup();

        ChromeOptions options = new ChromeOptions();
        // No --headless - browser opens visibly
        options.addArguments("--no-sandbox");
        options.addArguments("--disable-dev-shm-usage");
        options.addArguments("--disable-gpu");
        options.addArguments("--window-size=1920,1080");

        WebDriver driver = new ChromeDriver(options);
        try {
            driver.get("https://the-internet.herokuapp.com/login");

            org.openqa.selenium.WebElement usernameField = driver.findElement(org.openqa.selenium.By.id("username"));
            usernameField.sendKeys("tomsmith");

            org.openqa.selenium.WebElement passwordField = driver.findElement(org.openqa.selenium.By.id("password"));
            passwordField.sendKeys("SuperSecretPassword!");

            org.openqa.selenium.WebElement loginButton = driver.findElement(org.openqa.selenium.By.cssSelector("button.radius"));
            loginButton.click();

            // Verify secure area login succeeded - check for secure area indicator
            try {
                org.openqa.selenium.WebElement flashMessage = driver.findElement(org.openqa.selenium.By.id("flash"));
                String flashText = flashMessage.getText();
                System.out.println("Flash message: " + flashText);
                assertTrue(flashText.contains("You logged into a secure area!"), "Should show success message");
            } catch (org.openqa.selenium.NoSuchElementException e) {
                // Flash message may have different text/structure; verify secure area by checking URL
                String currentUrl = driver.getCurrentUrl();
                System.out.println("Current URL: " + currentUrl);
                assertTrue(currentUrl.contains("/secure"), "Should be on secure area page after login");
            }
            System.out.println("Web Test PASSED: Heroku secure login verified with real visible Selenium");

            // Keep browser open briefly so you can see it
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            driver.quit();
        }
    }
}
