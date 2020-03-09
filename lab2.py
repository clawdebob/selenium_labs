import unittest
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Labs(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_convert_tables(self):
        writer = pd.ExcelWriter('output/output.xlsx', engine='xlsxwriter')
        driver = self.driver
        main_link = "http://ab-w.net/HTML/table.php"
        tag = "table"
        driver.get(main_link)
        self.assertIn("Создание таблиц в HTML", driver.title)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, tag))
        )
        tables = driver.find_elements_by_css_selector("table[border]")
        for idx, element in enumerate(tables):
            source = "<table>" + element.get_attribute("innerHTML") + "</table>"
            data = pd.read_html(source)
            data[0].to_excel(writer, sheet_name = "Table " + str(idx + 1))
        writer.save()



if __name__ == "__main__":
    unittest.main()
