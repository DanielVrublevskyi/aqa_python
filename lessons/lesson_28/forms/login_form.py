from playwright.sync_api import Page, expect

from lessons.lesson_28.pages.garage_page import GaragePage


class LoginForm:
    def __init__(self, page:Page):
        self.page = page

        self.inp_email = page.locator("input#signinEmail")
        self.inp_password = page.locator("input#signinPassword")
        self.login_button = page.locator(".modal-content button.btn-primary")
        self.login_error = page.locator("p.alert-danger")

    def fill_login_form_and_click_login(self, email: str, password: str) -> GaragePage:
        self.inp_email.fill(email)
        self.inp_password.fill(password)
        self.login_button.click()
        return GaragePage(self.page)

    def assert_login_error_is_shown(self):
        expect(self.login_error).to_have_text("Wrong email or password")