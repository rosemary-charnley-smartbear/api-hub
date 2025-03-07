# coding: utf-8

"""
    Flower Shop -- Billing

    This is a sample Flower Shop server.   This includes the Billing REST APIs. You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).   # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: rosemary.charnley@smartbear.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.receipt_api import ReceiptApi  # noqa: E501
from swagger_client.rest import ApiException


class TestReceiptApi(unittest.TestCase):
    """ReceiptApi unit test stubs"""

    def setUp(self):
        self.api = ReceiptApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_receipt_id_get(self):
        """Test case for receipt_id_get

        Get a receipt.  # noqa: E501
        """
        pass

    def test_receipt_post(self):
        """Test case for receipt_post

        Create a receipt.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
