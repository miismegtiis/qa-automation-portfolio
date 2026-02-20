'''Test Case 1 – Single Iframe Interaction
Steps:

    1. Navigate to the Frames page.
    2. Click on the "Single Iframe" tab.
    3. Switch to the displayed iframe.
    4. Enter text into the input field inside the iframe.
    5. Verify that the entered text is displayed correctly.
    6. Switch back to the main page content.

Expected Result:

The text is successfully entered inside the iframe input field.

Test Case 2 – Nested Iframe Interaction
Steps:

    1. Click on the "Iframe with in an Iframe" tab.
    2. Switch to the outer iframe.
    3. Switch to the inner iframe.
    4. Enter text into the input field.
    5. Verify that the text appears correctly.
    6. Switch back to default content.

Expected Result:

The text is successfully entered inside the nested iframe structure.
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://demo.automationtesting.in/Frames.html"

class TestIframeHandling:

    TAB_SINGLE = (By.XPATH, '//a[text()="Single Iframe "]')
    TAB_NESTED = (By.XPATH, '//li/a[@href="#Multiple"]')

    SINGLE_IFRAME = (By.ID, "singleframe")
    OUTER_IFRAME = (By.XPATH, '//iframe[@src="MultipleFrames.html"]')
    INNER_IFRAME = (By.XPATH, '//iframe[@src="SingleFrame.html"]')

    INPUT_FIELD = (By.XPATH, '//input[@type="text"]')

    def setup_method(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument("window-position=0,0")

        self.browser = webdriver.Chrome(options=options)
        self.browser.get(URL)
        self.wait = WebDriverWait(self.browser, 5)

    def teardown_method(self):
       self.browser.close()

    # Helper function for handling cookie consent window using try and except, since it might not pop up
    def cookie_cookie_handling(self):
        try:
            button_cookie = self.browser.find_element(By.XPATH, '//div[@class="fc-footer-buttons"]/button[@aria-label="Do not consent"]')
            button_cookie.click()
        except:
            pass

    def test_single_iframe(self):
        # Deal with cookies
        self.cookie_cookie_handling()

        # Select single iframe, find the tab, click and switch to iframe
        tab_single_iframe = self.wait.until(EC.element_to_be_clickable(self.TAB_SINGLE))
        tab_single_iframe.click()

        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.SINGLE_IFRAME))

        # Find the input field inside the iframe and enter text
        input_in_iframe = self.browser.find_element(*self.INPUT_FIELD)
        input_in_iframe.send_keys('Hello')

        # Verify that the entered text is displayed correctly.
        assert input_in_iframe.get_attribute('value') == 'Hello'

        # Switch back to the main page content
        self.browser.switch_to.default_content()

    def test_nested_iframe(self):
        # Deal with cookies
        self.cookie_cookie_handling()

        # Select Iframe with in an Iframe, find the tab, click and switch to the outer iframe
        tab_nested_iframe = self.wait.until(EC.element_to_be_clickable(self.TAB_NESTED))
        tab_nested_iframe.click()

        # Switch to the outer iframe.
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.OUTER_IFRAME))

        #Switch to the inner iframe.
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.INNER_IFRAME))

        # Find the input field inside the iframe and enter text
        input_in_inner_iframe = self.wait.until(element_to_be_clickable(self.INPUT_FIELD))
        input_in_inner_iframe.send_keys('Hello')

        # Verify that the entered text is displayed correctly.
        assert input_in_inner_iframe.get_attribute('value') == 'Hello'

        # Switch back to the main page content
        self.browser.switch_to.default_content()