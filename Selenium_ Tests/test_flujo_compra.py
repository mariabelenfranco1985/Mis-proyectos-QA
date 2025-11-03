import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class PruebaFlujoCompra(unittest.TestCase):

    def setUp(self):
        # Configuración inicial del navegador
        opciones = Options()
        opciones.add_argument("--start-maximized")
        servicio = Service()
        self.navegador = webdriver.Chrome(service=servicio, options=opciones)
        self.espera = WebDriverWait(self.navegador, 10)

    def test_flujo_de_compra_completo(self):
        navegador = self.navegador
        espera = self.espera

        # Paso 1: Ingresar al sitio web
        navegador.get("https://www.saucedemo.com/")

        # Paso 2: Iniciar sesión con credenciales válidas
        espera.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        navegador.find_element(By.ID, "password").send_keys("secret_sauce")
        navegador.find_element(By.ID, "login-button").click()

        # Paso 3: Agregar dos productos al carrito
        espera.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        espera.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light"))).click()

        # Paso 4: Ir al carrito
        espera.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

        # Paso 5: Verificar que haya productos en el carrito
        try:
            productos = espera.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))
            cantidad_productos = len(productos)
            self.assertGreater(cantidad_productos, 0)
            print(f"🛒 Se agregaron {cantidad_productos} productos al carrito correctamente.")
        except TimeoutException:
            self.fail("❌ No se encontraron productos en el carrito.")

        # Paso 6: Hacer clic en “Checkout”
        navegador.find_element(By.ID, "checkout").click()

        # Paso 7: Completar los datos del comprador
        espera.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Maria")
        navegador.find_element(By.ID, "last-name").send_keys("Franco")
        navegador.find_element(By.ID, "postal-code").send_keys("1629")
        navegador.find_element(By.ID, "continue").click()

        # Paso 8: Finalizar la compra
        espera.until(EC.presence_of_element_located((By.ID, "finish"))).click()

        # Paso 9: Verificar mensaje de confirmación
        mensaje_confirmacion = espera.until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        ).text
        self.assertIn("THANK YOU", mensaje_confirmacion.upper())
        print("✅ La compra se completó correctamente y fue confirmada en pantalla.")

    def tearDown(self):
        # Cierra el navegador al finalizar la prueba
        self.navegador.quit()


if __name__ == "__main__":
    unittest.main()
