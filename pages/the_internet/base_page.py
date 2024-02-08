import os

from playwright.sync_api import Page

from config import config


class BasePage:

    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self, url: str) -> None:
        self.page.goto(config.base_url + url)
