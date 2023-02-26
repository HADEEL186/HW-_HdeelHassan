from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("setup")
class TestAddProfile:
    def test_add(self, setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "//a[@href='add_profile']").click()
        setup.find_element(By.XPATH, "//input[@name='filename']").send_keys("C:/Users/97252/OneDrive/שולחן העבודה/projectphoto/x.jpg")
        setup.find_element(By.CSS_SELECTOR, "input[name*='rate']").send_keys("4")
        setup.find_element(By.CSS_SELECTOR, "input[type='text'][name$='name']").send_keys("NOURA")
        setup.find_element(By.CSS_SELECTOR, "input[name*='position']").send_keys("founder")
        setup.find_element(By.CSS_SELECTOR, "input[name*='company']").send_keys("ADF")
        setup.find_element(By.CSS_SELECTOR, "input[name*='country']").send_keys("Isreal")
        setup.find_element(By.CSS_SELECTOR, "input[name*='birth_date']").send_keys("5/5/1991")
        setup.find_element(By.XPATH, "//textarea[@placeholder='Enter information']").send_keys("wonderful")
        setup.find_element(By.XPATH, "//button[@type='submit']").click()
        assert setup.current_url == "http://127.0.0.1:5000", "The test faild"

