import requests
import unittest

class TestApiUsers(unittest.TestCase):

    def test_listar_usuarios(self):
        """Verifica que la API devuelva código 200 y datos correctos."""
        url = "https://reqres.in/api/users?page=2"
        response = requests.get(url)

        # Validar código de respuesta
        self.assertEqual(response.status_code, 200)

        # Convertir a JSON
        data = response.json()

        # Validar que exista la clave 'data'
        self.assertIn('data', data)

        # Validar que la lista tenga usuarios
        self.assertTrue(len(data['data']) > 0)

        # Validar que el primer usuario tenga los campos esperados
        first_user = data['data'][0]
        self.assertIn('id', first_user)
        self.assertIn('email', first_user)
        self.assertIn('first_name', first_user)
        self.assertIn('last_name', first_user)


if __name__ == '__main__':
    unittest.main()
