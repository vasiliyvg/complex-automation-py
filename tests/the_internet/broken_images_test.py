import pytest


# Executed once before/after each test
@pytest.fixture(autouse=True)
def before_each_after_each(broken_images_page):
    # Actions before all tests
    broken_images_page.navigate()
    yield
    # Actions after all tests


# TC 5: Broken images
def test_find_broken_images(broken_images_page):
    broken_images_page.should_have_broken_images_by_src(["/img/avatar-blank.jpg"], ["asdf.jpg", "hjkl.jpg"])
