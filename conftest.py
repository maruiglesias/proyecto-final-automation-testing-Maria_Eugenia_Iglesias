import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)

    yield driver

    driver.quit()

@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
def headers():
    return {"x-api-key": "reqres_30304c3dafc04758b8db4299ac4def16"} 