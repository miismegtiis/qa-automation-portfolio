'''Test Scenario: Verify Dynamically Loaded Content

Objective:
Ensure that dynamically loaded content appears after triggering the loading process.

Steps:
    1. Navigate to the dynamic loading page.
    2. Click the "Start" button.
    3. Wait until the hidden content becomes visible.
    4. Verify the text "Hello World!" is displayed.

Expected Result:
The dynamically loaded text appears and matches the expected value.
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = 'https://the-internet.herokuapp.com/dynamic_loading/1'

class TestDynamicLoading:

    START_BUTTON = (By.XPATH, '//*/div[@id="start"]/button')
    FINISH_RESULT = (By.XPATH, '//*/div[@id="finish"]/h4')

    def setup_method(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument("window-position=0,0")
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(URL)
        self.wait = WebDriverWait(self.browser, 10)

    def teardown_method(self):
       self.browser.close()

    def test_dynamic_loading(self):
        # Find and click 'Start' button
        button_start = self.browser.find_element(*self.START_BUTTON)
        button_start.click()
        # Wait until the hidden element appears on the page
        hidden_element = self.wait.until(EC.visibility_of_element_located(self.FINISH_RESULT))

        # Verify the visibility and the content of the appearing text
        assert hidden_element.is_displayed
        assert 'Hello World!' == hidden_element.text

