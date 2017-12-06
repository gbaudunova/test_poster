import unittest
from . import tasks
from grab import DataNotFound


class TestTasks(unittest.TestCase):

    def setUp(self):
        self.log_pass = {
            'login': 'denis',
            'password': 'gorod312'
        }

    def test_get_selected_portal(self):
        portal = [
            {
                'name': 'Hacker news',
                'url_auth': 'https://news.ycombinator.com/login',
                'url_submit': 'https://news.ycombinator.com/submit',
                'inp_login': 'acct',
                'inp_password': 'pw',
                'inp_title': 'title',
                'inp_url': 'url',
                'inp_text': 'text',
                'auth_by': '<form method="post" action="login">',
                'auth_complete': '<span class="pagetop">'
            }
        ]
        data = ['Hacker news']
        self.assertEqual(tasks.get_selected_portal(data), portal)

    def test_send_spam(self):
        data = "{'url': 'https://www.google.com', 'title': 'title', 'description': None}"
        sel_portal = ['Hacker news']
        self.assertEqual(tasks.send_spam(data, sel_portal), 200)
