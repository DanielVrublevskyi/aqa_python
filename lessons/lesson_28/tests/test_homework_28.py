from lessons.lesson_28.pages.garage_page import GaragePage
from lessons.lesson_28.pages.home_page import HomePage
from lessons.lesson_28.tests.data_for_tests import generate_email, generate_password, \
    generate_first_name, generate_last_name
from lessons.lesson_28.config import TEST_EMAIL, TEST_PASSWORD

class TestHomePgeSanity:

    def test_home_page(self, page):
        home_page = HomePage(page)
        home_page.assert_home_page_is_opened()


    def test_registration(self, page):
        home_page = HomePage(page)
        registration_form = home_page.click_sign_up()

        name = generate_first_name()
        last_name = generate_last_name()
        email = generate_email()
        password = generate_password()

        registration_form.input_name(name)
        registration_form.input_last_name(last_name)
        registration_form.input_email(email)
        registration_form.input_password(password)
        registration_form.input_repeat_password(password)
        registration_form.click_register_button()

        garage_page = GaragePage(page)
        garage_page.assert_garage_page_is_opened()

    def test_guest_login(self, page):
        home_page = HomePage(page)

        garage_page = home_page.click_guest_login()
        garage_page.assert_garage_page_is_opened()

    def test_login(self, page):
        home_page = HomePage(page)
        login_form = home_page.click_sign_in()
        garage_page =login_form.fill_login_form_and_click_login(TEST_EMAIL, TEST_PASSWORD)
        garage_page.assert_garage_page_is_opened()

    def test_invalid_login(self, page):
        home_page = HomePage(page)
        login_form = home_page.click_sign_in()
        email = generate_email()
        password = generate_password()
        login_form.fill_login_form_and_click_login(email, password)
        login_form.assert_login_error_is_shown()

