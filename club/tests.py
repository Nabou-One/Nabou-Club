from django.test import TestCase
from django.urls import reverse

class ClubViewTests(TestCase):
    def test_index_view_status_code(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_content(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, "Hello world")
