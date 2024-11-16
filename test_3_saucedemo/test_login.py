from playwright.async_api import Page, async_playwright, expect
import pytest
import pytest_asyncio

async def login(page: Page, user: str, password: str):
    await page.goto("https://www.saucedemo.com/")
    await page.locator("[data-test=\"username\"]").click()
    await page.locator("[data-test=\"username\"]").fill(user)
    await page.locator("[data-test=\"password\"]").click()
    await page.locator("[data-test=\"password\"]").fill(password)
    await page.locator("[data-test=\"login-button\"]").click()

@pytest.mark.asyncio
async def test_correct_login_in(page: Page):
    await login(page, "standard_user", "secret_sauce")
    assert "https://www.saucedemo.com/inventory.html" == page.url
    await expect(page.locator("[data-test=\"inventory-list\"]")).to_be_visible()

@pytest.mark.asyncio
async def test_incorrect_login(page: Page):
    await login(page, "incorrect_user", "secret_sauce")
    assert "https://www.saucedemo.com/" == page.url
    await expect(page.locator("[data-test=\"error\"]")).to_contain_text(
        "Epic sadface: Username and password do not match any user in this service"
    )

@pytest.mark.asyncio
async def test_locked_user_login(page: Page):
    await login(page, "locked_out_user", "secret_sauce")
    await expect(page.locator("[data-test=\"error\"]")).to_contain_text(
        "Epic sadface: Sorry, this user has been locked out."
    )

# Async page fixture using pytest-asyncio
@pytest_asyncio.fixture
async def page():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        yield page
        await context.close()
        await browser.close()
    