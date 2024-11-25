import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.fixture(autouse=True)
def login_in_page():
    # Initialize Playwright and open a browser
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        
        user = "standard_user"
        password = "secret_sauce"
        
        page.goto("https://www.saucedemo.com/")
        page.locator("[data-test=\"username\"]").click()
        page.locator("[data-test=\"username\"]").fill(user)
        page.locator("[data-test=\"password\"]").click()
        page.locator("[data-test=\"password\"]").fill(password)
        page.locator("[data-test=\"login-button\"]").click()
        
        yield page 

        # Teardown
        browser.close()
        playwright.stop()

def test_visit_homepage(login_in_page):
    expect(login_in_page).to_have_title("Swag Labs")

# def test_check_homepage_text(shared_page):
#     # Reuses the same page object from the previous test
#     assert "Example Domain" in shared_page.content()