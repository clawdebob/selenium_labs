import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Labs(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_links_on_site(self):
        driver = self.driver
        main_link = "https://sumirea.ru/"
        link_selector = "a[href*='http']"
        links_values_list = []
        new_tab = Keys.CONTROL + Keys.ENTER
        close_tab = Keys.CONTROL + 'w'
        get_href_func = lambda link: link.get_attribute("href")
        
        driver.get(main_link)
        self.assertIn(main_link, driver.current_url)
        self.assertIn("ММОО «Студенческий союз МИРЭА»", driver.title)

        links = driver.find_elements_by_css_selector(link_selector)
        sorted_links_list = sorted(links, key = get_href_func)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, link_selector))
        )
        for link in sorted_links_list:
            link.send_keys(new_tab)
            link_value = get_href_func(link).replace("http:", "https:")
            links_values_list.append(link_value)

        links_values_list.reverse()
        links_values_list.insert(0, main_link)

        for idx, tab in enumerate(driver.window_handles):
            driver.switch_to.window(tab)
            self.assertIn(links_values_list[idx], driver.current_url)
            driver.close()

if __name__ == "__main__":
    unittest.main()
