from django.test import TestCase, Client
from .forms import *
from .models import *

client = Client()


class PortalTest(TestCase):
    def create_portal(self):
        portal_models = Portal.objects.create(name='name', user="user")
        return Portal.objects.create(name='name', user="user")
        self.assertEqual(portal_models.name, 'name')
        self.assertEqual(portal_models.user, 'user')

    def test_creation(self):
        w = self.create_portal()
        self.assertTrue(isinstance(w, Portal))
        self.assertEqual(w.__str__(), w.name)


class User_Form_Test(TestCase):
    def setUp(self):
        self.client = Client()
        self.userValidData = {
            'login': 'login',
            'password': 'password'

        }

    def test_UserForm_valid(self):
        form = PortalForm(data={'name': "us", 'user': "user"})
        self.assertTrue(form.is_valid())

    # def test_create_portal(self):
    #     responce = self.client.post(self.userValidData, follow=True)
    #     self.assertTemplateUsed('template.html')
    #     self.assertContains(responce, 'Error', 0)
