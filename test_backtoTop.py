from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest


@pytest.mark.usefixtures("setup")
class TestBackTop:
    def test_back_top(self, setup):
        setup.get("http://127.0.0.1:5000")
        setup.execute_script("window.scrollBy(0,document.body.scrollHeight);")
        setup.get_screenshot_as_file("bottom.png")
        setup.execute_script("window.scrollTo(0,0);")
        setup.get_screenshot_as_file("top.png")
        setup.find_element(By.LINK_TEXT, "Back to top").click()
        assert setup.execute_script("return window.scrollY") == 0, "Back to top button did not work"