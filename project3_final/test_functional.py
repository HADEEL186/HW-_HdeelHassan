from BaseClass import BaseClass
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("setup")
@pytest.mark.functional
class TestFunctional(BaseClass):

    def test_addBtn(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "//a[@href='add_profile']").click()
        setup.get_screenshot_as_file("addBtn.png")
        assert setup.current_url.endswith("/add_profile"),log.error("Page URL does not match expected value")
        log.info("test_addBtn passed")

    def test_contact(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.LINK_TEXT, "Contact Us").click()
        setup.find_element(By.ID, "name").send_keys("Hadeel")
        setup.find_element(By.ID, "email").send_keys("hadeelhassan186@gmail.com")
        setup.find_element(By.ID, "message").send_keys("Hi")
        setup.get_screenshot_as_file("message.png")
        setup.find_element(By.XPATH, "//input[@value='Submit']").click()
        assert setup.current_url.endswith("http://127.0.0.1:5000/contact"),log.error("Page URL does not match")
        log.info("test_contact passed")

    def test_title(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://127.0.0.1:5000")
        title = setup.find_element(By.XPATH, "//div[@class='logo']").text
        setup.get_screenshot_as_file("tittle.png")
        assert title == "Powerful women in Tech",log.error("the test faild")
        log.info("test_title passed")

    def test_search_empty(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "//input[@placeholder='Enter search keywords']").send_keys(" ")
        setup.find_element(By.CSS_SELECTOR, "input[value='search']").click()
        setup.get_screenshot_as_file("emptySearch.png")
        assert setup.current_url.endswith("http://127.0.0.1:5000"),log.error("Page URL does not match")
        log.info("test_search_empty passed")