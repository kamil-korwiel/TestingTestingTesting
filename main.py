import nest_asyncio; nest_asyncio.apply()  # This is needed to use sync API in repl
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as pw:
    # create browser instance
        browser = pw.chromium.launch(
            # we can choose either a Headful (With GUI) or Headless mode:
            headless=False,
        )
        # create context
        # using context we can define page properties like viewport dimensions
        context = browser.new_context(
            # most common desktop viewport is 1920x1080
            viewport={"width": 1920, "height": 1080}
        )
        # create page aka browser tab which we'll be using to do everything
        page = context.new_page()
        page.goto("https://google.pl/")
        page.get_by_test_id("lnXdpd")
        element = page.get_by_test_id("lnXdpd")
        atr = element.get_attribute('src')
        print(atr)


if __name__ == "__main__":
    main()