from config import config


# TC 4: Login using basic auth
def test_basic_auth(basic_auth_page):
    basic_auth_page.perform_log_in(config.user_name, config.password)
    basic_auth_page.navigate()
    basic_auth_page.should_be_logged_in()
