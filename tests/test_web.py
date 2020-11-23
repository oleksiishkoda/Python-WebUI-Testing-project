import pytest

from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage



def test_basic_duckduckgo_search(browser):
    # URL = 'https://www.duckduckgo.com'
    # PHRASE = 'panda'
    # browser.get(URL)
    # search_input = browser.find_element_by_id('search_form_input_homepage')
    # search_input.send_keys(PHRASE + Keys.RETURN)
    # link_divs = browser.find_elements_by_css_selector('#links > div')
    # assert len(link_divs) > 0
    # xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE}')]"
    # phrase_results = browser.find_elements_by_xpath(xpath)
    # assert len(phrase_results) > 0
    # search_input = browser.find_element_by_id('search_form_input')
    # assert search_input.get_attribute('value') == PHRASE

    PHRASE = 'panda'
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    result_page = DuckDuckGoResultPage(browser)
    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE
