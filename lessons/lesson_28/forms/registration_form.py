from playwright.sync_api import Page

class RegistrationForm:
    def __init__(self, page:Page):
        self.inp_name = page.locator("#signupName")
        self.inp_last_name = page.locator("#signupLastName")
        self.inp_email = page.locator("input#signupEmail")
        self.inp_password = page.locator("input#signupPassword")
        self.inp_repeat_password = page.locator("input#signupRepeatPassword")
        self.register_button = page.locator(".modal-content button.btn-primary")

    def input_name(self, name: str):
        self.inp_name.fill(name)

    def input_last_name(self, last_name: str):
        self.inp_last_name.fill(last_name)

    def input_email(self, email: str):
        self.inp_email.fill(email)

    def input_password(self, password: str):
        self.inp_password.fill(password)

    def input_repeat_password(self, password: str):
        self.inp_repeat_password.fill(password)

    def click_register_button(self):
        self.register_button.click()
