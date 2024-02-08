import pytest

from playwright.sync_api import expect, Page

ANIMALS = [
    'panda',
    'python',
]


@pytest.mark.parametrize('phrase', ANIMALS)
def test_basic_duckduckgo_search(
        phrase: str,
        page: Page,
        search_page,
        result_page):
    search_page.navigate()
    search_page.search(phrase)
    expect(result_page.search_input).to_have_value(phrase)
    assert result_page.result_link_titles_contain_phrase(phrase)

    # And the search result title contains the phrase
    expect(page).to_have_title(f'{phrase} at DuckDuckGo')
