from playwright.async_api import async_playwright, Browser, BrowserContext
import pytest_asyncio
import pytest


@pytest.fixture(scope='session')
async def browser():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        yield browser
        await browser.close()
        
@pytest.fixture(scope='session')
async def context(browser:Browser):
    context = await browser.new_context()
    yield context

@pytest.fixture(scope='module')
async def page_spokopolish(context:BrowserContext):
    page = await context.new_page()
    await page.goto("https://spokopolish.pl/")
    yield page