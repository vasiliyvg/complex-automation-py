from playwright.sync_api import Page, expect
from config import config

from pages.the_internet.base_page import BasePage


class BrokenImagesPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.img = page.locator('.example img')

    def navigate(self, **kwargs) -> None:
        BasePage.navigate(self, '/broken_images')

    def should_have_broken_images_by_src(self, valid_src_list, broken_src_list) -> None:
        for img in self.img.all():
            src = img.get_attribute('src')
            res = self.page.request.get(f"{config.base_url}/{img.get_attribute('src')}")
            if src in valid_src_list:
                assert res.status == 200
            if src in broken_src_list:
                assert (res.status == 404)