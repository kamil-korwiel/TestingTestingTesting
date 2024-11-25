# import re
# from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.google.pl/?gws_rd=ssl")
#     page.get_by_label("Wybierz język, pl").click()
#     page.get_by_role("button", name="Odrzuć wszystko").click()
#     page.get_by_role("img", name="Google").click()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
