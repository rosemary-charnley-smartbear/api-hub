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
from swagger_client.api.bill_api import BillApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBillApi(unittest.TestCase):
    """BillApi unit test stubs"""

    def setUp(self):
        self.api = BillApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_bill_id_get(self):
        """Test case for bill_id_get

        Get a bill.  # noqa: E501
        """
        pass

    def test_bill_post(self):
        """Test case for bill_post

        Submit a bill.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
