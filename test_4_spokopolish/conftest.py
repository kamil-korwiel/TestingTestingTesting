# from playwright.async_api import async_playwright, Browser, BrowserContext ,Page
from playwright.sync_api import Browser
import pytest

@pytest.fixture(scope='class',autouse=True)
def page_spokopolish(browser: Browser):
    context = browser.new_context()
    context.set_default_timeout(50000)
    page = context.new_page()
    page.goto("https://spokopolish.pl/")
    yield page
    page.close()
    
    
