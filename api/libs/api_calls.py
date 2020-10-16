import os
import sys
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(path)


from api.libs.http_requests import HTTP
import json




class ApiCalls(HTTP):

    def __init__(self, server_url):
        super().__init__(server_url)

    def auth_token(self, username, password):
        """

        :param username:
        :param password:
        :return:
        """
        return self.get_auth_token(url='api/auth/token', credentials=(username, password))

    def get_users(self):
        """

        :return:
        """
        return self.make_request(url='api/users', action='GET', )

    def get_user_info(self, username):
        """

        :param username:
        :return:
        """
        return self.make_request(url='api/users/{}'.format(username), action='GET', )

    def update_user_info(self, username, firstname=None, lastname=None, phone=None):
        """

        :param username:
        :param firstname:
        :param lastname:
        :param phone:
        :return:
        """
        payload = dict()
        if firstname:
            payload['firstname'] = firstname
        if lastname:
            payload['lastname'] = lastname
        if phone:
            payload['phone'] = phone
        return self.make_request(url='api/users/{}'.format(username), action='PUT', data=payload)



if __name__ == '__main__':
    api_caller = ApiCalls('http://localhost:8080')
    api_caller.auth_token(username='test', password='test')
    api_caller.get_users()
    userinfo = api_caller.get_user_info('test')
    api_caller.update_user_info(username='test', phone='9999999')
