import os
from playwright.sync_api import sync_playwright

USER_ID = os.getenv("ATTENDANCE_ID")
PASSWORD = os.getenv("ATTENDANCE_PASSWORD")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto("https://sa.wims.jp/n9oZ2s/WP001Init.do?compUrl=OMK3")

    print("ページを開きました")

    page.get_by_role("textbox", name="User ID").fill(USER_ID)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)

    page.get_by_role("link", name="出勤").click()

    print("打刻完了")

    browser.close()
