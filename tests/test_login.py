import pytest
from playwright.sync_api import sync_playwright


def test_login_successful(page):
    page.fill("#login-container input[placeholder='Email']", "john.doe@example.com")
    page.fill("#login-container input[placeholder='Password']", "P@ssw0rd123")
    page.click("#login-container button")
    # Assert the login is successful, for example, by checking the page title or a success message
    assert "Success" in page.title


def test_login_invalid_email(page):
    page.fill("#login-container input[placeholder='Email']", "invalid_email_format")
    page.fill("#login-container input[placeholder='Password']", "short")
    page.click("#login-container button")
    # Assert the page displays an error, for example, by checking for error messages
    assert "Invalid Email format" in page.locator("#error-message").inner_text


def test_login_empty_email(page):
    page.fill("#login-container input[placeholder='Email']", "")
    page.fill("#login-container input[placeholder='Password']", "noemail@123")
    page.click("#login-container button")
    # Assert the page displays an error, for example, by checking for error messages
    assert "Email is required" in page.locator("#error-message").inner_text


def test_login_empty_password(page):
    page.fill("#login-container input[placeholder='Email']", "harry.potter@hogwarts.edu")
    page.fill("#login-container input[placeholder='Password']", "")
    page.click("#login-container button")
    # Assert the page displays an error, for example, by checking for error messages
    assert "Password is required" in page.locator("#error-message").inner_text


def test_login_multiple_entries(page):
    page.fill("#login-container input[placeholder='Email']", "john.doe@example.com")
    page.fill("#login-container input[placeholder='Password']", "P@ssw0rd123")
    page.click("#login-container button")

    #ERROR HANDLING: Invalid input
    #Tests that the login form does not accept invalid input
    page.fill("#login-container input[placeholder='Email']", "invalid_email@example.com")
    page.fill("#login-container input[placeholder='Password']", "short_pass")
    page.click("#login-container button")
    assert "Invalid input" in page.locator("#error-message").inner_text


# Helper function to launch the browser
def launch_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("file:///path/to/login.html")  # Replace with your HTML file path
        yield page
        browser.close()

# Run tests using pytest
# pytest --browser-type=chromium --headless -v test_login.py
# Make sure you replace "file:///path/to/login.html" with the absolute path to your html file
# This assumes the login.html file is available locally
# Replace this placeholder with the actual path to login.html
# Make sure to use pytest --browser-type=chromium to correctly use playwright
