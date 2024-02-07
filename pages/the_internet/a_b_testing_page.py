from playwright.sync_api import Page, expect


class ABTestingPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.header = page.get_by_role('heading')
        self.content = page.locator('p')

    def navigate(self) -> None:
        self.page.goto('/abtest')

    def should_have_header(self, text: str) -> None:
        expect(self.header).to_have_text(text)

    def should_have_content(self, text: str) -> None:
        expect(self.content).to_have_text(text)
