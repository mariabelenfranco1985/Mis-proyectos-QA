import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class PruebaCerrarSesion(unittest.TestCase):

    def setUp(self):
        opciones = Options()
        opciones.add_argument("--start-maximized")
        opciones.add_experimental_option("detach", True)
        servicio = Service()
        self.navegador = webdriver.Chrome(service=servicio, options=opciones)
        self.espera = WebDriverWait(self.navegador, 10)

    def test_cerrar_sesion(self):
        navegador = self.navegador
        espera = self.espera

        # Paso 1: Ingresar a la página principal
        navegador.get("https://www.saucedemo.com/")

        # Paso 2: Iniciar sesión
        espera.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        navegador.find_element(By.ID, "password").send_keys("secret_sauce")
        navegador.find_element(By.ID, "login-button").click()

        # Paso 3: Esperar que aparezca el menú lateral (hamburguesa)
        boton_menu = espera.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        boton_menu.click()

        # Paso 4: Hacer clic en el botón de “Logout”
        boton_logout = espera.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        boton_logout.click()

        # Paso 5: Verificar que el usuario vuelva a la pantalla de login
        espera.until(EC.presence_of_element_located((By.ID, "login-button")))
        self.assertTrue("saucedemo.com" in navegador.current_url)
        print("✅ Prueba exitosa: el usuario cerró sesión correctamente.")

    def tearDown(self):
        self.navegador.quit()

if __name__ == "__main__":
    unittest.main()
