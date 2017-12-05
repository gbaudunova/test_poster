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


class TestForm(TestCase):

    def test_user_form_valid(self):
        form = PortalForm(data={'name': "Hacker News", 'user': "admin"})

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
        self.data = {
            'name': 'Hacker news',
            'portals': 'Hacker news'
        }

    def test_for_connection(self):
        response = self.client.get('https://127.0.0.1:8000/portal/create/')

        self.assertTemplateUsed('template.html')

        self.assertRedirects(response, '/main/', status_code=302, target_status_code=200)

    def test_for_auth_user(self):
        data = {'login': 'login_user', 'password': 'password_user'}

        r = self.client.post(reverse('portal:create_portal'), data=data, follow=True)

        self.assertEqual(r.status_code, 200)

    def test_for_auth_user_using_wrong_data(self):
        wrong_data = {'login': 'L', 'password': ''}

        resp = self.client.post(reverse('portal:create_portal'), data=wrong_data, follow=True)

        self.assertEqual(resp.status_code, 200)

    def test_for_selected_portal(self):
        r = self.client.post(reverse('portal:create_portal'), data=self.data)

        self.assertEqual(r.status_code, 302)

        self.assertRedirects(r, '/portal/create/', status_code=302, target_status_code=302)

    def test_if_portal_form_valid_should_return_text_portal_exists_in_your_list(self):

        portal_form = {'name': 'Golang news', 'user': 'admin'}

        portal_models = Portal.objects.create(name='Golang news', user='user1')

        r = self.client.post(reverse('portal:create_portal'), data=portal_form)

        self.assertEqual(r.status_code, 302)

        self.assertEqual(r.context, "Портал %s  уже существует в вашем списке!" % portal_form['name'])

    def test_for_create_portal_in_selected_portal(self):

        data = {'username': 'admin', 'password': 'password'}

        valid_form = {'name': 'Hacker News', 'user': 'admin'}

        portal_models = Portal.objects.create(name='Hacker news', user='admin')

        r = self.client.post(reverse('/portal/create/'), data=valid_form)

        self.assertEqual(r.status_code, 302)

        self.assertRedirects(r, '/main/', status_code=302, target_status_code=302)

    def test_for_delete_portals(self):

        data = {'login': 'login', 'password': '2323232'}

        r = self.client.post(reverse('portal:delete_portal', kwargs={'id_portal': 1}), data=data)

        self.assertEqual(r.status_code, 302)

        self.assertRedirects(r, '/main/', status_code=302, target_status_code=200)





