from BaseClass import BaseClass
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixture("setup")
@pytest.mark.smoke
class TestSmoke(BaseClass):
    def test_home(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.LINK_TEXT, "Contact Us").click()
        setup.find_element(By.LINK_TEXT, "Home").click()
        setup.get_screenshot_as_file("currentURL.png")
        assert setup.current_url.endswith("/"), log.critical("Page URL does not match expected value after clicking on Home button")
        log.info("test_home passed: the URL is the same")

    def test_logo(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.LINK_TEXT, "About").click()
        setup.find_element(By.XPATH, "//a[@href='/']//img").click()
        setup.get_screenshot_as_file("logoBtn.png")
        assert setup.current_url.endswith("/"), log.critical("Page URL does not match expected value after clicking on logo")
        log.info("test_Logo passed")

    def test_footer(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://127.0.0.1:5000")
        footer = setup.find_element_by_tag_name("footer")
        setup.get_screenshot_as_file("footer.png")
        assert footer.is_displayed(), log.critical("test_footer failed")
        log.info("test_footer passed")

    def test_home_screenshot(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.LINK_TEXT, "Contact Us").click()
        setup.get_screenshot_as_file("screenshot/Smoke_Test/test_home/step1.png")
        setup.find_element(By.LINK_TEXT, "Home").click()
        assert setup.current_url.endswith("/"), log.critical("Page URL does not match expected value after clicking on Home button")
        log.info("test_home_screenshot passed")

    def test_facebook_icon(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "//a[@class='facebook']").click()
        setup.get_screenshot_as_file("facebook.png")
        assert "facebook" in setup.current_url, log.critical("Page URL does not match expected value")
        log.info("test_facebookIcon passed")

    def test_twitter_icon(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "//a[@class='twitter']").click()
        setup.get_screenshot_as_file("twitter.png")
        assert "twitter" in setup.current_url, log.critical("Page URL does not match expected value")
        log.info("test_twitterIcon passed")

    def test_youtube_icon(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "//a[@class='youtube']").click()
        setup.get_screenshot_as_file("youtube.png")
        assert "youtube" in setup.current_url, log.critical("Page URL does not match expected value")
        log.info("test_youtubeIcon passed")

    def test_google_icon(self, setup):
        log = self.getLogger(self.__class__.__name__)
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "//a[@class='google']").click()
        setup.get_screenshot_as_file("google.png")
        assert "google" in setup.current_url, log.critical("Page URL does not match expected value")
        log.info("test_googleIcon passed")
