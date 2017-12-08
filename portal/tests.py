from django.test import TestCase, Client
from django.urls import reverse
from .forms import *
from .models import *


client = Client()


class PortalTest(TestCase):
    def create_portal(self):
        portal_models = Portal.objects.create(name='Hacker News', user="user1")
        return Portal.objects.create(name='name', user="user")
        self.assertEqual(portal_models.name, 'name1')
        self.assertEqual(portal_models.user, 'user1')

    def test_creation(self):
        w = self.create_portal()
        self.assertTrue(isinstance(w, Portal))
        self.assertEqual(w.__str__(), w.name)


class TestForm(TestCase):

    def test_user_form_is_not_valid(self):
        data = {'name': "Hacker News", 'user': "admin", 'login': 'hjhk', 'password': 'dfdfd'}
        form = PortalForm(data=data)

        self.assertTrue(form.is_valid(), True)

    def test_user_form__is_not_valid(self):
        form = PortalForm(data={'name': "Hacker News", 'user': "admin"})
        self.assertFalse(form.is_valid(), False)


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
        self.data = {
            'name': 'Hacker news',
            'portals': 'Hacker news'
        }

    def test_for_auth_user(self):
        data = {'name': "Hacker News",
                'login': '',
                'password': 'dfdfd'}

        r = self.client.get(reverse('portal:create_portal'), data=data, follow=True)

        self.assertRedirects(r, '/main/', status_code=302, target_status_code=302)

    def test_for_selected_portal(self):
        r = self.client.post(reverse('portal:create_portal'), data=self.data)

        self.assertEqual(r.status_code, 200)

    def test_if_portal_already_exists(self):
        data = {'name': "Hacker News", 'user': "admin", 'login': 'hjhk', 'password': 'dfdfd'}

        portal_models = Portal.objects.create(name='Hacker news', user='user1')

        r = self.client.post(reverse('portal:create_portal'), data=data)

        self.assertEqual(r.status_code, 200)

        self.assertEqual(r.context, "Портал уже существует в вашем списке!")

    def test_if_portal_form_valid_should_return_text_portal_exists_in_your_list(self):

        data = {'name': "Hacker News", 'user': "admin", 'login': 'hjhk', 'password': 'dfdfd'}

        r = self.client.post(reverse('portal:create_portal'), data=data)

        self.assertEqual(r.status_code, 200)

    def test_for_false_verification_form(self):

        data = {'name': "Hacker News", 'user': "", 'login': 'hjhk'}

        r = self.client.post(reverse('portal:create_portal'), data=data)

        self.assertRedirects(r, '/main/', status_code=302, target_status_code=302)

    def test_for_delete_portals(self):

        data = {'login': 'login', 'password': '2323232'}

        r = self.client.post(reverse('portal:delete_portal', kwargs={'id_portal': 1}), data=data)

        self.assertEqual(r.status_code, 302)

        self.assertRedirects(r, '/main/', status_code=302, target_status_code=200)





