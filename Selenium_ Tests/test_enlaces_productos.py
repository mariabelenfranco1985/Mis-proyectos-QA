import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class PruebaEnlacesProductos(unittest.TestCase):

    def setUp(self):
        # Configuración del navegador
        opciones = Options()
        opciones.add_argument("--start-maximized")
        servicio = Service()
        self.navegador = webdriver.Chrome(service=servicio, options=opciones)
        self.espera = WebDriverWait(self.navegador, 10)

    def test_verificar_enlaces_productos(self):
        navegador = self.navegador
        espera = self.espera

        # Paso 1: Ingresar al sitio
        navegador.get("https://www.saucedemo.com/")

        # Paso 2: Iniciar sesión
        espera.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        navegador.find_element(By.ID, "password").send_keys("secret_sauce")
        navegador.find_element(By.ID, "login-button").click()

        # Paso 3: Esperar que se carguen los productos
        espera.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))

        # Paso 4: Obtener los nombres de los productos
        productos = navegador.find_elements(By.CLASS_NAME, "inventory_item_name")
        nombres_productos = [p.text for p in productos]
        print(f"🔍 Se encontraron {len(nombres_productos)} productos en la página principal.")

        # Paso 5: Recorrer la lista de nombres
        for nombre in nombres_productos:
            print(f"➡️ Probando enlace del producto: {nombre}")

            # Refrescar lista de productos antes de cada clic
            espera.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))
            enlaces = navegador.find_elements(By.CLASS_NAME, "inventory_item_name")

            # Buscar el producto actual en la lista actualizada
            for enlace in enlaces:
                if enlace.text == nombre:
                    enlace.click()
                    break

            # Esperar el título del detalle del producto
            titulo_detalle = espera.until(
                EC.presence_of_element_located((By.CLASS_NAME, "inventory_details_name"))
            ).text

            # Validar que el título coincide con el producto
            self.assertEqual(nombre, titulo_detalle)
            print(f"✅ Enlace del producto '{nombre}' funciona correctamente.")

            # Volver a la lista
            navegador.back()
            espera.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))

        print("🎯 Todos los enlaces de productos funcionan correctamente.")

    def tearDown(self):
        self.navegador.quit()

if __name__ == "__main__":
    unittest.main()
