from playwright.sync_api import Page, expect
import re


user_name = "standard_user"
password = "secret_sauce"


def login(page: Page, user: str, password: str):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill(user)
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()


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


def test_have_title(page: Page):
    login(page, user_name, password)
    expect(page).to_have_title("Swag Labs")


def test_have_inventory(page: Page):
    login(page, user_name, password)
    expect(page.locator("[data-test=\"inventory-list\"]")).to_be_visible()


def test_have_correct_numbers_of_items_inventory(page: Page):
    login(page, user_name, password)
    list_of_items = page.locator("[data-test=\"inventory-item\"]").all()
    assert 6 == len(list_of_items)


def test_correct_item_button_text(page: Page):
    login(page, user_name, password)
    expect(page.locator(
        "[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_contain_text("Add to cart")


def test_correct_item_button_text_after_click(page: Page):
    login(page, user_name, password)
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(page.locator(
        "[data-test=\"remove-sauce-labs-backpack\"]")).to_contain_text("Remove")


def test_shop_cart_icon_indicator(page: Page):
    login(page, user_name, password)
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(page.locator(
        "[data-test=\"shopping-cart-link\"]")).to_contain_text("1")


def test_is_the_same_source_image(page: Page):
    login(page, user_name, password)
    img_from_grid = page.locator(
        "[data-test=\"item-4-img-link\"]").get_by_role("img").get_attribute("src")
    page.locator("[data-test=\"item-4-img-link\"]").click()
    img_from_item = page.locator(
        "[data-test=\"item-sauce-labs-backpack-img\"]").get_attribute("src")
    assert img_from_grid == img_from_item


def test_ascending_order_items_name(page: Page):
    login(page, user_name, password)
    page.locator("[data-test=\"product-sort-container\"]").select_option("az")
    list_of_items = page.locator(
        "[data-test=\"inventory-list\"]").locator("[data-test=\"inventory-item\"]").all()
    str_title_list = [item.locator(
        '[data-test="inventory-item-name"]').text_content() for item in list_of_items]
    assert check_ascending_order(str_title_list)


def test_descending_order_items_name(page: Page):
    login(page, user_name, password)
    page.locator("[data-test=\"product-sort-container\"]").select_option("za")
    list_of_items = page.locator(
        "[data-test=\"inventory-list\"]").locator("[data-test=\"inventory-item\"]").all()
    str_title_list = [item.locator(
        '[data-test="inventory-item-name"]').text_content() for item in list_of_items]
    assert check_descending_order(str_title_list)


def test_ascending_order_price(page: Page):
    login(page, user_name, password)
    page.locator(
        "[data-test=\"product-sort-container\"]").select_option("lohi")
    list_of_items = page.locator(
        "[data-test=\"inventory-list\"]").locator("[data-test=\"inventory-item\"]").all()
    str_price_list = [item.locator(
        '[class="inventory_item_price"]').text_content() for item in list_of_items]
    int_price_list = [float(re.search(
        "[0-9]+.[0-9][0-9]", str_price).group(0)) for str_price in str_price_list]
    assert check_ascending_order(int_price_list)


def test_descending_order_price(page: Page):
    login(page, user_name, password)
    page.locator(
        "[data-test=\"product-sort-container\"]").select_option("hilo")
    list_of_items = page.locator(
        "[data-test=\"inventory-list\"]").locator("[data-test=\"inventory-item\"]").all()
    str_price_list = [item.locator(
        '[class="inventory_item_price"]').text_content() for item in list_of_items]
    int_price_list = [float(re.search(
        "[0-9]+.[0-9][0-9]", str_price).group(0)) for str_price in str_price_list]
    assert check_descending_order(int_price_list)
