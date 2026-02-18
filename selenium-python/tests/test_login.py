"""
Login tests practice:
    Test case 1: Positive LogIn test
    Test case 2: Negative username test
    Test case 3: Negative password test
    """

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://practicetestautomation.com/practice-test-login/"

class TestLogin:

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "submit")
    ERROR = (By.ID, "error")
    LOGOUT = (By.XPATH, '//a[text()="Log out"]')

    def setup_method(self):
        options = Options()
        options.add_argument("--start-maximized")
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(URL)
        self.wait = WebDriverWait(self.browser, 5)

    def teardown_method(self):
        self.browser.quit()

    # Helper method
    def login(self, username, password):
        self.browser.find_element(*self.USERNAME).send_keys(username)
        self.browser.find_element(*self.PASSWORD).send_keys(password)
        self.browser.find_element(*self.SUBMIT).click()

    def test_login_positive(self):
        # Proceed with login through the helper function with correct login data and find the logout link element for later assertion
        self.login("student", "Password123")
        link_logout = self.wait.until(EC.visibility_of_element_located(self.LOGOUT))

        # Assert successful login in different ways
        assert link_logout.text == "Log out"
        assert link_logout.is_displayed()
        assert "logged-in-successfully" in self.browser.current_url

    def test_login_negative_incorrect_user(self):
        # Proceed with login through the helper function with incorrect username and find the error message element for later assertion
        self.login("incorrectUser", "Password123")
        error_message = self.wait.until(EC.visibility_of_element_located(self.ERROR))

        # Assert the appearance of the error message in different ways
        assert error_message.is_displayed()
        assert error_message.text == "Your username is invalid!"
        assert "practice-test-login" in self.browser.current_url

    def test_login_negative_incorrect_pw(self):
        # Proceed with login through the helper function with incorrect password and find the error message element for later assertion
        self.login("student", "incorrectPassword")
        error_message = self.wait.until(EC.visibility_of_element_located(self.ERROR))

        # Assert the appearance of the error message in different ways
        assert error_message.is_displayed()
        assert error_message.text == "Your password is invalid!"
        assert "practice-test-login" in self.browser.current_url
