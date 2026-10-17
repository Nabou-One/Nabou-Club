from django.test import TestCase
from django.urls import reverse

class ClubViewTests(TestCase):
    def test_hello_club_view(self):
        response = self.client.get(reverse('hello_club'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello club")
