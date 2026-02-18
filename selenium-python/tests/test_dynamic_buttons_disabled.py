"""
Test Scenario:
Click all dynamically enabled buttons and verify the success message.

Target URL:
https://testpages.eviltester.com/styled/dynamic-buttons-disabled.html
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://testpages.eviltester.com/styled/dynamic-buttons-disabled.html"


class TestDynamicButtonsDisabled:

    def setup_method(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--guest")
        options.add_argument("language=en")
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(URL)


    def teardown_method(self):
        self.browser.quit()

    def test_all_buttons_clicked_disabled(self):
        wait = WebDriverWait(self.browser, 20)

        # Click buttons sequentially as they become enabled
        wait.until(EC.element_to_be_clickable((By.ID, "button00"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "button01"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "button02"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "button03"))).click()

        # Verify success message
        message = wait.until(
            EC.visibility_of_element_located((By.ID, "buttonmessage"))
        )

        assert message.text == "All Buttons Clicked"
