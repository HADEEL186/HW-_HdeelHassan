from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("setup")
class TestContact:
    def test_contact(self, setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.LINK_TEXT, "Contact Us").click()
        setup.find_element(By.ID, "name").send_keys("Hadeel")
        setup.find_element(By.ID, "email").send_keys("hadeelhassan186@gmail.com")
        setup.find_element(By.ID, "message").send_keys("Hi")
        setup.find_element(By.XPATH, "//input[@value='Submit']").click()
        assert setup.current_url.endswith("/contact"), "Page URL does not match "