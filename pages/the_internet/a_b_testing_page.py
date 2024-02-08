from playwright.sync_api import Page, expect

from pages.the_internet.base_page import BasePage


class ABTestingPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.header = page.get_by_role('heading')
        self.content = page.locator('p')

    def navigate(self, **kwargs) -> None:
        BasePage.navigate(self, '/abtest')

    def should_have_header(self, text: str) -> None:
        expect(self.header).to_have_text(text)

    def should_have_content(self, text: str) -> None:
        expect(self.content).to_have_text(text)
