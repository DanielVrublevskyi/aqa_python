from playwright.sync_api import Page, expect


class GaragePage:
    def __init__(self, page:Page):
        self.page = page
        self.garage_title = page.locator(".panel-page_heading h1")
        self.add_car_button = page.get_by_role("button", name="Add car")
        self.empty_garage_message = page.locator(".panel-empty_message")

        self.header_logo = page.locator("a.header_logo")
        self.header_nav = page.locator("nav.header_nav")
        self.header_garage = self.header_nav.get_by_role("link", name="Garage")
        self.header_expenses = self.header_nav.get_by_role("link", name="Fuel expenses")
        self.header_instructions = self.header_nav.get_by_role("link", name="Instructions")
        self.my_profile_button = page.locator("#userNavDropdown")

        self.sidebar = page.locator("nav.sidebar")
        self.sidebar_garage = self.sidebar.get_by_role("link", name="Garage")
        self.sidebar_expenses = self.sidebar.get_by_role("link", name="Fuel expenses")
        self.sidebar_instructions = self.sidebar.get_by_role("link", name="Instructions")
        self.sidebar_profile = self.sidebar.get_by_role("link", name="Profile")
        self.sidebar_settings = self.sidebar.get_by_role("link", name="Settings")
        self.sidebar_logout = self.sidebar.locator("a.sidebar_btn", has_text="Log out")

    def assert_garage_page_is_opened(self):
        expect(self.garage_title).to_be_visible()
        expect(self.add_car_button).to_be_visible()
        expect(self.my_profile_button).to_be_visible()