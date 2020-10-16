import pytest
from unittest import TestCase
from api.libs.api_calls import ApiCalls

class TestUser(TestCase):

    api_calls = ApiCalls('http://localhost:8080/')

    def test_auth_token(self):
        response = self.api_calls.auth_token(username='test', password='test')
        json_response = response.json()
        self.assertTrue(200, response.status_code)
        self.assertEqual('SUCCESS', json_response.get('status'))
        self.assertTrue(json_response.get('token'))

    def test_get_users(self):
        self.api_calls.auth_token(username='test', password='test')
        response = self.api_calls.get_users()
        json_response = response.json()
        self.assertTrue(response.ok)
        self.assertEqual('SUCCESS', json_response.get('status'))
        self.assertTrue('test', json_response.get('payload'))

    def test_invalid_user(self):
        self.api_calls.auth_token(username='test', password='test')
        response = self.api_calls.get_user_info('invalid')
        self.assertFalse(response.ok)
        self.assertEqual(500, int(response.status_code))

    def test_get_user_info(self):
        self.api_calls.auth_token(username='test', password='test')
        response = self.api_calls.get_user_info('test')
        json_response = response.json()
        self.assertTrue(response.ok)
        self.assertEqual('SUCCESS', json_response.get('status'))
        self.assertTrue(json_response.get('payload').get('firstname'))
        self.assertTrue(json_response.get('payload').get('lastname'))
        self.assertTrue(json_response.get('payload').get('phone'))

        # self.assertEqual('test', json_response.get('payload').get('firstname'))
        # self.assertEqual('lastname', json_response.get('payload').get('lastname'))
        # self.assertEqual('phone', json_response.get('payload').get('phone'))

    def test_update_user(self):
        self.api_calls.auth_token(username='test', password='test')
        response= self.api_calls.update_user_info(username='test', phone='9999999')
        json_response = response.json()
        self.assertEqual(201, response.status_code)
        self.assertTrue(response.ok)
        self.assertEqual('SUCCESS', json_response.get('status'))

        response = self.api_calls.get_user_info('test')
        json_response = response.json()
        self.assertEqual('9999999', json_response['payload'].get('phone'))




#
# api_caller = ApiCalls('http://localhost:8080')
# api_caller.auth_token(username='test', password='test')
# api_caller.get_users()
# userinfo = api_caller.get_user_info('test')
# api_caller.update_user_info(username='test', phone='9999999')