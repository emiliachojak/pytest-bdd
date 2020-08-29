import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants
DUCKDUCKGO_HOME = 'https://duckduckgo.com'
PATH_TO_CHROMEDRIVER = 'C:\\Users\\user\\Desktop\\pytest-bdd\\chromedriver.exe'

# Scenarios
scenarios('../features/web.feature')


# Fixtures
@pytest.fixture
def browser():
    driver = webdriver.Chrome(PATH_TO_CHROMEDRIVER)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# Given steps
@given('the DuckDuckGo home page is displayed')
def ddg_home(browser):
    browser.get(DUCKDUCKGO_HOME)


# When steps
@when(parsers.parse('the user searches for "{text}"'))
def search_phrase(browser, text):
    search_input = browser.find_element_by_name('q')
    search_input.send_keys(text + Keys.RETURN)


@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    """
    Check search result list
    A more comprehensive test would check results for marching phrases
    Check the list before the search phrase for correct implicit waiting
     """
    links_div = browser.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    # Check search phrase
    search_input = browser.find_element_by_name('q')
    assert search_input.get_attribute('value') == phrase
