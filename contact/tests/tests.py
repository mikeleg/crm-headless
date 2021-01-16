from ..models import Contact
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factory import ContactFactory


class ContactTest(APITestCase):
    
    def setUp(self) -> None:
        self.contact = ContactFactory.create_batch(5)


    def test_contact_list(self):
        url = '/api/account/1/contact'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)