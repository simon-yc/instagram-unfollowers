import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from credentials import USERNAME, PASSWORD


class Instagram:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)
        self.browser.get("https://www.instagram.com")

    def close_browser(self):
        self.browser.close()
        self.browser.quit()

    def login(self):
        print("Attemping login...")
        try:
            username_input = self.browser.find_element(By.NAME, "username")
            username_input.send_keys(USERNAME)
            password_input = self.browser.find_element(By.NAME, "password")
            password_input.send_keys(PASSWORD)
            login_button = self.browser.find_element(By.TAG_NAME, "form")
            login_button.submit()
            print("Login was successful")
        except Exception as ex:
            print("Login failed")
            print(f"exception: {ex}")
            self.close_browser()


instance = Instagram()
instance.login()
