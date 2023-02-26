from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("setup")
class TestHomeBtn:
    def test_home(self, setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.LINK_TEXT, "Contact Us").click()
        setup.find_element(By.LINK_TEXT, "Home").click()
        assert setup.current_url.endswith("/"), "Page URL does not match expected value after clicking on Home button"

