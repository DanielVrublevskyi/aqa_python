import os

import pytest
import allure
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=os.getenv("CI") == "true",
            args=["--start-maximized"]
        )
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    page.goto("https://guest:welcome2qauto@qauto.forstudy.space/")

    yield page

    try:
        allure.attach(
            page.screenshot(full_page=True),
            name="Final screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    finally:
        context.close()