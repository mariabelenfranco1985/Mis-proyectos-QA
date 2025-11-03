import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class PruebaEliminarProductoCarrito(unittest.TestCase):

    def setUp(self):
        opciones = Options()
        opciones.add_argument("--start-maximized")
        opciones.add_experimental_option("detach", True)  # 🔹 evita cierre brusco del navegador
        servicio = Service()
        self.navegador = webdriver.Chrome(service=servicio, options=opciones)
        self.espera = WebDriverWait(self.navegador, 10)

    def test_eliminar_producto_del_carrito(self):
        navegador = self.navegador
        espera = self.espera

        # Paso 1: Ingresar al sitio
        navegador.get("https://www.saucedemo.com/")

        # Paso 2: Iniciar sesión
        espera.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        navegador.find_element(By.ID, "password").send_keys("secret_sauce")
        navegador.find_element(By.ID, "login-button").click()

        # Paso 3: Esperar que aparezcan los productos
        espera.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))

        # Paso 4: Agregar el primer producto al carrito
        primer_producto = navegador.find_element(By.CLASS_NAME, "inventory_item_name").text
        boton_agregar = navegador.find_element(By.XPATH, "(//button[contains(text(), 'Add to cart')])[1]")
        boton_agregar.click()
        print(f"🛒 Producto agregado al carrito: {primer_producto}")

        # Paso 5: Ir al carrito
        navegador.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        espera.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))

        # Verificar que el producto esté dentro
        producto_carrito = navegador.find_element(By.CLASS_NAME, "inventory_item_name").text
        self.assertEqual(primer_producto, producto_carrito)
        print(f"✅ El producto '{producto_carrito}' aparece en el carrito.")

        # Paso 6: Eliminar el producto
        boton_eliminar = espera.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Remove')]")))
        boton_eliminar.click()
        print(f"🗑️ Producto '{primer_producto}' eliminado del carrito.")

        # Paso 7: Confirmar que el carrito quedó vacío
        try:
            espera.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
            self.fail("❌ El producto no fue eliminado correctamente.")
        except TimeoutException:
            print("✅ El carrito está vacío. Eliminación exitosa.")
        except NoSuchElementException:
            print("✅ El carrito está vacío. Eliminación exitosa (sin elementos).")

    def tearDown(self):
        try:
            self.navegador.quit()
        except Exception:
            pass  # 🔹 evita error RtUserThreadStart al cerrar Chrome

if __name__ == "__main__":
    unittest.main()

