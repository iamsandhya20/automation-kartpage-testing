
import pytest
from selenium import webdriver


@pytest.fixture()
def setup(request):
    driver = webdriver.Edge()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    print("Test ended...")
    driver.close()
