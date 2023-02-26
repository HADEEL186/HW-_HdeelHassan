from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("setup")
class TestAddButton:
    def test_addBtn(self, setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "//a[@href='add_profile']").click()
        assert setup.current_url.endswith("/add_profile"), "Page URL does not match expected value"


