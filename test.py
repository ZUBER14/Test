from playwright.sync_api import sync_playwright, expect

def test_basic(playwright):
    browser = playwright.chromium.launch(headless=False,channel="msedge" , args = ["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")

    # page.on("request")



    # page.wait_for_timeout(5000)

#   To check URL is correct what we expected
    expect(page).to_have_url("https://testautomationpractice.blogspot.com/")

    # Title
    expect(page).to_have_title("Automation Testing Practice")


    # #Visible on page
    # event = page.locator("#alertBtn")
    # expect(event).to_be_visible()

    # expect(page.locator("#python")).to_be_visible()

    # expect(event).to_be_enabled()

    # # We can add not to add assertion so it will work opposite 

    # expect(event).to_be_hidden()

    title = page.locator("h1[class='title']")

    expect(title).to_contain_text("Testing")
    expect(title).to_have_text("Automation Testing Practice")
    

    browser.close()

# Entry point
with sync_playwright() as playwright:
    test_basic(playwright)
