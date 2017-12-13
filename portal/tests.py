from django.test import TestCase, Client
from django.urls import reverse

from .forms import PortalForm
from .models import Portal
from .views import catch_portal_form


client = Client()


class PortalTest(TestCase):
    def test_for_create_portal(self):
        portal_models = Portal.objects.create(name='Hacker News', user="user1")
        self.assertEqual(portal_models.name, 'Hacker News')
        self.assertEqual(portal_models.user, 'user1')
        assert isinstance(portal_models, Portal)


class TestForm(TestCase):

    def test_user_form_is_valid(self):
        data = {'name': "Hacker News", 'user': "admin",
                'login': 'hjhk', 'password': 'dfdfd'}
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
            'password': 'pas'

        }
        self.validData = {
            'name': 'Hacker News',
            'user': 'user1'
        }
        self.data = {
            'name': 'Hacker news',
            'portals': 'Hacker news'
        }

    def test_for_catch_data(self):
        data = {'name': "Hacker News", 'user': "admin",
                'login': 'hjhk', 'password': 'dfdfd'}
        r = self.client.post(reverse('portal:create_portal'), data=data)
        self.assertTemplateUsed('index.html')

        self.assertEqual(r.status_code, 200)

        #self.assertRedirects(r, '/main/', status_code=302, target_status_code=302)
#
#     def test_if_portal_form_valid_should_return_data_in_form(self):
#
#         data = {'name': "Hacker News", 'user': "admin",
#                 'login': 'hjhk', 'password': 'dfdfd'}
#
#         r = self.client.post(reverse('portal:create_portal'), data=data)
#
#         self.assertEqual(r.status_code, 200)
#
#     def test_for_false_verification_form(self):
#
#         data = {'name': "Hacker News", 'user': "", 'login': 'hjhk'}
#
#         r = self.client.post(reverse('portal:create_portal'), data=data)
#
#         self.assertEqual(r.content, "Форма не валидна")
#
#         self.assertRedirects(r, '/main/',
#                              status_code=302, target_status_code=302)
#
#     def test_if_portal_form_valid_should_return_text(self):
#         data = {'name': "Hacker News", 'user': "admin",
#                 'login': 'hjhk', 'password': 'dfdfd'}
#
#         response = self.client.post(reverse('portal:create_portal'),
#                                     data=data)
#
#         self.assertEqual(response.status_code, 302)
#
#         self.assertEqual(response.context, "Портал уже"
#                                            " существует в вашем списке!")
#
#     def test_for_delete_portals(self):
#
#         data = {'login': 'login', 'password': '2323232'}
#
#         r = self.client.post(reverse('portal:delete_portal',
#                                      kwargs={'id_portal': 1}), data=data)
#         self.assertEqual(r.status_code, 302)
#         self.assertRedirects(r, '/main/',
#                              status_code=302, target_status_code=200)
