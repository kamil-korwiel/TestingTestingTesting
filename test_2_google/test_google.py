from playwright.sync_api import Page, expect



def test_google_attribute(page: Page):
    page.goto("https://google.pl/")
    page.get_by_role("button", name="Odrzuć wszystko").click()
    
    atr = page.get_by_role("img", name="Google").get_attribute("height")
    page.set_viewport_size({"width": 640, "height": 480});
    assert "92" == atr
    atr = page.get_by_role("img", name="Google").get_attribute("height")
    page.set_viewport_size({"width": 1280, "height": 960});
    assert "92" == atr