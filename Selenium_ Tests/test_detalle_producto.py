import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class PruebaDetalleProducto(unittest.TestCase):

    def setUp(self):
        opciones = Options()
        opciones.add_argument("--start-maximized")
        opciones.add_experimental_option("detach", True)
        servicio = Service()
        self.navegador = webdriver.Chrome(service=servicio, options=opciones)
        self.espera = WebDriverWait(self.navegador, 10)

    def test_visualizar_detalle_producto(self):
        navegador = self.navegador
        espera = self.espera

        # Paso 1: Ingresar al sitio
        navegador.get("https://www.saucedemo.com/")

        # Paso 2: Iniciar sesión con un usuario válido
        espera.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        navegador.find_element(By.ID, "password").send_keys("secret_sauce")
        navegador.find_element(By.ID, "login-button").click()

        # Paso 3: Esperar a que aparezcan los productos
        productos = espera.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))

        # Guardar el nombre del primer producto
        nombre_producto = productos[0].text
        print(f"🛍️ Probando detalle del producto: {nombre_producto}")

        # Paso 4: Hacer clic en el primer producto
        productos[0].click()

        # Paso 5: Verificar que el nombre en la página de detalle coincida
        nombre_detalle = espera.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_details_name"))).text
        self.assertEqual(nombre_producto, nombre_detalle)
        print(f"✅ El nombre del producto coincide: {nombre_detalle}")

        # Paso 6: Verificar que haya una descripción y un precio visibles
        descripcion = navegador.find_element(By.CLASS_NAME, "inventory_details_desc").text
        precio = navegador.find_element(By.CLASS_NAME, "inventory_details_price").text

        self.assertTrue(len(descripcion) > 0, "❌ No se encontró la descripción del producto.")
        self.assertTrue(precio.startswith("$"), "❌ No se muestra el precio correctamente.")

        print(f"📝 Descripción: {descripcion}")
        print(f"💲 Precio: {precio}")
        print("✅ Prueba completada: el detalle del producto se visualiza correctamente.")

    def tearDown(self):
        self.navegador.quit()

if __name__ == "__main__":
    unittest.main()
