import unittest
import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Labs(unittest.TestCase):

    def setUp(self):
        option = Options()

        option.add_argument("--disable-infobars")
        option.add_experimental_option("prefs", { 
            "profile.default_content_setting_values.notifications": 1 
        })

        self.driver = webdriver.Chrome(options=option)

    def test_get_friend_online(self):
        driver = self.driver
        main_link = "https://www.facebook.com/"
        driver.get(main_link)
        self.assertIn("Facebook", driver.title)
        login_input = driver.find_element_by_id("email")
        password_input = driver.find_element_by_id("pass")
        login_button = driver.find_element_by_id("loginbutton")
        login = input("Login: ")
        password = getpass("Password: ")
        login_input.send_keys(login)
        password_input.send_keys(password)
        login_button.click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "mercurymessages"))
        )
        messager = driver.find_element_by_name("mercurymessages")
        messager.click()
        go_to_messager = driver.find_element_by_css_selector("a[href='/messages/t/']")
        go_to_messager.click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "js_2q"))
        )
        settings = driver.find_element_by_id("js_2q")
        settings.click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "__MenuItem"))
        )
        active = driver.find_elements_by_class_name("__MenuItem")[2]
        active.click()
        online = driver.find_elements_by_css_selector("#js_23 ._8slc")
        online_list = []
        for item in online:
            online_list.append(item.get_attribute("text"))
        print(online_list)

if __name__ == "__main__":
    unittest.main()
