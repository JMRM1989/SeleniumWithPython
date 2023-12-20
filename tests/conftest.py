import os
import pytest as pytest
from selenium import webdriver



@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome()
    yield driver

    driver.quit()


@pytest.fixture
def headless_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    yield driver

    driver.quit()


@pytest.fixture()
def root_url():
    return "https://test-design.org/practical-exercises/"


def get_config_path():
    ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
    return os.path.join(ROOT_DIR, 'config', 'test_config_json')
