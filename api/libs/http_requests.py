import requests
import json


class HTTP(object):

    def __init__(self, server_url):
        self.server_url = server_url
        self.http = requests.Session()
        self._url = None
        self.token = None


    def get_api_path(self, path):
        return '/'.join((self.server_url, path))


    def get_auth_token(self, url, credentials):
        """

        :param url:  API path
        :param credentials:
        :return:
        """

        response = self.http.get(self.get_api_path(url), auth=credentials)
        self.token = json.loads(response.text).get('token')
        return response


    def make_request(self, url, action, data='', status_code='', parser=None):
        """Abstraction of typical http events
        *http request wrapper with SSL cert verify disabled*

        :param status_code:
        :param str url: the url
        :param str action: one of the HTTP verbs (upper case)
        :param data:
        :param headers: additional headers besides the default one
        :param func parser: parse the response from the UI
        :return:
        """
        self._url = self.get_api_path(url)
        headers = {
            'Content-Type': "application/json",
            'Token': self.token,

        }
        kwargs = {}
        if headers:
            kwargs.update(headers=headers)
        if data:
            kwargs.update(data=json.dumps(data))

        return getattr(self.http, action.lower())(self._url, **kwargs)


