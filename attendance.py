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

    # 発生した通信をすべてログに出す(dakoku関連の通信を特定するため)
    page.on("request", lambda req: print(f"[REQUEST] {req.method} {req.url}"))
    page.on("response", lambda res: print(f"[RESPONSE] {res.status} {res.url}"))

    page.goto("https://sa.wims.jp/n9oZ2s/WP001Init.do?compUrl=OMK3")
    page.wait_for_load_state("networkidle")

    page.get_by_role("textbox", name="User ID").fill(USER_ID)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)

    page.get_by_role("link", name="出勤").click()

    # クリック後に発生する通信が完了するまで待つ
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(3000)  # 念のため追加の待機

    page.screenshot(path="/tmp/after_click.png")

    print("打刻完了")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
