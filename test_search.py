from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("setup")
class TestSearch:
    def test_search(self, setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "//input[@placeholder='Enter search keywords']").send_keys("Kelly")
        setup.find_element(By.CSS_SELECTOR, "input[value='search']").click()
        print("Passed!")
        assert len(setup.find_elements(By.XPATH,"(//a)[6]")) == 1, "You didn't get anything"
        print("Passed!")
        link_element = setup.find_element(By.XPATH, "(//a)[6]")
        assert "Kelly" in link_element.text, "Search results do not match the search keywords"