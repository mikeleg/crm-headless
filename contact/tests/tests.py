from ..models import Contact
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factory import ContactFactory


class ContactTest(APITestCase):
    def setUp(self) -> None:
        self.contact = ContactFactory.create_batch(5)

    def test_contact_list(self):
        url = "/api/account/1/contact"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_contact_OK(self):
        url = "/api/account/1/contact"
        payload = {
            "name": "Mikele",
            "surname": "Gatti",
            "email": "test@test.com",
        }

        response = self.client.post(url, payload)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Mikele")
        self.assertEqual(response.data["surname"], "Gatti")
        self.assertEqual(response.data["email"], "test@test.com")
