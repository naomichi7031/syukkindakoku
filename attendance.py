import os
from playwright.sync_api import sync_playwright

USER_ID = os.getenv("ATTENDANCE_ID")
PASSWORD = os.getenv("ATTENDANCE_PASSWORD")

def run(playwright):
    browser = playwright.chromium.launch(
        headless=True,
        args=["--no-sandbox"]
    )

    page = browser.new_page()

    page.goto("https://sa.wims.jp/n9oZ2s/WP001Init.do?compUrl=OMK3")

    page.get_by_role("textbox", name="User ID").fill(USER_ID)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)

    page.get_by_role("link", name="出勤").click()

    print("打刻完了")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
