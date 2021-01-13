from account.models import Account
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factory import AccountFactory


class AccountTest(APITestCase):
    def setUp(self):
        self.account = AccountFactory.create_batch(20)

    def test_account_list(self):
        response = self.client.get(reverse("account-list"))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data), 20)

    def test_create_account_OK(self):
        payload = {
            "legalname": "Test Legal",
            "vat": "00000000000",
            "address": "via test 10",
            "city": "Parma",
            "zipcode": "43036",
            "country": "Italy",
            "province": "PR",
            "phone": "033333324242",
            "email": "test@test.com",
            "type": 'CUSTOMER',
        }

        response = self.client.post(reverse("account-list"), payload)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"],'')
        self.assertEqual(response.data["vat"], "00000000000")
        self.assertIsNotNone(response.data["id"])
        self.assertEqual(response.data["geo"],'')
        self.assertEqual(response.data["sdi"],'')
        self.assertEqual(response.data["pec"],'')
        self.assertEqual(response.data["id"],21)

   
    def test_create_account_KO(self):
        payload = {
            "vat": "00000000000",
            "address": "via test 10",
            "city": "Parma",
            "zipcode": "43036",
            "country": "Italy",
            "province": "PR",
            "phone": "033333324242",
            "email": "test@test.com",
            "type": 'CUSTOMER',
        }

        response = self.client.post(reverse("account-list"), payload)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_account_detail_OK(self):
        response = self.client.get(reverse("account-detail", kwargs={"pk": 2}))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Name 1")
        self.assertEqual(response.data["legalname"], "Legalname 1")

    def test_account_detail_modify_OK(self):
        payload = {
            "legalname": "PROVA CAMBIO",
            "address": "via test 10",
        }
        
        response = self.client.patch(reverse("account-detail", kwargs={"pk": 2}),payload)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 2)
        self.assertEqual(response.data["legalname"], "PROVA CAMBIO")
        self.assertEqual(response.data["address"], "via test 10")
    
    def test_account_detail_delete_OK(self):
        num_before_delete = Account.objects.count()
        response = self.client.delete(reverse("account-detail", kwargs={"pk": 2}))
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        self.assertNotEqual(num_before_delete,Account.objects.count()-1)