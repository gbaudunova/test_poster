from django.test import TestCase, Client
from django.urls import reverse

from .forms import *
from .models import *


client = Client()


class PortalTest(TestCase):
    def create_portal(self):
        portal_models = Portal.objects.create(name='name1', user="user1")

        return Portal.objects.create(name='name', user="user")

        self.assertEqual(portal_models.name, 'name1')

        self.assertEqual(portal_models.user, 'user1')

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
        self.validData = {
            'name': 'Reddit',
            'user': 'user1'
        }

    def test_for_connection(self):
        response = self.client.get('https://127.0.0.1:8000/portal/create/')
        self.assertTemplateUsed('template.html')
        self.assertRedirects(response, '/main/', status_code=302, target_status_code=200)

    def test_for_receive_data(self):
        data = {'login': 'login_user', 'password': 'password_user'}
        r = self.client.post(reverse('portal:create_portal'), data=data, follow=True)
        self.assertEqual(r.status_code, 200)

    def test_for_delete_portals(self):
        resp = self.client.get(reverse('portal:delete_portal', args=[id_portal]), follow=True)


    # def test_for_create_portals(self):
    #     portal_models = Portal.objects.create(name='Reddit', user="user1")
    #     portal_form = PortalForm(data=self.validData)
    #     self.assertTrue(portal_form.is_valid())
    #     create_new_portal = portal_form.save()
    #     # self.assertEqual(create_new_portal.name, self.validData['name'])
    #     response = client.post(reverse('portal:create_portal'), {'name': 'Reddit', 'portals': 'Hacker News'}, follow=True)
    #     a = portal_models.objects.filter(name=create_new_portal.name)
    #     self.assertEqual(create_new_portal.name, jkj)


