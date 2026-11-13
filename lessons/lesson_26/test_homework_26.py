'''Сайт https://the-internet.herokuapp.com

Задача 1
1) Відкрити сторінку Add/Remove Elements
2) Натиснути кнопку add element і перевірити, що новий елемент додався
3) Натиснути кнопку delete і перевірити, що новий елемент зник
4) повторити декілька разів(додати поспіль елементи видалити багато елементів і тд)

Задача 2
1) відкрити Dynamic Content
2) Знайти 3 текста
3) Клюкнути на кнопку click here
4) Перевірити, що текст змінився'''

from playwright.sync_api import sync_playwright, expect

def create_browser(p):
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    page = browser.new_page(no_viewport=True)
    return page, browser


def test_add_remove_elements():
    with sync_playwright() as p:
        page, browser = create_browser(p)
        page.goto("https://the-internet.herokuapp.com")
        add_remove_elements = page.locator("a[href='/add_remove_elements/']")
        add_remove_elements.click()

        btn_add_element = page.get_by_role("button", name="Add Element")
        btn_delete = page.get_by_role("button", name="Delete")

        for i in range(1, 4):
            btn_add_element.click()
            expect(btn_delete).to_have_count(i)

        for i in range(2, -1, -1):
            btn_delete.nth(i).click()
            expect(btn_delete).to_have_count(i)

        browser.close()

def test_dynamic_content():
    with sync_playwright() as p:
        page, browser = create_browser(p)
        page.goto("https://the-internet.herokuapp.com")
        dynamic_content = page.locator("a[href='/dynamic_content']")
        dynamic_content.click()

        texts = page.locator(".large-10 .large-10")
        expect(texts).to_have_count(3)

        texts_before = texts.all_inner_texts()

        btn_click_here = page.locator("a[href='/dynamic_content?with_content=static']")
        btn_click_here.click()
        texts_after = texts.all_inner_texts()

        assert texts_before != texts_after