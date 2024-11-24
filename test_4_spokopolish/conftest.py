# from playwright.async_api import async_playwright, Browser, BrowserContext
from playwright.sync_api import sync_playwright, Browser, BrowserContext

# import pytest_asyncio
import pytest

# ### async
# @pytest.fixture(scope='session')
# async def browser_async():
#     async with async_playwright() as playwright:
#         browser = await playwright.chromium.launch()
#         yield browser
#         await browser.close()
        
# @pytest.fixture(scope='class')
# async def context_async(browser_async:Browser):
#     context = await browser_async.new_context()
#     context.set_default_timeout(5000)
#     yield context
#     await context.close()

# @pytest.fixture(scope='class')
# async def page_spokopolish_async(context_async:BrowserContext):
#     await context_async.clear_cookies()
#     page = await context_async.new_page()
#     await page.goto("https://spokopolish.pl/")
#     yield page
#     print("class - close")
#     await page.close()
    
    
### sync

@pytest.fixture(scope='class')
def page_spokopolish():
    with sync_playwright() as playwright:
        
        browser = playwright.chromium.launch()
        
        context = browser.new_context()
        context.set_default_timeout(5000)
        
        page = context.new_page()
        page.goto("https://spokopolish.pl/")
        
        yield page
        
        page.close()
        context.close()
        browser.close()