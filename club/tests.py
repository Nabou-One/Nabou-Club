from django.test import TestCase
from django.urls import reverse

class HomeViewTest(TestCase):
    def test_home_page_status_code_and_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bienvenue dans Nabou Club")
