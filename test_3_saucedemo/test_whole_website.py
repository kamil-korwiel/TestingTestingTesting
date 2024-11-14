from playwright.sync_api import sync_playwright, Page, expect
import pytest
import re


user_name = "standard_user"
password = "secret_sauce"

@pytest.fixture(scope="session")
def login_in_page():
    # Initialize Playwright and open a browser
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    context = browser.new_context()
    context.set_default_timeout(10000)
    page = context.new_page()
    
    user = "standard_user"
    password = "secret_sauce"
    
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill(user)
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()
    
    yield page 

    # Teardown
    browser.close()
    playwright.stop()


def check_descending_order(item_list: list[str | int]) -> bool:
    for i in range(0, len(item_list)-1):
        if item_list[i] < item_list[i+1]:
            return False
    return True


def check_ascending_order(item_list: list[str | int]) -> bool:
    for i in range(0, len(item_list)-1):
        if item_list[i] > item_list[i+1]:
            return False
    return True

def test_have_title(login_in_page: Page):
    expect(login_in_page).to_have_title("Swag Labs")
    

def test_have_inventory(login_in_page: Page):
    expect(login_in_page.locator("[data-test=\"inventory-list\"]")).to_be_visible()
    

def test_have_correct_numbers_of_items_inventory(login_in_page: Page):
    list_of_items = login_in_page.locator("[data-test=\"inventory-item\"]").all()
    assert 6 == len(list_of_items)
    

def test_correct_item_button_text(login_in_page: Page):
    expect(login_in_page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_contain_text("Add to cart")
    

def test_correct_item_button_text_after_click(login_in_page: Page):
    login_in_page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(login_in_page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_contain_text("Remove")
    

def test_shop_cart_icon_indicator(login_in_page: Page):
    login_in_page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(login_in_page.locator("[data-test=\"inventory-item\"]")).to_contain_text("1")
    
    
def test_if_product_is_in_shopping_cart(login_in_page: Page):
    login_in_page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(login_in_page.locator("[data-test=\"inventory-item\"]")).to_be_visible()
    login_in_page.locator("[data-test=\"continue-shopping\"]").click()
    

def test_ascending_order_items_name(login_in_page: Page):
    
    login_in_page.locator("[data-test=\"product-sort-container\"]").select_option("az")
    list_of_items = login_in_page.locator("[data-test=\"inventory-list\"]").locator("[data-test=\"inventory-item\"]").all()
    str_title_list = [item.locator('[data-test="inventory-item-name"]').text_content() for item in list_of_items]
    assert check_ascending_order(str_title_list)
    

def test_descending_order_items_name(login_in_page: Page):
    login_in_page.locator("[data-test=\"product-sort-container\"]").select_option("za")
    list_of_items = login_in_page.locator("[data-test=\"inventory-list\"]").locator("[data-test=\"inventory-item\"]").all()
    str_title_list = [item.locator('[data-test="inventory-item-name"]').text_content() for item in list_of_items]
    assert check_descending_order(str_title_list)
    

def test_ascending_order_price(login_in_page: Page):
    login_in_page.locator("[data-test=\"product-sort-container\"]").select_option("lohi")
    list_of_items = login_in_page.locator("[data-test=\"inventory-list\"]").locator("[data-test=\"inventory-item\"]").all()
    str_price_list = [item.locator('[class="inventory_item_price"]').text_content() for item in list_of_items]
    int_price_list =  [ float(re.search("[0-9]+.[0-9][0-9]", str_price).group(0)) for str_price in str_price_list ]  
    assert check_ascending_order(int_price_list)
    

def test_descending_order_price(login_in_page: Page):
    login_in_page.locator("[data-test=\"product-sort-container\"]").select_option("hilo")
    list_of_items = login_in_page.locator("[data-test=\"inventory-list\"]").locator("[data-test=\"inventory-item\"]").all()
    str_price_list = [item.locator('[class="inventory_item_price"]').text_content() for item in list_of_items]
    int_price_list =  [ float(re.search("[0-9]+.[0-9][0-9]", str_price).group(0)) for str_price in str_price_list ]  
    assert check_descending_order(int_price_list)


def test_is_the_same_image(login_in_page: Page):
    try:
        img_from_grid = login_in_page.locator("[data-test=\"item-4-img-link\"]").get_by_role("img").get_attribute("src")
        login_in_page.locator("[data-test=\"item-4-img-link\"]").click()
        img_from_item = login_in_page.locator("[data-test=\"item-sauce-labs-backpack-img\"]").get_attribute("src")
        assert img_from_grid == img_from_item
    except Exception as e:
        login_in_page.screenshot(path=f'/home/confused/Documents/Code/PlayWrite/TestingTestingTesting/screenshot/{"fuuk"}.png')
        raise e

def test_is_have_working_go_back_button(login_in_page: Page):
    login_in_page.locator("[data-test=\"back-to-products\"]").click()
    expect(login_in_page.locator("[data-test=\"inventory-list\"]")).to_be_visible()
    
    
    
    

