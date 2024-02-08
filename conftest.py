import pytest
from playwright.sync_api import Page

from pages.duck_duck_go.result import DuckDuckGoResultPage
from pages.duck_duck_go.search import DuckDuckGoSearchPage
from pages.the_internet.a_b_testing_page import ABTestingPage
from pages.the_internet.add_remove_element_page import AddRemoveElementPage
from pages.the_internet.basic_auth_page import BasicAuthPage


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


@pytest.fixture
def basic_auth_page(page: Page) -> BasicAuthPage:
    return BasicAuthPage(page)

# Request context


#
# @pytest.fixture(scope='session')
# def gh_context(
#         playwright: Playwright,
#         gh_access_token: str) -> Generator[APIRequestContext, None, None]:
#     headers = {
#         "Accept": "application/vnd.github.v3+json",
#         "Authorization": f"token {gh_access_token}"}
#
#     request_context = playwright.request.new_context(
#         base_url="https://api.github.com",
#         extra_http_headers=headers)
#
#     yield request_context
#     request_context.dispose()
