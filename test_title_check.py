from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_title(self, setup):
        setup.get("http://127.0.0.1:5000")
        print(setup.find_element(By.XPATH, "//div[@class='logo']").text)
        assert setup.find_element(By.XPATH, "//div[@class='logo']").text == "Powerful women in Tech"