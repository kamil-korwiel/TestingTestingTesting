import re
from playwright.sync_api import Page, expect

def test_google_attribute(page: Page):
    page.goto("https://google.pl/")
    element = page.locator("/html/body/div[1]/div[2]/div/img")
    name = element.get_attribute("alt")
    assert "Google" == name