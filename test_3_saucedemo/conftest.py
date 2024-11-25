from playwright.sync_api import Browser
import pytest

@pytest.fixture(scope="session")
def login_in_page(browser: Browser):
    context = browser.new_context()
    context.set_default_timeout(10000)
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
    page.close()
