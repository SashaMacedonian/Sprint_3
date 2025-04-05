import pytest
from selenium import webdriver
import json
import os


@pytest.fixture
def chrome_browser():
    chrome_browser = webdriver.Chrome()
    yield chrome_browser
    chrome_browser.quit()

@pytest.fixture
def config():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, 'config.json')
    with open(config_path, 'r') as file_object:
        data = json.load(file_object)
    return data



