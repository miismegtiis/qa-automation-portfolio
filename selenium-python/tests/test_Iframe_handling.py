'''Test Scenario: Interact with Text Editor Inside an Iframe

Objective:
Verify interaction with elements inside an iframe.

Steps:
    1. Navigate to the iframe page.
    2. Switch to the iframe.
    3. Clear the existing text.
    4. Enter new text.
    5.Verify the text is updated correctly.
    6. Switch back to the main content.

Expected Result:
The editor displays the newly entered text.
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://the-internet.herokuapp.com/iframe"

class TestDynamicButtonsDisabled:

    def setup_method(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument("window-position=0,0")

        self.browser = webdriver.Chrome(options=options)
        self.browser.get(URL)
        self.wait = WebDriverWait(self.browser, 5)

    def teardown_method(self):
       self.browser.close()

    def test_iframe(self):

        iframe_cookies =
        button_do_not_consent =
        '''alert_button = self.browser.find_element(By.XPATH, '//*/div[@role="alert"]/button')
        alert_button.click()

        iframe = self.browser.find_element(By.ID, 'mce_0_ifr')
        self.browser.switch_to.frame(iframe)
        textarea = self.browser.find_element(By.ID, 'tinymce')
        textarea.click()
        textarea.clear()
        textarea.send_keys('The old pond \nA frog leaps in. \nSound of the water \nMatsuo Bashu')

        assert 'The old pond \nA frog leaps in. \nSound of the water \nMatsuo Bashu' in textarea.text

#website is not free, need another one'''