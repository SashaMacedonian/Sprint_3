import pytest
from selenium import webdriver


@pytest.fixture
def chrome_browser():
    chrome_browser = webdriver.Chrome()
    yield chrome_browser
    chrome_browser.quit()






