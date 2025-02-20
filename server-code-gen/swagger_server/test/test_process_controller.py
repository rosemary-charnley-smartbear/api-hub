# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.bill import Bill  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProcessController(BaseTestCase):
    """ProcessController integration test stubs"""

    def test_process_post(self):
        """Test case for process_post

        Process a bill.
        """
        body = Bill()
        response = self.client.open(
            '/Charnley-Test/Billing-Flower-Shop/2.0.0/process',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
