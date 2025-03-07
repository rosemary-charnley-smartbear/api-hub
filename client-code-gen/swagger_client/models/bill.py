# coding: utf-8

"""
    Flower Shop -- Billing

    This is a sample Flower Shop server.   This includes the Billing REST APIs. You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).   # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: rosemary.charnley@smartbear.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Bill(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'person': 'Person',
        'billing_address': 'Address',
        'discount_code': 'str',
        'payment_type': 'str',
        'discount': 'float',
        'subtotal': 'float',
        'tax': 'float',
        'total': 'float'
    }

    attribute_map = {
        'id': 'id',
        'person': 'person',
        'billing_address': 'billingAddress',
        'discount_code': 'discountCode',
        'payment_type': 'paymentType',
        'discount': 'discount',
        'subtotal': 'subtotal',
        'tax': 'tax',
        'total': 'total'
    }

    def __init__(self, id=None, person=None, billing_address=None, discount_code=None, payment_type=None, discount=None, subtotal=None, tax=None, total=None):  # noqa: E501
        """Bill - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._person = None
        self._billing_address = None
        self._discount_code = None
        self._payment_type = None
        self._discount = None
        self._subtotal = None
        self._tax = None
        self._total = None
        self.discriminator = None
        self.id = id
        if person is not None:
            self.person = person
        if billing_address is not None:
            self.billing_address = billing_address
        if discount_code is not None:
            self.discount_code = discount_code
        if payment_type is not None:
            self.payment_type = payment_type
        if discount is not None:
            self.discount = discount
        if subtotal is not None:
            self.subtotal = subtotal
        if tax is not None:
            self.tax = tax
        if total is not None:
            self.total = total

    @property
    def id(self):
        """Gets the id of this Bill.  # noqa: E501


        :return: The id of this Bill.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Bill.


        :param id: The id of this Bill.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def person(self):
        """Gets the person of this Bill.  # noqa: E501


        :return: The person of this Bill.  # noqa: E501
        :rtype: Person
        """
        return self._person

    @person.setter
    def person(self, person):
        """Sets the person of this Bill.


        :param person: The person of this Bill.  # noqa: E501
        :type: Person
        """

        self._person = person

    @property
    def billing_address(self):
        """Gets the billing_address of this Bill.  # noqa: E501


        :return: The billing_address of this Bill.  # noqa: E501
        :rtype: Address
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this Bill.


        :param billing_address: The billing_address of this Bill.  # noqa: E501
        :type: Address
        """

        self._billing_address = billing_address

    @property
    def discount_code(self):
        """Gets the discount_code of this Bill.  # noqa: E501


        :return: The discount_code of this Bill.  # noqa: E501
        :rtype: str
        """
        return self._discount_code

    @discount_code.setter
    def discount_code(self, discount_code):
        """Sets the discount_code of this Bill.


        :param discount_code: The discount_code of this Bill.  # noqa: E501
        :type: str
        """

        self._discount_code = discount_code

    @property
    def payment_type(self):
        """Gets the payment_type of this Bill.  # noqa: E501


        :return: The payment_type of this Bill.  # noqa: E501
        :rtype: str
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this Bill.


        :param payment_type: The payment_type of this Bill.  # noqa: E501
        :type: str
        """

        self._payment_type = payment_type

    @property
    def discount(self):
        """Gets the discount of this Bill.  # noqa: E501


        :return: The discount of this Bill.  # noqa: E501
        :rtype: float
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this Bill.


        :param discount: The discount of this Bill.  # noqa: E501
        :type: float
        """

        self._discount = discount

    @property
    def subtotal(self):
        """Gets the subtotal of this Bill.  # noqa: E501


        :return: The subtotal of this Bill.  # noqa: E501
        :rtype: float
        """
        return self._subtotal

    @subtotal.setter
    def subtotal(self, subtotal):
        """Sets the subtotal of this Bill.


        :param subtotal: The subtotal of this Bill.  # noqa: E501
        :type: float
        """

        self._subtotal = subtotal

    @property
    def tax(self):
        """Gets the tax of this Bill.  # noqa: E501


        :return: The tax of this Bill.  # noqa: E501
        :rtype: float
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this Bill.


        :param tax: The tax of this Bill.  # noqa: E501
        :type: float
        """

        self._tax = tax

    @property
    def total(self):
        """Gets the total of this Bill.  # noqa: E501


        :return: The total of this Bill.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Bill.


        :param total: The total of this Bill.  # noqa: E501
        :type: float
        """

        self._total = total

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Bill, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Bill):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
