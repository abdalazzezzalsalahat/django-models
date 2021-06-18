from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snacks
# Create your tests here.

class SnacksTests(TestCase):

    def setUp(self):
        """[summary]
        a set-up function
        """
        self.user = get_user_model().objects.create_user(
            username="azeez", email="azeez@email.com", password="pass"
        )

        self.snack = Snacks.objects.create(
            name="Milkshake", description="this is so fun", purcheser=self.user,
        )

    def test_home_page_status_code(self):
        """[summary]
        testting home page response status
        """
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_snack_list_view(self):
        """[summary]
        testing List page response
        """
        url = reverse("snacks_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "snacks_list.html")

    def test_snack_detail_view(self):
        """[summary]
        tsting details page response
        """
        response = self.client.get(reverse("snacks_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, "snacks_detail.html")

