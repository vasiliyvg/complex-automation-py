import pytest

from pages.the_internet.add_remove_element_page import AddRemoveElementPage


# Executed once before/after each test
@pytest.fixture(autouse=True)
def before_each_after_each(add_remove_element_page: AddRemoveElementPage):
    # Actions before all tests
    add_remove_element_page.navigate()
    yield
    # Actions after all tests


# TC 2: Add the element to the page
def test_add_element_to_the_page(add_remove_element_page: AddRemoveElementPage):
    add_remove_element_page.add_element()
    add_remove_element_page.should_have_elements(1)


# TC 3: Remove all elements from the page
def test_remove_all_elements_from_the_page(add_remove_element_page: AddRemoveElementPage):
    add_remove_element_page.add_element()
    add_remove_element_page.add_element()
    add_remove_element_page.should_have_elements(2)
    add_remove_element_page.remove_first_element()
    add_remove_element_page.should_have_elements(1)
    add_remove_element_page.remove_first_element()
    add_remove_element_page.should_have_elements(0)
