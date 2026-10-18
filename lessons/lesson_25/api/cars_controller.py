import requests

from core.utils.request_utils import RequestUtils
from requests.auth import HTTPBasicAuth


class CarsController(RequestUtils):

    def __init__(self, log_file=None):
        super().__init__(log_file=log_file)

        self.base_url = "http://127.0.0.1:8080"
        self.headers = self.get_auth()

    def get_auth(self):
        auth = HTTPBasicAuth("test_user", "test_pass")
        response = self.send_request(method='POST', path=self.base_url + '/auth', auth=auth, exp_status_code=200)
        return  {"Authorization": f"Bearer {response.json().get('access_token')}"}

    def get_cars(self, sort_by=None, limit=None):
        params = {
            "sort_by": sort_by,
            "limit": limit,
        }
        return self.send_request(method='GET', path=self.base_url + '/cars', params=params, headers=self.headers, exp_status_code=200)

