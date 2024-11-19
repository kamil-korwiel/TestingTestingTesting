from playwright.async_api import Page, expect, BrowserContext
import pytest
import json


def save(name:str,payload_json:str) -> None:
    with open(f'./{name}.json','w') as file:
        file.write(payload_json)
        
def get_file(name:str) -> dict:
    with open(f'./{name}.json', "r") as f:
        cookie = json.loads(f.read())
        print(type(cookie))
        return cookie

@pytest.mark.usefixtures("page_spokopolish")
@pytest.mark.asyncio(loop_scope="session")
class TestCookies():
    
    async def test_cookie_before(self,page_spokopolish:Page):
        context = page_spokopolish.context
        cookie = await context.cookies()
        save("cookie_before",json.dumps(cookie))
    
    async def test_privacy_popup(self,page_spokopolish: Page):
        await expect(page_spokopolish.get_by_role("heading", name="We value your privacy")).to_be_visible()
    
    # async def test_clicking_reject_all(self,page_spokopolish: Page):
    #     await page_spokopolish.get_by_role("button", name="Reject All").click()
    #     await expect(page_spokopolish.get_by_role("heading", name="We value your privacy")).not_to_be_visible()
        
    async def test_clicking_accept_all(self,page_spokopolish: Page):
        await page_spokopolish.get_by_role("button", name="Accept All").click()
        await expect(page_spokopolish.get_by_role("heading", name="We value your privacy")).not_to_be_visible()
        
    async def test_cookie_after(self,page_spokopolish:Page):
        context = page_spokopolish.context
        cookie = await context.cookies()
        
        print(type(cookie))
        cookie_after_dict = cookie[0]
        print(type(cookie_after_dict))
        cookie_before_dict = get_file('cookie_before')[0]
        print(type(cookie_before_dict))
        
        assert cookie_after_dict == cookie_before_dict
