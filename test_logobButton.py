from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("setup")
class TestLogo:
    def test_Logo(self, setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.LINK_TEXT, "About").click()
        setup.find_element(By.XPATH, "//a[@href='/']//img").click()
        assert setup.current_url.endswith("/"), "Page URL does not match expected value after clicking on logo"
