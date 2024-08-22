import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    firefox = webdriver.Firefox()
    firefox.maximize_window()

    yield firefox

    firefox.quit()
