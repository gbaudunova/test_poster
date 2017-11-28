from django.test import TestCase, Client
from .forms import *
from .models import *
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

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

    def test_UserForm_valid(self):
        form = PortalForm(data={'name': "us", 'user': "user"})
        self.assertTrue(form.is_valid())


class ViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.userValidData = {
            'login': 'login',
            'password': 'password'

        }
        self.portalNames = {
            'name1': 'Hacker News',
            'name2': 'Reddit',
            'name3': 'Golang News',
            'name4': 'Habrahabr'
        }
        self.portals = {
            'portal1': 'Hacker News',
            'portal2': 'Reddit',
            'portal3': 'Golang News',
            'portal4': 'Habrahabr'
        }
        self.validData = {
            'name': 'name',
            'user': 'user'
        }

    def test_if_statement(self):
        portal_form = PortalForm(data=self.validData)
        self.assertTrue(portal_form.is_valid())
        create_new_portal = portal_form.save()
        self.assertEqual(create_new_portal.name, self.validData['name'])





