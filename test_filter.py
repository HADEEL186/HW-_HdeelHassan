from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("setup")
class TestFilter:
    def test_title(self, setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "//input[@placeholder='Enter filter value']").send_keys("founder")
        setup.find_element(By.CSS_SELECTOR, "input[value='Filter']").click()
        assert len(setup.find_elements(By.XPATH,"//th[1]")) != 0, "You didn't get anything"
