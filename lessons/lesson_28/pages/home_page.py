from playwright.sync_api import Page, expect

from lessons.lesson_28.pages.garage_page import GaragePage
from lessons.lesson_28.pages.login_form import LoginForm
from lessons.lesson_28.pages.registration_form import RegistrationForm


class HomePage:
    def __init__(self, page: Page):
        self.page = page

        self.hillel_logo = page.locator("a.header_logo")
        self.home_button = page.locator("//a[contains(@class, 'header-link') and text()='Home']")
        self.about_button = page.locator("button[appscrollto='aboutSection']")
        self.contacts_button = page.locator("button[appscrollto='contactsSection']")
        self.guest_login_button = page.locator("button.-guest")
        self.sign_in_button = page.locator("button.header_signin")
        self.sign_up_button = page.locator("//button[contains(@class, 'btn-primary') and text()='Sign up']")
        self.video = page.locator("iframe.hero-video_frame")
        self.do_more_title = page.locator("h1.hero-descriptor_title")
        self.hero_description = page.locator("p.hero-descriptor_descr")
        self.facebook_link = page.locator("span.icon-facebook")
        self.telegram_link = page.locator("span.icon-telegram")
        self.youtube_link = page.locator("span.icon-youtube")
        self.instagram_link = page.locator("span.icon-instagram")
        self.linkedin_link = page.locator("span.icon-linkedin")

    def assert_home_page_is_opened(self):
        expect(self.hillel_logo).to_be_visible()
        expect(self.home_button).to_be_visible()
        expect(self.about_button).to_be_visible()
        expect(self.contacts_button).to_be_visible()
        expect(self.guest_login_button).to_be_visible()
        expect(self.sign_in_button).to_be_visible()
        expect(self.video).to_be_visible()
        expect(self.sign_up_button).to_be_visible()

    def click_sign_up(self) -> RegistrationForm:
        self.sign_up_button.click()
        return RegistrationForm(self.page)

    def click_guest_login(self) -> GaragePage:
        self.guest_login_button.click()
        return GaragePage(self.page)

    def click_sign_in(self) -> LoginForm:
        self.sign_in_button.click()
        return LoginForm(self.page)

