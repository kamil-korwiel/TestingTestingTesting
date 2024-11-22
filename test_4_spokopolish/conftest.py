from playwright.async_api import async_playwright, Browser, BrowserContext
import pytest_asyncio
import pytest


@pytest.fixture(scope='session')
async def browser():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        yield browser
        await browser.close()
        
@pytest.fixture(scope='class')
async def context(browser:Browser):
    context = await browser.new_context()
    context.set_default_timeout(5000)
    yield context
    await context.close()

@pytest.fixture(scope='class')
async def page_spokopolish(context:BrowserContext):
    await context.clear_cookies()
    page = await context.new_page()
    await page.goto("https://spokopolish.pl/")
    yield page
    print("class - close")
    await page.close()