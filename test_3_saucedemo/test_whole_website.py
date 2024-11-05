from playwright.sync_api import Page, expect

def login(page: Page,user: str,password: str):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill(user)
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()
    

def test_have_title(page: Page):
    login(page,"standard_user","secret_sauce")
    expect(page).to_have_title("Swag Labs")
    

def test_have_inventory(page: Page):
    login(page,"standard_user","secret_sauce")
    expect(page.locator("[data-test=\"inventory-list\"]")).to_be_visible()
    

def test_have_correct_numbers_of_items_inventory(page: Page):
    login(page,"standard_user","secret_sauce")
    list_of_items = page.locator("[data-test=\"inventory-item\"]").all()
    assert 6 == len(list_of_items)
    

def test_correct_item_button_text(page: Page):
    login(page,"standard_user","secret_sauce")
    expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_contain_text("Add to cart")
    

def test_correct_item_button_text_after_click(page: Page):
    login(page,"standard_user","secret_sauce")
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_contain_text("Remove")
    

def test_shop_cart_icon_indicator(page: Page):
    login(page,"standard_user","secret_sauce")
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_contain_text("1")
    

def test_is_the_same_image(page: Page):
    login(page,"standard_user","secret_sauce")
    img_from_grid = page.locator("[data-test=\"item-4-img-link\"]").get_by_role("img").get_attribute("src")
    page.locator("[data-test=\"item-4-img-link\"]").click()
    img_from_item = page.locator("[data-test=\"item-sauce-labs-backpack-img\"]").get_attribute("src")
    assert img_from_grid == img_from_item
    

