from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.test import APIClient


class UserTestCase(TestCase):
    user_one = None

    def test_login(self):
        self.assertEqual("HOLA", "hola".upper())

    def test_registration_past(self):
        user_email = "user_1@testing.com"
        data = {
            "email": user_email,
            "password1": "Prueba10",
            "password2": "Prueba10",
            "first_name": "User One",
            "last_name": "Testing",
            "country_phone_code": "+52",
            "mobile_number": "9999999999"
        }
        client = APIClient()
        response = client.post('/rest-auth/registration/', data, format='json')

        self.assertEqual(response.status_code, 201)

        self.user_one = User.objects.filter(email=user_email).first()

        self.assertNotEqual(self.user_one, None)

