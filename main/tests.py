from django.test import TestCase, Client


class ViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.input_data = {
            'title': 'title',
            'url': 'http://grablib.org',
            'descroption': 'Autumn',
            'hackernews': 'hackernews'
        }
        self.empty_data = {
            'title': '',
            'url': '',
            'description': ''

        }
        self.small_data = {
            'title': 't'
        }

    def test_for_connection(self):
        responce = self.client.get('http://127.0.0.1:8000/main/')
        self.assertEqual(responce.status_code, 200)

        self.assertTemplateUsed('template.html')

    def test_check_data(self):
        responce = self.client.post('/main/', self.input_data, follow=True)
        self.assertTemplateUsed('template.html')
        self.assertContains(responce, 'Error', 0)

    def test_empty_data(self):
        responce = self.client.post('/main/', self.empty_data, follow=True)
        self.assertTemplateUsed('template.html')

    def test_length_of_data(self):
        responce = self.client.post('/main/', self.small_data, follow=True)
        self.assertTemplateUsed('template.html')

    def test_for_fail_connection(self):
        responce = self.client.post('/main/', self.small_data)
        responce = self.client.get('http://127.0.0.1:8000/main/')
        self.assertNotEqual(responce.status_code, 404)
        self.assertTemplateUsed('template.html')











