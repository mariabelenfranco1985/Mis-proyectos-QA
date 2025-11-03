import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class PruebaAgregarProductoCarrito(unittest.TestCase):

    def setUp(self):
        # Configuración inicial del navegador
        self.navegador = webdriver.Chrome()
        self.navegador.maximize_window()

    def test_agregar_producto_al_carrito(self):
        navegador = self.navegador
        navegador.get("https://www.saucedemo.com/")

        # Paso 1: Iniciar sesión con credenciales válidas
        navegador.find_element(By.ID, "user-name").send_keys("standard_user")
        navegador.find_element(By.ID, "password").send_keys("secret_sauce")
        navegador.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # Paso 2: Agregar producto al carrito
        navegador.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)

        # Paso 3: Ir al carrito
        navegador.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)

        # Paso 4: Verificar que el producto se agregó correctamente
        nombre_producto = navegador.find_element(By.CLASS_NAME, "inventory_item_name").text
        self.assertEqual(nombre_producto, "Sauce Labs Backpack")
        print("🎒 El producto fue agregado al carrito correctamente.")

    def tearDown(self):
        # Cierra el navegador al finalizar
        self.navegador.quit()

if __name__ == "__main__":
    unittest.main()
