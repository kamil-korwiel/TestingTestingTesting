from playwright.sync_api import Page,expect
import pytest


@pytest.mark.usefixtures("page_spokopolish")
class TestVisibilityOfElements:
    
    def test_nav_bar_elements(self,page_spokopolish: Page):
        expect(page_spokopolish.get_by_role("link", name="Home")).to_be_visible()
        expect(page_spokopolish.get_by_role("link", name="Courses", exact=True)).to_be_visible()
        expect(page_spokopolish.get_by_role("link", name="Polski dla firm")).to_be_visible()
        expect(page_spokopolish.get_by_role("link", name="Blog")).to_be_visible()
        expect(page_spokopolish.get_by_role("link", name="About Us")).to_be_visible()
            
        