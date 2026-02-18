'''Test Scenario: Verify Table Data Integrity

Objective:
Validate specific row data within a web table.

Steps:
    1. Navigate to the tables page.
    2. Locate Table 1.
    3. Identify the row containing the first name "Jason".
    4. Verify that the email address is correct.
    5. The due amount matches the expected value.

Expected Result:
The correct row is found and the data matches expected values.
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = 'https://the-internet.herokuapp.com/tables'

class TestTableHandling:

    TABLE1 = (By.ID, 'table1')
    TABLE1_ROWS = (By.XPATH, '//table[@id="table1"]/tbody/tr')
    TABLE1_CELL = (By.TAG_NAME, 'td')

    def setup_method(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument("window-position=0,0")
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(URL)
        self.wait = WebDriverWait(self.browser, 5)

    def teardown_method(self):
       self.browser.close()

    def test_table_handling(self):
        # Find all rows in table1 (excluding header)
        rows = self.browser.find_elements(*self.TABLE1_ROWS)

        # Find the row of Jason
        jason_row = None
        for row in rows:
            if 'Jason' in row.text:
                jason_row = row
                break
        assert jason_row is not None, 'Jason row was not found in the table'

        # Find the row of Jason
        cells_of_jason_row = jason_row.find_elements(*self.TABLE1_CELL)

        # Find cell values
        first_name = cells_of_jason_row[1].text
        email = cells_of_jason_row[2].text
        due = cells_of_jason_row[3].text

        # Verify name, email address and amount due and define AssertionError message
        assert first_name == 'Jason', 'First name was not correct.'
        assert email == 'jdoe@hotmail.com', 'Email address was not correct.'
        assert due == '$100.00', 'Due value was not correct.'






