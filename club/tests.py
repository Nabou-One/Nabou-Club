from django.test import TestCase
from django.urls import reverse

class ClubViewsTestCase(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bienvenue Dans le Club")
