
from playwright.sync_api import Route, Playwright

# NOT_ALLOWED_RESOURCES = (
#     "image", "font", "stylesheet", "media"
# )

# def on_route(route:Route):
#     if route.request.resource_type in NOT_ALLOWED_RESOURCES:
#         route.abort()

#     else:
#         route.continue_()


def test_browser_context(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    # page.route("**", on_route)

    page.goto("https://testautomationpractice.blogspot.com/")

    page.wait_for_timeout(5000)