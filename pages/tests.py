from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.

class HomePageViewTest(TestCase):
    def test_home_page_view_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_view_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Home Page')

    def test_home_page_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

class AboutPageViewTest(TestCase):
    def test_aboutus_page_view_url(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)

    def test_aboutus_page_view_url_by_name(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)

    def test_aboutus_page_view_content(self):
        response = self.client.get(reverse('aboutus'))
        self.assertContains(response, 'About Us')

    def test_aboutus_page_template_used(self):
        response = self.client.get(reverse('aboutus'))
        self.assertTemplateUsed(response, 'pages/aboutus.html')

class SignupPageViewTest(TestCase):
    def test_signup_page_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_view_template_used(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_signup_page_view_content(self):
        response = self.client.get(reverse('signup'))
        self.assertContains(response, 'Sign Up')

class LoginPageViewTest(TestCase):
    def test_login_page_view_url_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_view_template_used(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'account/login.html')

    def test_login_page_view_content(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'Log In')