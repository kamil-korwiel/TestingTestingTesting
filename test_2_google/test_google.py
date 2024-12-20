from playwright.sync_api import Page, expect
import pytest

@pytest.mark.browser_context_args(timezone_id="Europe/Warsaw", locale="pl-PL")
def test_google_attribute(page: Page):
    page.context.clear_cookies()
    page.context.set_default_timeout(10000)
    page.goto("https://google.pl/")
    page.get_by_role("button", name="Odrzuć wszystko").click()
    
    atr = page.get_by_role("img", name="Google").get_attribute("height")
    page.set_viewport_size({"width": 640, "height": 480});
    assert "92" == atr
    atr = page.get_by_role("img", name="Google").get_attribute("height")
    page.set_viewport_size({"width": 1280, "height": 960});
    assert "92" == atr