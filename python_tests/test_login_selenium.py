import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestGoogleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_busqueda_google(self):
        driver = self.driver
        driver.get("https://www.google.com")
        driver.maximize_window()

        # Buscar "María Belén Franco QA"
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("María Belén Franco QA")
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)

        # Validar que haya resultados
        resultados = driver.find_elements(By.CSS_SELECTOR, "div.g")
        self.assertTrue(len(resultados) > 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

