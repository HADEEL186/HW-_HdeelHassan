from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("setup")
class TestDeleteProfile:
    def test_delete(self, setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "(//img)[21]").click()
        setup.find_element(By.CSS_SELECTOR, "a[href='/delete/20']").click()
        assert setup.current_url.endswith("/"), "Page URL does not match expected value"

