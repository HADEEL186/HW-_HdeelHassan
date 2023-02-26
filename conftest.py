from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pytest

@pytest.fixture()
def setup():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    # chrome_options.add_argument("headless")
    service_obj = Service("chromedriver_linux64/chromedriver")
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    return driver