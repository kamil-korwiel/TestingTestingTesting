from playwright.sync_api import Page, expect


def login(page: Page,user: str,password: str):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill(user)
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()

def test_correct_login_in(page: Page):
    login(page,"standard_user","secret_sauce")    
    assert "https://www.saucedemo.com/inventory.html" == page.url
    expect(page.locator("[data-test=\"inventory-list\"]")).to_be_visible()

def test_incorrect_login(page: Page):
    login(page,"incorrect_user","secret_sauce")    
    assert "https://www.saucedemo.com/" == page.url
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Username and password do not match any user in this service")
    

def test_locked_user_login(page: Page):
    login(page,"locked_out_user","secret_sauce")
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Sorry, this user has been locked out.")

    