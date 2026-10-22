import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';

test.describe('Heroku Login Feature (TypeScript Playwright)', () => {

  test('should login successfully with valid credentials', async ({ page }) => {
    const loginPage = new LoginPage(page);

    await loginPage.goto();
    await loginPage.login('tomsmith', 'SuperSecretPassword!');

    // Verify successful login
    await expect(loginPage.flashMessage).toContainText('You logged into a secure area!');
    await expect(page).toHaveURL(/.*\/secure/);
  });

  test('should fail login with invalid credentials', async ({ page }) => {
    const loginPage = new LoginPage(page);

    await loginPage.goto();
    await loginPage.login('wronguser', 'wrongpassword');

    // Verify error message
    await expect(loginPage.flashMessage).toContainText('Your username is invalid!');
  });

});
