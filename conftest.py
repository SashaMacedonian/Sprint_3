import pytest
from selenium import webdriver
import json


@pytest.fixture
def chrome_browser():
    chrome_browser = webdriver.Chrome()
    yield chrome_browser
    chrome_browser.quit()

@pytest.fixture
def config():
    path = "/Users/davlikanov/Desktop/Sprint_3/config.json"
    with open(path, 'r') as file_object:
        data = json.load(file_object)
    return data



