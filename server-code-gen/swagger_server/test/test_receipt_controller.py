# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.receipt import Receipt  # noqa: E501
from swagger_server.test import BaseTestCase


class TestReceiptController(BaseTestCase):
    """ReceiptController integration test stubs"""

    def test_receipt_id_get(self):
        """Test case for receipt_id_get

        Get a receipt.
        """
        response = self.client.open(
            '/Charnley-Test/Billing-Flower-Shop/2.0.0/receipt/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_receipt_post(self):
        """Test case for receipt_post

        Create a receipt.
        """
        body = Receipt()
        response = self.client.open(
            '/Charnley-Test/Billing-Flower-Shop/2.0.0/receipt',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
