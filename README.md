# QA Automation Portfolio – Kamilla Hegyi
This repository contains automated UI tests written in **Python** using **Selenium WebDriver** and **Pytest**.

# Project Overview
The purpose of this project is to demonstrate practical web automation skills by covering common real-world UI scenarios such as login validation, iframe interaction, file uploads, dynamic elements, alerts, and table handling.

The goal of this repository is to demonstrate:
- understanding of basic automation testing concepts
- structured test organization
- clean and readable test scripts
- ability to work with Git and version control
- understanding of synchronization and wait strategies in UI automation

The test projects are based on practice web applications,
including training environments and a school-developed hotel booking application.

All examples are for educational purposes.

## Selenium Automation Practice Project
Each test file includes detailed test case descriptions, test steps, and expected results.
This project focuses on building a strong and stable automation foundation before moving to more advanced design patterns such as Page Object Model (POM).

---

## Technologies Used

- Python 3.13  
- Selenium WebDriver  
- Pytest
- ChromeDriver  
- WebDriverWait & Expected Conditions  

---

## Test Coverage

### 🔐 test_login
- Valid login verification
- Element locating strategies
- Authentication validation
- Assertion-based verification

### 🖼 test_iframe_handling
- Switching to single iframe
- Handling nested iframes (iframe within iframe)
- Switching back to default content
- Validating input values inside iframe context
- Handling cookie consent overlays

### 📤 test_file_upload
- Uploading files via input element
- Verifying uploaded file name
- Handling local file paths

### 📊 test_table_handling
- Locating table elements
- Iterating through rows and cells
- Validating specific row data
- Working with structured table content

### ⚠️ test_alerts_handling
- Handling JavaScript alerts
- Accepting and dismissing alerts
- Validating alert text
- Switching between alert and page context

### 🔘 test_dynamic_buttons_disabled
- Interacting with dynamically enabled/disabled buttons
- Waiting for element state changes
- Verifying button state transitions

### ⏳ test_dynamic_loading
- Handling dynamically loaded elements
- Using explicit waits for asynchronous content
- Verifying visibility after loading completes

---

## Key Automation Concepts Demonstrated

- Explicit waits for test stability  
- Handling dynamic elements and asynchronous content  
- Proper iframe switching and context management  
- Alert handling  
- Cookie consent overlay handling  
- File upload automation  
- Table data validation  
- Clean test structure using setup and teardown methods  
- Assertion-based validation  

---

## Project Structure

```
tests/
    test_alerts_handling.py
    test_dynamic_buttons_disabled.py
    test_dynamic_loading.py
    test_file_upload.py
    test_iframe_handling.py
    test_login.py
    test_table_handling.py
requirements.txt
README.md
```

---

## How to Run the Tests

1. Clone the repository:
```
git clone <your-repo-url>
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run all tests:
```
pytest
```

4. Run a specific test file:
```
pytest tests/test_iframe_handling.py
```

---

## Purpose of This Project

This project was created to strengthen hands-on Selenium automation skills and to build a structured automation portfolio.

It demonstrates the ability to automate realistic UI interactions and manage common web automation challenges such as dynamic elements, iframe handling, file operations, and alert management.

Future improvements may include:
- Refactoring to Page Object Model (POM)
- Introducing fixtures for setup and teardown
- Adding reporting tools
- Expanding test coverage
- Integrating CI pipelines
