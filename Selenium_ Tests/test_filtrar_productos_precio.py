import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class PruebaFiltradoProductos(unittest.TestCase):

    def setUp(self):
        # Configuración inicial del navegador
        opciones = Options()
        opciones.add_argument("--start-maximized")
        servicio = Service()
        self.navegador = webdriver.Chrome(service=servicio, options=opciones)
        self.espera = WebDriverWait(self.navegador, 10)

    def test_filtrar_productos_por_precio(self):
        navegador = self.navegador
        espera = self.espera

        # Paso 1: Ingresar al sitio
        navegador.get("https://www.saucedemo.com/")

        # Paso 2: Iniciar sesión
        espera.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        navegador.find_element(By.ID, "password").send_keys("secret_sauce")
        navegador.find_element(By.ID, "login-button").click()

        # Paso 3: Esperar que se carguen los productos
        espera.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_price")))

        # Paso 4: Capturar los precios actuales
        precios_iniciales = [float(p.text.replace("$", "")) for p in navegador.find_elements(By.CLASS_NAME, "inventory_item_price")]

        # Paso 5: Cambiar el filtro a “Precio (low to high)”
        filtro = Select(espera.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))))
        filtro.select_by_value("lohi")

        # Paso 6: Esperar que los precios se actualicen
        espera.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_price")))
        precios_filtrados = [float(p.text.replace("$", "")) for p in navegador.find_elements(By.CLASS_NAME, "inventory_item_price")]

        # Paso 7: Validar que los precios estén en orden ascendente
        self.assertEqual(precios_filtrados, sorted(precios_filtrados))
        print("✅ Los productos se ordenaron correctamente de menor a mayor precio.")

        # Mostrar comparación de precios
        print(f"Precios iniciales: {precios_iniciales}")
        print(f"Precios filtrados (menor a mayor): {precios_filtrados}")

    def tearDown(self):
        # Cierra el navegador al finalizar la prueba
        self.navegador.quit()

if __name__ == "__main__":
    unittest.main()
