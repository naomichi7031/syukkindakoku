import os
from playwright.sync_api import Playwright, sync_playwright


USER_ID = os.getenv("ATTENDANCE_ID")
PASSWORD = os.getenv("ATTENDANCE_PASSWORD")


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)

    context = browser.new_context()
    page = context.new_page()

    page.goto("https://sa.wims.jp/n9oZ2s/WP001Init.do?compUrl=OMK3")

    print("ページを開きました")

    # ID入力
    page.get_by_role("textbox", name="User ID").fill(USER_ID)

    # パスワード入力
    page.get_by_role("textbox", name="Password").fill(PASSWORD)

    print("ID/PASS入力完了")

    # 出勤ボタン押下
    page.get_by_role("link", name="出勤").click()

    print("出勤打刻完了")

    page.wait_for_timeout(5000)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
