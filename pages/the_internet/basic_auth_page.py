from playwright.sync_api import Page, expect

from config import config
from pages.the_internet.base_page import BasePage


class BasicAuthPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def perform_log_in(self, user_name: str, password: str) -> None:
        context = self.page.context.browser.new_context(
            base_url=config.base_url,
            http_credentials={'username': user_name, 'password': password}
        )
        self.page = context.new_page()

    def navigate(self, **kwargs) -> None:
        BasePage.navigate(self, '/basic_auth')

    def should_be_logged_in(self) -> None:
        expect(self.page.get_by_role('paragraph')).to_have_text(
            'Congratulations! You must have the proper credentials.')
