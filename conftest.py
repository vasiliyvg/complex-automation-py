import pytest
from playwright.sync_api import Page

from pages.the_internet.a_b_testing_page import ABTestingPage
from pages.the_internet.add_remove_element_page import AddRemoveElementPage
from pages.the_internet.basic_auth_page import BasicAuthPage


# ------------------------------------------------------------
# Page objects
# ------------------------------------------------------------

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