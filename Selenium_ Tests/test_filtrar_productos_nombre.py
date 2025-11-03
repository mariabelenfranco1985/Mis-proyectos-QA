import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class PruebaFiltradoPorNombre(unittest.TestCase):

    def setUp(self):
        # Configuración inicial del navegador
        opciones = Options()
        opciones.add_argument("--start-maximized")
        servicio = Service()
        self.navegador = webdriver.Chrome(service=servicio, options=opciones)
        self.espera = WebDriverWait(self.navegador, 10)

    def test_filtrar_productos_por_nombre(self):
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

        # Paso 4: Capturar los nombres de los productos antes del filtrado
        nombres_iniciales = [n.text for n in navegador.find_elements(By.CLASS_NAME, "inventory_item_name")]

        # Paso 5: Cambiar el filtro a “Name (A to Z)”
        filtro = Select(espera.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))))
        filtro.select_by_value("az")

        # Paso 6: Esperar que los nombres se actualicen
        espera.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))
        nombres_filtrados = [n.text for n in navegador.find_elements(By.CLASS_NAME, "inventory_item_name")]

        # Paso 7: Verificar que los nombres estén en orden alfabético
        self.assertEqual(nombres_filtrados, sorted(nombres_filtrados))
        print("✅ Los productos se ordenaron correctamente de la A a la Z.")

        # Mostrar resultados
        print("Lista ordenada correctamente:")
        for nombre in nombres_filtrados:
            print("   -", nombre)

    def tearDown(self):
        # Cierra el navegador al finalizar la prueba
        self.navegador.quit()

if __name__ == "__main__":
    unittest.main()
