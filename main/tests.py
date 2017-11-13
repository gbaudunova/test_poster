from django.test import TestCase

# Create your tests here.
class PortalTest(TestCase):
    def test_models_creation(self):
        portal_models = Portal.objects.create(name='name', user="user")
        self.assertEqual(portal_models.name, 'name')
        self.assertEqual(portal_models.user, 'user')


class SetupTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(name="name", user="user")


class User_Form_Test(TestCase):
    def test_UserForm_valid(self):
        form = PortalForm(data={'name': "us", 'user': "user"})
        self.assertTrue(form.is_valid())




# @app.route('/', methods=['POST'])
# def post():
#     data = request.get_json()
#     log(data)
#
#     if data['object'] == 'page':
#         for entry in data['entry']:
#             for messaging_event in entry['messaging']:
#                 sender_id = messaging_event['sender']['id']
#                 recipient_id = messaging_event['recipient']['id']
#
#                 if messaging_event.get('message'):
#                     if 'text' in messaging_event['message']:
#                         messaging_text = messaging_event['message']['text']
#                     else:
#                         messaging_text = 'nothing'
#
#                     response = messaging_text
#
#                     bot.send_text_message(sender_id, response)
#
#
#     return "ok", 200
#
#
# def log(message):
#     print(message)
#     sys.stdout.flush()