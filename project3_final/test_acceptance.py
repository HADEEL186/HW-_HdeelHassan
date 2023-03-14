import time
from BaseClass import BaseClass
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("setup")
@pytest.mark.acceptance
class TestAcceptance(BaseClass):
    def test_open_about_page(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.LINK_TEXT, "About").click()
        setup.get_screenshot_as_file("aboutPage.png")
        assert "About Us" in setup.find_element(By.CSS_SELECTOR, "body center h1").text, log.error(
            "Page title does not match expected value")
        log.info("passed")

    def test_add_profile(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "//a[@href='add_profile']").click()
        setup.find_element(By.XPATH, "//input[@name='filename']").send_keys(
            "C:/Users/97252/OneDrive/שולחן העבודה/projectphoto/x.jpg")
        setup.find_element(By.CSS_SELECTOR, "input[name*='rate']").send_keys("4")
        setup.find_element(By.CSS_SELECTOR, "input[type='text'][name$='name']").send_keys("NOURA")
        setup.find_element(By.CSS_SELECTOR, "input[name*='position']").send_keys("founder")
        setup.find_element(By.CSS_SELECTOR, "input[name*='company']").send_keys("ADF")
        setup.find_element(By.CSS_SELECTOR, "input[name*='country']").send_keys("Isreal")
        setup.find_element(By.CSS_SELECTOR, "input[name*='birth_date']").send_keys("5/5/1991")
        setup.find_element(By.XPATH, "//textarea[@placeholder='Enter information']").send_keys("wonderful")
        setup.get_screenshot_as_file("add.png")
        setup.find_element(By.XPATH, "//button[@type='submit']").click()
        assert setup.current_url == "http://127.0.0.1:5000", log.error("The test faild")
        log.info("passed")

    def test_filter(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "//input[@placeholder='Enter filter value']").send_keys("founder")
        setup.get_screenshot_as_file("filter.png")
        setup.find_element(By.CSS_SELECTOR, "input[value='Filter']").click()
        assert len(setup.find_elements(By.XPATH, "//th[1]")) != 0, log.error("You didn't get anything")
        log.info("passed")

    def test_search(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "//input[@placeholder='Enter search keywords']").send_keys("Kelly")
        setup.find_element(By.CSS_SELECTOR, "input[value='search']").click()
        print("Passed!")
        assert len(setup.find_elements(By.XPATH, "(//a)[6]")) == 1, "You didn't get anything"
        print("Passed!")
        link_element = setup.find_element(By.XPATH, "(//a)[6]")
        assert "Kelly" in link_element.text, log.error("Search results do not match the search keywords")
        log.info("passed")

    def test_back_top(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://127.0.0.1:5000")
        setup.execute_script("window.scrollBy(0,document.body.scrollHeight);")
        setup.get_screenshot_as_file("bottom.png")
        setup.execute_script("window.scrollTo(0,0);")
        setup.get_screenshot_as_file("top.png")
        setup.find_element(By.LINK_TEXT, "Back to top").click()
        assert setup.execute_script("return window.scrollY") == 0, log.error("Back to top button did not work")