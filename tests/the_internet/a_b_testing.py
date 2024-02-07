from pages.the_internet.a_b_testing_page import ABTestingPage


# TC 1: AB page should display header and multi-line content
def test_a_b_page(a_b_page: ABTestingPage):
    a_b_page.navigate()
    a_b_page.should_have_header('No A/B Test')
    a_b_page.should_have_content("""Also known as split testing. This is a way in which businesses are able to 
    simultaneously test and learn from different versions of a page to see which text and/or functionality works best 
    towards a desired outcome (e.g. a user action such as a click-through).""")
