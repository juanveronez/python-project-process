from time import sleep

from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
import subprocess

@pytest.fixture
def driver():
    process = subprocess.Popen(["task", "run"])
    
    options = ChromeOptions()
    options.headless = True
    driver = Chrome(options=options)

    driver.set_page_load_timeout(5)
    yield driver

    driver.quit()
    process.kill()

def test_app_opens(driver: WebDriver):
    driver.get("http://localhost:8501")
    sleep(5)

def test_page_title(driver: WebDriver):
    driver.get("http://localhost:8501")
    sleep(5)

    page_title = driver.title
    expected_title = "Excel Schema Validator"

    assert page_title == expected_title
