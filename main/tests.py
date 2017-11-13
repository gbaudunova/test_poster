# from django.test import TestCase
#
# class PortalTest(TestCase):
#     def test_models_creation(self):
#         portal_models = Portal.objects.create(name='name', user="user")
#         self.assertEqual(portal_models.name, 'name')
#         self.assertEqual(portal_models.user, 'user')
#
#
# class SetupTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(name="name", user="user")
#
#
# class User_Form_Test(TestCase):
#     def test_UserForm_valid(self):
#         form = PortalForm(data={'name': "us", 'user': "user"})
#         self.assertTrue(form.is_valid())
