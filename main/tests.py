import sys
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
import requests
from .views import *

client = Client()
input_data = {
    'title': 'title',
    'url': 'http://grablib.org'
    }


class ViewTest(TestCase):

    def test_for_connection(self):
        responce = self.client.get('http://127.0.0.1:8000/main/')
        self.assertEqual(responce.status_code, 200)
        self.assertTemplateUsed('template.html')


    def test_catch_data(self):
        responce = self.client.post()
        self.assertEqual(responce.status_code, 200)




        # request = self.client.post(reverse('catch_data'), data)
        # request.client = self.client
        #
        # responce = MainFormsCreateView.as_view()(request)
        # self.assertEqual(responce.status_code, 302)










