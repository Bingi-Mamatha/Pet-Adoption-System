
import unittest
from app import app


class PetAdoptionTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_homepage_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_contains_pet_information(self):
        response = self.client.get("/")
        self.assertIn(b"Buddy", response.data)
        self.assertIn(b"Milo", response.data)


if __name__ == "__main__":
    unittest.main()
