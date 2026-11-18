"""
Experiment 3.b: Automated Form Testing using Selenium in Python
Tests the Student Registration Form deployed in Docker or locally via file URL.
Validates input entry, dropdown selection, and successful submission assertions.
"""

import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def get_driver():
    """Attempt to initialize Chrome, fallback to Edge if Chrome is unavailable."""
    # Try Chrome first
    try:
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        print("[Driver] Initialized Chrome WebDriver successfully (Headless).")
        return driver
    except Exception as e_chrome:
        print(f"[Driver Warning] Chrome init failed ({e_chrome}). Trying Microsoft Edge...")

    # Fallback to Microsoft Edge (Default on Windows)
    try:
        edge_options = EdgeOptions()
        edge_options.add_argument("--headless=new")
        edge_options.add_argument("--disable-gpu")
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=edge_options)
        print("[Driver] Initialized Edge WebDriver successfully (Headless).")
        return driver
    except Exception as e_edge:
        print(f"[Driver Error] Edge init failed: {e_edge}")
        raise RuntimeError("No supported browser driver found. Please install Chrome or Edge.")

def run_test(target_url: str):
    print("=" * 60)
    print("      DevOps Lab - Selenium Automated Form Testing      ")
    print("=" * 60)
    print(f"[Target URL] {target_url}\n")

    driver = get_driver()
    try:
        # Step 1: Open Target URL
        print("Step 1: Navigating to student registration form...")
        driver.get(target_url)
        time.sleep(1)

        # Step 2: Locate form elements
        print("Step 2: Locating input fields...")
        name_input   = driver.find_element(By.ID, "fullName")
        email_input  = driver.find_element(By.ID, "email")
        phone_input  = driver.find_element(By.ID, "phone")
        dob_input    = driver.find_element(By.ID, "dob")
        gender_select= Select(driver.find_element(By.ID, "gender"))
        course_select= Select(driver.find_element(By.ID, "course"))
        submit_btn   = driver.find_element(By.ID, "submitBtn")

        # Step 3: Fill out test data
        print("Step 3: Entering student registration details...")
        name_input.send_keys("Alex Morgan")
        email_input.send_keys("alex.morgan@university.edu")
        phone_input.send_keys("9876543210")
        dob_input.send_keys("2002-05-15")
        gender_select.select_by_value("Male")
        course_select.select_by_value("Computer Science & Engineering")

        # Step 4: Submit form
        print("Step 4: Clicking 'Register Student' submit button...")
        submit_btn.click()

        # Step 5: Verify success message
        print("Step 5: Waiting for status response...")
        wait = WebDriverWait(driver, 5)
        status_el = wait.until(
            EC.visibility_of_element_located((By.ID, "statusMessage"))
        )

        status_text = status_el.text.strip()
        print(f"\n[Observed Message] \"{status_text}\"")

        # Assertion
        expected_msg = "Student registered successfully!"
        assert expected_msg in status_text, f"Assertion Failed: Expected '{expected_msg}', got '{status_text}'"

        print("\n" + "=" * 60)
        print("TEST PASSED: Student Registration Form successfully validated via Selenium!")
        print("=" * 60)

    finally:
        driver.quit()
        print("\n[Browser] WebDriver session closed.")

if __name__ == "__main__":
    # Determine test target (Docker URL or local file)
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        # Default to local HTML file path if Docker is not specified
        local_html = os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html"))
        target = f"file:///{local_html.replace(os.sep, '/')}"

    run_test(target)
