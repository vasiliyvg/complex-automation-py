import pytest

from pages.duck_duck_go.result import DuckDuckGoResultPage
from pages.duck_duck_go.search import DuckDuckGoSearchPage
from playwright.sync_api import Playwright, APIRequestContext, Page, sync_playwright
from typing import Generator
from pages.the_internet.a_b_testing_page import ABTestingPage
from pages.the_internet.add_remove_element_page import AddRemoveElementPage

# @pytest.fixture
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch()
#         yield browser
#         browser.close()
# 
# 
# @pytest.fixture
# def page(browser):
#     page = browser.new_page()
#     yield page
#     page.close()

# ------------------------------------------------------------
# Page objects
# ------------------------------------------------------------

# ------ Duck Duck Go

@pytest.fixture
def result_page(page: Page) -> DuckDuckGoResultPage:
    return DuckDuckGoResultPage(page)


@pytest.fixture
def search_page(page: Page) -> DuckDuckGoSearchPage:
    return DuckDuckGoSearchPage(page)


# ------ The Internet

@pytest.fixture
def a_b_page(page: Page) -> ABTestingPage:
    return ABTestingPage(page)


@pytest.fixture
def add_remove_element_page(page: Page) -> AddRemoveElementPage:
    return AddRemoveElementPage(page)


# Request context

@pytest.fixture(scope='session')
def gh_context(
        playwright: Playwright,
        gh_access_token: str) -> Generator[APIRequestContext, None, None]:
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {gh_access_token}"}

    request_context = playwright.request.new_context(
        base_url="https://api.github.com",
        extra_http_headers=headers)

    yield request_context
    request_context.dispose()
