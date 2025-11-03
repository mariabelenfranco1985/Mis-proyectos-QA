import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LoginTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login_valido(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        
        # Credenciales válidas
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        
        # Verificar que accedió al inventario
        self.assertIn("inventory", driver.current_url)
        print("✅ Login válido exitoso")

    def test_login_invalido(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        
        # Credenciales inválidas
        driver.find_element(By.ID, "user-name").send_keys("usuario_invalido")
        driver.find_element(By.ID, "password").send_keys("clave_erronea")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        
        # Verificar mensaje de error
        mensaje_error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        self.assertIn("Epic sadface", mensaje_error)
        print("❌ Login inválido correctamente detectado")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
