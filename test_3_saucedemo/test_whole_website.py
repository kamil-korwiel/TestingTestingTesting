import re
from playwright.async_api import Page, expect
import pytest


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



@pytest.mark.asyncio(loop_scope="session")
async def test_have_title(login_in_page: Page):
    await expect(login_in_page).to_have_title("Swag Labs")
    

@pytest.mark.asyncio(loop_scope="session")
async def test_have_inventory(login_in_page: Page):
    await expect(login_in_page.locator("[data-test=\"inventory-list\"]")).to_be_visible()
    

@pytest.mark.asyncio(loop_scope="session")
async def test_have_correct_numbers_of_items_inventory(login_in_page: Page):
    items = await login_in_page.locator("[data-test=\"inventory-item\"]").all()
    assert 6 == len(items)
    

@pytest.mark.asyncio(loop_scope="session")
async def test_correct_item_button_text(login_in_page: Page):
    await expect(login_in_page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_contain_text("Add to cart")
    

@pytest.mark.asyncio(loop_scope="session")
async def test_correct_item_button_text_after_click(login_in_page: Page):
    await login_in_page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    await expect(login_in_page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_contain_text("Remove")
    

@pytest.mark.asyncio(loop_scope="session")
async def test_shop_cart_icon_indicator(login_in_page: Page):
    await login_in_page.locator("[data-test=\"shopping-cart-link\"]").click()
    await expect(login_in_page.locator("[data-test=\"inventory-item\"]")).to_contain_text("1")
    
    
@pytest.mark.asyncio(loop_scope="session")
async def test_if_product_is_in_shopping_cart(login_in_page: Page):
    await login_in_page.locator("[data-test=\"shopping-cart-link\"]").click()
    await expect(login_in_page.locator("[data-test=\"inventory-item\"]")).to_be_visible()
    await login_in_page.locator("[data-test=\"continue-shopping\"]").click()
    

@pytest.mark.asyncio(loop_scope="session")
async def test_ascending_order_items_name(login_in_page: Page):
    await login_in_page.locator("[data-test=\"product-sort-container\"]").select_option("az")
    items = await login_in_page.locator("[data-test=\"inventory-item-name\"]").all_text_contents()
    assert check_ascending_order(items)
    

@pytest.mark.asyncio(loop_scope="session")
async def test_descending_order_items_name(login_in_page: Page):
    await login_in_page.locator("[data-test=\"product-sort-container\"]").select_option("za")
    items = await login_in_page.locator("[data-test=\"inventory-item-name\"]").all_text_contents()
    assert check_descending_order(items)
    

@pytest.mark.asyncio(loop_scope="session")
async def test_ascending_order_price(login_in_page: Page):
    await login_in_page.locator("[data-test=\"product-sort-container\"]").select_option("lohi")
    prices = await login_in_page.locator('[class="inventory_item_price"]').all_text_contents()
    price_list = [float(re.search("[0-9]+.[0-9][0-9]", price).group(0)) for price in prices]
    assert check_ascending_order(price_list)
    

@pytest.mark.asyncio(loop_scope="session")
async def test_descending_order_price(login_in_page: Page):
    await login_in_page.locator("[data-test=\"product-sort-container\"]").select_option("hilo")
    prices = await login_in_page.locator('[class="inventory_item_price"]').all_text_contents()
    price_list = [float(re.search("[0-9]+.[0-9][0-9]", price).group(0)) for price in prices]
    assert check_descending_order(price_list)


@pytest.mark.asyncio(loop_scope="session")
async def test_is_the_same_image(login_in_page: Page):
    try:
        img_from_grid = await login_in_page.locator("[data-test=\"item-4-img-link\"]").get_by_role("img").get_attribute("src")
        await login_in_page.locator("[data-test=\"item-4-img-link\"]").click()
        img_from_item = await login_in_page.locator("[data-test=\"item-sauce-labs-backpack-img\"]").get_attribute("src")
        assert img_from_grid == img_from_item
    except Exception as e:
        await login_in_page.screenshot(path=f'/home/confused/Documents/Code/PlayWrite/TestingTestingTesting/screenshot/{"fuuk"}.png')
        raise e


@pytest.mark.asyncio(loop_scope="session")
async def test_is_have_working_go_back_button(login_in_page: Page):
    await login_in_page.locator("[data-test=\"back-to-products\"]").click()
    await expect(login_in_page.locator("[data-test=\"inventory-list\"]")).to_be_visible()
