from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("setup")
class TestAbout:
    def test_about(self, setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.LINK_TEXT, "About").click()
        assert "About Us" in setup.find_element(By.CSS_SELECTOR, "body center h1").text, "Page title does not match expected value"
     