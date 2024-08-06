import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re

auth_page = "https://academic.ui.ac.id/main/Authentication/"
course_plan_page = "file:///Users/hilmirusydi/EpakSIAK/SiakWar/testground/Penambahan%20IRS%20-%20Dennis%20Al%20Baihaqi%20Walangadi%20(1906400141)%3B%20Kurikulum%2009.00.12.01-2016%20-%20SIAK%20NG.html"
def setup_driver():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=options)
    return driver

def load_config(config_file):
    config = {}
    with open(config_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("username:"):
                config['username'] = line.split("username:")[1].strip()
            elif line.startswith("password:"):
                config['password'] = line.split("password:")[1].strip()
            elif line.startswith("matkul_code:"):
                config['matkul_code'] = []
            elif config.get('matkul_code') is not None:
                config['matkul_code'].append(line)
    return config

def login(driver, username, password):
    print("Logging in...")
    driver.get(auth_page)
    
    # Enter username and password and submit the form
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "u"))).send_keys(username)
    driver.find_element(By.NAME, "p").send_keys(password)
    driver.find_element(By.NAME, "p").send_keys(Keys.RETURN)
    
    try:
        # Wait for either the welcome URL or the login failed message
        WebDriverWait(driver, 20).until(
            lambda d: "Welcome" in d.current_url or d.find_element(By.XPATH, '//p[@class="error" and text()="Login Failed"]')
        )
    except TimeoutException:
        return False
    
    if "Welcome" in driver.current_url:
        print("Logged in successfully!")
        driver.get(course_plan_page)
        WebDriverWait(driver, 20).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )
        print("Navigated to Course Plan page!")
        return True



def show_error_message(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Login Error", message)
    root.destroy()

def check_for_sks(driver):
    retry_count = 0
    while True:
        retry_count += 1
        try:
            WebDriverWait(driver, 20).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
            if re.search(r'sks', driver.page_source, re.IGNORECASE):
                print("SKS found!")
                print(f"Total retry attempts: {retry_count}")
                break
            else:
                print(f"Reloading, unable to find SKS... Retry attempt: {retry_count}")
                driver.refresh()
        except Exception as e:
            print(f"An error occurred while checking for SKS: {e}")
            driver.refresh()

def select_radio_buttons(driver, matkul_code):
    matkul_len = len(matkul_code)
    cnt = 0
    not_found = []
    
    print('Matkul picked:')
    for code in matkul_code:
        print(code)
    print(matkul_len)

    for code in matkul_code:
        code_without_dash = code.split('-')[0]
        found = False
        
        # Try to find the radio button using the exact value
        try:
            element = driver.find_element(By.XPATH, f'//input[@type="radio"][@value="{code}"]')
            print(f"Found using value! {element.get_attribute('value')}")
            cnt += 1
            if not element.is_selected():
                print("Clicking!")
                element.click()
            found = True
        except:
            pass  # Ignore errors and proceed to the next method

        # If not found by value, try using the title
        if not found:
            try:
                element = driver.find_element(By.XPATH, f'//input[@type="radio"][@title="{code_without_dash}"]')
                print(f"Found using title! {element.get_attribute('title')}")
                cnt += 1
                if not element.is_selected():
                    print("Clicking!")
                    element.click()
                found = True
            except:
                pass  # Ignore errors and proceed to the next method

        # If still not found, try using part of the URL
        if not found:
            try:
                element = driver.find_element(By.XPATH, f'//input[@type="radio"][@href[contains(., "cc={code_without_dash}")]]')
                print(f"Found using URL! {element.get_attribute('href')}")
                cnt += 1
                if not element.is_selected():
                    print("Clicking!")
                    element.click()
                found = True
            except:
                pass  # Ignore errors and proceed

        if not found:
            not_found.append(code)

    if not_found:
        print(f"Warning: The following codes were not found: {', '.join(set(not_found))}")
        print("Skipping form submission due to missing codes.")
    else:
        print(f"Checked {cnt} items.")
        # Auto-submit after selecting all radio buttons
        try:
            button = driver.find_element(By.XPATH, "//input[@value='Simpan IRS']")
            print("Submitting form...")
            button.click()
            print("Form submitted!")
        except Exception as e:
            print(f"Error finding or clicking the submit button: {e}")



def process_page(driver, username, password, matkul_code):
    if not login(driver, username, password):
        show_error_message("Login failed. Please check your username and password in config.txt")
        print("Login failed. Please check your username and password on config.txt")
        return  # Exit if login was unsuccessful

    # Check for SKS and perform further actions
    check_for_sks(driver)
    select_radio_buttons(driver, matkul_code)
    
    print("Process finished! Press enter to exit...")
    input()
    driver.quit()


if __name__ == "__main__":
    print("EpakSIAK Testing - May we win the war")
    print("Starting...")
    config = load_config('configtest.txt')
    
    driver = setup_driver()

    username = config.get('username')
    password = config.get('password')
    matkul_code = config.get('matkul_code')

    print(f"Loaded username: {username}")
    print(f"Loaded password: {password}")
    print(f"Loaded matkul codes: {matkul_code}")

    process_page(driver, username, password, matkul_code)
