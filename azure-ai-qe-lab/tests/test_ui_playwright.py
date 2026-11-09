import pytest
from playwright.sync_api import Page, expect

def test_heroku_login_success(page: Page):
    """
    Enterprise UI Test: Verifies secure login flow against Heroku app using Python Playwright.
    """
    print("\n[UI Test Start] Navigating to Heroku login page...")
    page.goto("https://the-internet.herokuapp.com/login")
    
    print("[UI Test Step] Asserting page title...")
    expect(page).to_have_title("The Internet")
    
    print("[UI Test Step] Filling credentials (tomsmith)...")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button.radius")
    
    print("[UI Test Step] Verifying secure area redirect and flash success message...")
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    flash = page.locator("#flash")
    expect(flash).to_contain_text("You logged into a secure area!")
    print("[UI Test PASSED] Heroku login success test completed successfully!\n")

def test_heroku_login_failure(page: Page):
    """
    Enterprise UI Test: Verifies invalid login handling.
    """
    print("\n[UI Test Start] Navigating to Heroku login page for failure test...")
    page.goto("https://the-internet.herokuapp.com/login")
    
    print("[UI Test Step] Entering invalid credentials...")
    page.fill("#username", "wronguser")
    page.fill("#password", "wrongpass")
    page.click("button.radius")
    
    print("[UI Test Step] Verifying invalid username flash error message...")
    flash = page.locator("#flash")
    expect(flash).to_contain_text("Your username is invalid!")
    print("[UI Test PASSED] Heroku login failure test completed successfully!\n")
