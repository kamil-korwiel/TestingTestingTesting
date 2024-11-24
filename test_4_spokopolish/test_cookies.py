from playwright.async_api import Page, expect, BrowserContext
import pytest
import json


def save(name:str,payload_json:str) -> None:
    with open(f'./{name}.json','w') as file:
        file.write(payload_json)
        
def get_file(name:str) -> dict:
    with open(f'./{name}.json', "r") as f:
        cookie = json.loads(f.read())
        return cookie
    
async def find_cookie(name:str,  cookies:list[dict]) -> dict:
    for coo in cookies:
        if coo["name"] == name:
            return coo
    return None

@pytest.mark.usefixtures("page_spokopolish_async")
@pytest.mark.asyncio(loop_scope="session")
class TestConsentCookieAcceptAll():
    
    async def test_cookie_before(self,page_spokopolish_async:Page):
        context = page_spokopolish_async.context
        cookie = await context.cookies()
        save("test_4_spokopolish/accept_all/cookie_before",json.dumps(cookie))
    
    async def test_privacy_popup(self,page_spokopolish_async: Page):
        await expect(page_spokopolish_async.get_by_role("heading", name="We value your privacy")).to_be_visible()
    
    async def test_clicking_accept_all(self,page_spokopolish_async: Page):
        await page_spokopolish_async.get_by_role("button", name="Accept All").click()
        await expect(page_spokopolish_async.get_by_role("heading", name="We value your privacy")).not_to_be_visible()

    async def test_cookies_after(self,page_spokopolish_async: Page):
        context = page_spokopolish_async.context
        cookies = await context.cookies()
        after = await find_cookie("cookieyes-consent",cookies)
        before = get_file("test_4_spokopolish/accept_all/cookie_before")
        after != before
        

@pytest.mark.usefixtures("page_spokopolish_async")
@pytest.mark.asyncio(loop_scope="session")
class TestConsentCookieRejectAll():
    
    async def test_cookie_before(self,page_spokopolish_async:Page):
        context = page_spokopolish_async.context
        cookie = await context.cookies()
        save("test_4_spokopolish/reject_all/cookie_before",json.dumps(cookie))
    
    async def test_privacy_popup(self,page_spokopolish_async: Page):
        await expect(page_spokopolish_async.get_by_role("heading", name="We value your privacy")).to_be_visible()
    
    async def test_clicking_reject_all(self,page_spokopolish_async: Page):
        await page_spokopolish_async.get_by_role("button", name="Reject All").click()
        await expect(page_spokopolish_async.get_by_role("heading", name="We value your privacy")).not_to_be_visible()
    
    async def test_cookies_after(self,page_spokopolish_async: Page):
        context = page_spokopolish_async.context
        cookies = await context.cookies()
        after = await find_cookie("cookieyes-consent",cookies)
        before = get_file("test_4_spokopolish/reject_all/cookie_before")
        after == before