import pytest
from playwright.sync_api import Page, expect

def test_heroku_login_success(page: Page):
    """
    Enterprise UI Test: Verifies secure login flow against Heroku app using Python Playwright.
    """
    page.goto("https://the-internet.herokuapp.com/login")
    
    # Assert page title
    expect(page).to_have_title("The Internet")
    
    # Fill credentials
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button.radius")
    
    # Assert secure area redirect and flash message
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    flash = page.locator("#flash")
    expect(flash).to_contain_text("You logged into a secure area!")

def test_heroku_login_failure(page: Page):
    """
    Enterprise UI Test: Verifies invalid login handling.
    """
    page.goto("https://the-internet.herokuapp.com/login")
    
    page.fill("#username", "wronguser")
    page.fill("#password", "wrongpass")
    page.click("button.radius")
    
    flash = page.locator("#flash")
    expect(flash).to_contain_text("Your username is invalid!")
