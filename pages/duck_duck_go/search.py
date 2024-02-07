"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

import os

from playwright.sync_api import Page


class DuckDuckGoSearchPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_button = page.locator('button[aria-label="Search"]')
        self.search_input = page.locator('#searchbox_input')
    
    def navigate(self) -> None:
        self.page.goto('/')
    
    def search(self, phrase: str) -> None:
        self.search_input.fill(phrase)
        self.search_input.wait_for()
        self.search_button.click()
