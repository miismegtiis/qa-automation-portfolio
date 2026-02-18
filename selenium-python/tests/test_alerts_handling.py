'''Test Scenario: Handle JavaScript Alerts

Objective:
Verify correct handling of JavaScript alert dialogs.

Steps:
    1. Navigate to the JavaScript Alerts page.
    2. Click the "Click for JS Alert" button.
    3. Accept the alert.
    4. Verify the result message.

Additional Scenarios:
    1. Handle JS Confirm by accepting and dismissing.
    2. Handle JS Prompt by entering text and verifying the result.

Expected Result:
The correct confirmation message is displayed after interacting with each alert type.'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


URL = "https://the-internet.herokuapp.com/javascript_alerts"

class TestAlertsHandling:

    def setup_method(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(URL)
        self.wait = WebDriverWait(self.browser, 10)

    def teardown_method(self):
       self.browser.close()

    def test_js_alerts(self):
        # Find and click 'CLick for JS Alert' button
        button_click_for_js_alert = self.browser.find_element(By.XPATH, '//button[text()="Click for JS Alert"]')
        button_click_for_js_alert.click()

        # Switch to alert and press ok
        alert = self.browser.switch_to.alert
        alert.accept()

        # Verify correctness of the appearing feedback
        result_text = self.wait.until(EC.visibility_of_element_located((By.ID, 'result')))
        assert result_text.text == 'You successfully clicked an alert'

    def test_js_confirm_accept(self):
        # Find and click 'Click for JS Confirm' button
        button_click_for_js_confirm = self.browser.find_element(By.XPATH, '//button[text()="Click for JS Confirm"]')
        button_click_for_js_confirm.click()

        # Switch to alert and press ok
        alert = self.browser.switch_to.alert
        alert.accept()

        # Verify correctness of the appearing feedback
        result_text = self.wait.until(EC.visibility_of_element_located((By.ID, 'result')))
        assert result_text.text == 'You clicked: Ok'

    def test_js_confirm_dismiss(self):
        # Find and click 'CLick for JS Confirm' button
        button_click_for_js_confirm = self.browser.find_element(By.XPATH, '//button[text()="Click for JS Confirm"]')
        button_click_for_js_confirm.click()

        # Switch to alert and press Cancel
        alert = self.browser.switch_to.alert
        alert.dismiss()

        # Verify correctness of the appearing feedback
        result_text = self.wait.until(EC.visibility_of_element_located((By.ID, 'result')))
        assert result_text.text == 'You clicked: Cancel'

    def test_js_prompt(self):
        # Find and click 'Click for JS Prompt' button
        button_click_for_js_confirm = self.browser.find_element(By.XPATH, '//button[text()="Click for JS Prompt"]')
        button_click_for_js_confirm.click()

        # Switch to alert, enter input text and press Ok
        alert = self.browser.switch_to.alert
        alert.send_keys('Hi, I am Milla')
        alert.accept()

        # Verify correctness of the appearing feedback
        result_text = self.wait.until(EC.visibility_of_element_located((By.ID, 'result')))
        assert result_text.text == 'You entered: Hi, I am Milla'

