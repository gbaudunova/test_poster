from django.test import TestCase, Client
from django.urls import reverse


class ViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.input_data = {
            'title': 'title',
            'url': 'http://grablib.org',
            'description': 'Autumn'
        }
        self.empty_data = {
            'title': '',
            'url': '',
            'description': ''

        }
        self.small_data = {
            'title': 't',
            'url': 'www',
            'description': 'df'
        }
        self.user_valid_data = {
            'login': 'denisoed',
            'password': 'gorod312'
        }

    def test_for_connection(self):
        responce = self.client.get('http://127.0.0.1:8000/main/')
        self.assertEqual(responce.status_code, 200)

        self.assertTemplateUsed('index.html')

    def test_check_data(self):
        responce = self.client.post(reverse('main:post_article'),
                                    self.input_data)
        self.assertTemplateUsed('index.html')
        self.assertContains(responce, 'Error', 0)

    def test_empty_data(self):
        responce = self.client.post('/main/', self.empty_data, follow=True)
        self.assertTemplateUsed('index.html')
        self.assertEqual(responce.status_code, 200)

    def test_length_of_data(self):
        responce = self.client.post('/main/', self.small_data, follow=True)
        self.assertTemplateUsed('index.html')
        self.assertEqual(responce.status_code, 200)
