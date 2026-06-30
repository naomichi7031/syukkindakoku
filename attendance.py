from playwright.sync_api import sync_playwright
import os

ID = os.environ.get("LOGIN_ID")
PASS = os.environ.get("LOGIN_PASSWORD")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://sa.wims.jp/n9oZ2s/WA014Init.do?compUrl=OMK3")

    print("ログイン画面を開きました")

    browser.close()