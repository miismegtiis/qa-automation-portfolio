'''Test Scenario: Verify File Upload Functionality

Objective:
Validate that a user can successfully upload a file and that the uploaded file name is displayed correctly after submission.

Steps:
    1. Navigate to the File Upload page.
    2. Locate the file input field.
    3. Select a file from the local system.
    4. Click the "Upload" button.
    5. Verify that the upload confirmation page is displayed.
    6. Verify that the uploaded file name matches the selected file.

Expected Result:
The file is uploaded successfully and the correct file name is displayed on the confirmation page.
'''

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = 'https://the-internet.herokuapp.com/upload'

class TestFileUpload:

    FILE_INPUT = (By.ID, 'file-upload')
    BUTTON_UPLOAD = (By.ID, 'file-submit')
    UPLOADED_FILES = (By.ID, 'uploaded-files')

    def setup_method(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument("window-position=0,0")
        options.add_argument("--guest")
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(URL)
        self.wait = WebDriverWait(self.browser, 10)

    def teardown_method(self):
       self.browser.close()

    def test_file_upload(self):

        # Create test file
        file_name = 'test_upload.txt'
        file_path = os.path.join(os.getcwd(), file_name)

        with open(file_name, 'w') as f:
            f.write('this is a .txt file for Selenium upload for test_file_upload.py')

        # Upload file
        self.browser.find_element(*self.FILE_INPUT).send_keys(file_path)
        self.browser.find_element(*self.BUTTON_UPLOAD).click()

        # Verify upload success
        uploaded = self.wait.until(EC.visibility_of_element_located(self.UPLOADED_FILES))

        assert uploaded.text == file_name

        # Cleanup
        os.remove(file_name)