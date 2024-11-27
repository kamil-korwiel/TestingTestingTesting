from playwright.sync_api import Page,expect
import pytest
import json
import os

PATH_COOKIE_BEFORE_ACCEPT = "test_4_spokopolish/accept_all/cookie_before.json"
PATH_COOKIE_BEFORE_REJECT = "test_4_spokopolish/reject_all/cookie_before.json"
COOKIE_CONSENT_NAME = "cookieyes-consent"


def ensure_that_path_exists(file_path):
    
    folder_path = os.path.dirname(file_path)
    if folder_path and not os.path.isdir(folder_path):
        os.makedirs(folder_path)
    

def save(path:str,payload_json:str) -> None:
    ensure_that_path_exists(path)
    # full_file_name = os.path.basename(file_path)
    with open(f'./{path}','w') as file:
        file.write(payload_json)
        
def get_file(path:str) -> dict:
    with open(f'./{path}', "r") as f:
        cookie = json.loads(f.read())
        return cookie
    
def find_cookie(name:str, cookies:list[dict]) -> dict:
    for coo in cookies:
        if coo["name"] == name:
            return coo
    return None

@pytest.mark.usefixtures("page_spokopolish")
class TestConsentCookieAcceptAll():
    
    def test_cookie_before(self,page_spokopolish:Page):
        context = page_spokopolish.context
        cookie = context.cookies()
        save(PATH_COOKIE_BEFORE_ACCEPT,json.dumps(cookie))
    
    def test_privacy_popup(self,page_spokopolish: Page):
        expect(page_spokopolish.get_by_role("heading", name="We value your privacy")).to_be_visible()
    
    def test_clicking_accept_all(self,page_spokopolish: Page):
        page_spokopolish.get_by_role("button", name="Accept All").click()
        expect(page_spokopolish.get_by_role("heading", name="We value your privacy")).not_to_be_visible()

    def test_cookies_after(self,page_spokopolish: Page):
        context = page_spokopolish.context
        cookies = context.cookies()
        after = find_cookie(COOKIE_CONSENT_NAME,cookies)
        before = get_file(PATH_COOKIE_BEFORE_ACCEPT)
        after != before
        

@pytest.mark.usefixtures("page_spokopolish")
class TestConsentCookieRejectAll():
    
    def test_cookie_before(self,page_spokopolish:Page):
        context = page_spokopolish.context
        cookie = context.cookies()
        save(PATH_COOKIE_BEFORE_REJECT,json.dumps(cookie))
    
    def test_privacy_popup(self,page_spokopolish: Page):
        expect(page_spokopolish.get_by_role("heading", name="We value your privacy")).to_be_visible()
    
    def test_clicking_reject_all(self,page_spokopolish: Page):
        page_spokopolish.get_by_role("button", name="Reject All").click()
        expect(page_spokopolish.get_by_role("heading", name="We value your privacy")).not_to_be_visible()
    
    def test_cookies_after(self,page_spokopolish: Page):
        context = page_spokopolish.context
        cookies = context.cookies()
        after = find_cookie(COOKIE_CONSENT_NAME,cookies)
        before = get_file(PATH_COOKIE_BEFORE_REJECT)
        after == before