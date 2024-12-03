from playwright.sync_api import Page,expect
import pytest


@pytest.mark.usefixtures("page_spokopolish")
class TestVisibilityOfElements:
    
    points = {
        "Own system":"We’re the only Polish school teaching with our own system – based on CEFR",
        "Own materials":"We create our own materials & lesson plans",
        "Logical, comprehensive, STEP-BY-STEP grammar explanations":"Complex concepts are stripped apart and fed to you in smaller chunks. As a result, you gradually build your understanding of grammar logically. Therefore, we strengthen your ability to apply grammar in practice",
        "Instruction in a language you speak":"We teach in English (or Ukrainian, Russian, French or Spanish) on basic levels. Then, gradually shift to teaching in Polish",
        "Language background recognition":"People have different learning needs depending on their language background. So, we don’t mix Slavic & non-Slavic learners in groups below B1",
        "Friendly learning environment":"Passionate teachers, who create genuine connections with their students",
        "Also a NGO":"We’re a people-oriented non-governmental organisation (NGO), as well as a language school",
    }
    points.keys()
    
    def test_nav_bar_elements(self,page_spokopolish: Page):
        expect(page_spokopolish.get_by_role("link", name="Home")).to_be_visible()
        expect(page_spokopolish.get_by_role("link", name="Courses", exact=True)).to_be_visible()
        expect(page_spokopolish.get_by_role("link", name="Polski dla firm")).to_be_visible()
        expect(page_spokopolish.get_by_role("link", name="Blog")).to_be_visible()
        expect(page_spokopolish.get_by_role("link", name="About Us")).to_be_visible()
            
    def test_bullet_points(self, page_spokopolish: Page):
        # css selector
        list_of_points = page_spokopolish.locator('.cmsmasters_row_outer').locator('li').all()
        for point, title in zip(list_of_points, self.points.keys()):
            expect(point.locator(".cmsmasters_icon_list_item_title")).to_contain_text(title)
            expect(point.locator(".cmsmasters_icon_list_item_text")).to_contain_text(self.points[title])
            