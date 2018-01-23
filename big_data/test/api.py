from ..blockchain import app
import unittest
import json
from pprint import pprint
from io import StringIO


class TestApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    def request_get(self, uri):
        print("GET {}".format(uri))
        headers = {"Content-Type": "application/json"}
        self.request = self.app.get(
            uri,
            headers=headers)
        try:
            pprint(json.loads(self.request.data.decode("utf-8")))
        except json.JSONDecodeError:
            print("{}".format(self.request.data.decode("utf-8")))

    def request_post(self, uri, data):
        print("POST {}".format(uri))
        headers = {"Content-Type": "application/json"}
        self.request = self.app.post(
            uri,
            headers=headers,
            input_stream=StringIO(json.dumps(data)))
        print(self.request._status)
        print(self.request.headers)
        try:
            pprint(json.loads(self.request.data.decode("utf-8")))
        except json.JSONDecodeError:
            print("{}".format(self.request.data.decode("utf-8")))