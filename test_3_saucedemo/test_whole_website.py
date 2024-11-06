from playwright.sync_api import Page, expect


user_name = "standard_user"
password = "secret_sauce"


def login(page: Page,user: str,password: str):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill(user)
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()
    

def test_have_title(page: Page):
    login(page, user_name , password)
    expect(page).to_have_title("Swag Labs")
    

def test_have_inventory(page: Page):
    login(page, user_name , password)
    expect(page.locator("[data-test=\"inventory-list\"]")).to_be_visible()
    

def test_have_correct_numbers_of_items_inventory(page: Page):
    login(page, user_name , password)
    list_of_items = page.locator("[data-test=\"inventory-item\"]").all()
    assert 6 == len(list_of_items)
    

def test_correct_item_button_text(page: Page):
    login(page, user_name , password)
    expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_contain_text("Add to cart")
    

def test_correct_item_button_text_after_click(page: Page):
    login(page, user_name , password)
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_contain_text("Remove")
    

def test_shop_cart_icon_indicator(page: Page):
    login(page, user_name , password)
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_contain_text("1")
    

def test_is_the_same_image(page: Page):
    login(page, user_name , password)
    img_from_grid = page.locator("[data-test=\"item-4-img-link\"]").get_by_role("img").get_attribute("src")
    page.locator("[data-test=\"item-4-img-link\"]").click()
    img_from_item = page.locator("[data-test=\"item-sauce-labs-backpack-img\"]").get_attribute("src")
    assert img_from_grid == img_from_item
    

def test_ascending_order(page: Page):
    login(page, user_name , password)
    list_of_items = page.locator("[data-test=\"inventory-list\"]").locator("[data-test=\"inventory-item\"]").all()
    page.locator("[data-test=\"product-sort-container\"]").select_option("az")

    uno_item = list_of_items[0].locator('[data-test="inventory-item-name"]').text_content()
    for i in range(1, len(list_of_items)):
        dos_item = list_of_items[i].locator('[data-test="inventory-item-name"]').text_content()
        print(dos_item)
        print(uno_item < dos_item)
        uno_item = dos_item
    

def test_descending_order(page: Page):
    login(page, user_name , password)
    list_of_items = page.locator("[data-test=\"inventory-list\"]").locator("[data-test=\"inventory-item\"]").all()
    page.locator("[data-test=\"product-sort-container\"]").select_option("za")
    
    uno_item = list_of_items[0].locator('[data-test="inventory-item-name"]').text_content()
    for i in range(1, len(list_of_items)):
        dos_item = list_of_items[i].locator('[data-test="inventory-item-name"]').text_content()
        print(dos_item)
        print(uno_item > dos_item)
        uno_item = dos_item