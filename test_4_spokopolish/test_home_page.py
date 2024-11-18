from playwright.async_api import Page, expect
import pytest

@pytest.mark.usefixtures("page_spokopolish")
@pytest.mark.asyncio(loop_scope="session")
class TestCookies():
    
    async def test_privacy_popup(self,page_spokopolish: Page):
        await expect(page_spokopolish.get_by_role("heading", name="We value your privacy")).to_be_visible()
    
    async def test_clicking_reject_all(self,page_spokopolish: Page):
        await page_spokopolish.get_by_role("button", name="Reject All").click()
        await expect(page_spokopolish.get_by_role("heading", name="We value your privacy")).not_to_be_visible()