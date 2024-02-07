from playwright.sync_api import Page, expect


class AddRemoveElementPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.add_element_button = page.get_by_role('button', name='Add Element')
        self.element_button = page.get_by_role('button', name='Delete')

    def navigate(self) -> None:
        self.page.goto('/add_remove_elements/')

    def add_element(self) -> None:
        self.add_element_button.click()

    def remove_first_element(self) -> None:
        self.element_button.first.click()

    def should_have_elements(self, num: int) -> None:
        expect(self.element_button).to_have_count(num)
