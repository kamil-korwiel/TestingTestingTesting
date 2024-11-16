from playwright.async_api import async_playwright
import pytest_asyncio


@pytest_asyncio.fixture(scope='session')
async def login_in_page():
    # Initialize Playwright and open a browser
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        context = await browser.new_context()
        context.set_default_timeout(10000)
        page = await context.new_page()
        
        user = "standard_user"
        password = "secret_sauce"
        
        await page.goto("https://www.saucedemo.com/")
        await page.locator("[data-test=\"username\"]").click()
        await page.locator("[data-test=\"username\"]").fill(user)
        await page.locator("[data-test=\"password\"]").click()
        await page.locator("[data-test=\"password\"]").fill(password)
        await page.locator("[data-test=\"login-button\"]").click()
        
        yield page
        # Teardown
        await browser.close()