from django.test import TestCase
from django.urls import reverse


class LandingPageTest(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse('landing'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing.html')

    def test_status_code_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_status_code_signup(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_status_code_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_status_code_leads(self):
        response = self.client.get(reverse('leads:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leads/list.html')

