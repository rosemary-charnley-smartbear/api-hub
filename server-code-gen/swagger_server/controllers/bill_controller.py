import connexion
import six

from swagger_server.models.bill import Bill  # noqa: E501
from swagger_server import util


def bill_id_get(id):  # noqa: E501
    """Get a bill.

     # noqa: E501

    :param id: Bill id.
    :type id: str

    :rtype: Bill
    """
    return 'do some magic!'


def bill_post(body):  # noqa: E501
    """Submit a bill.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Bill
    """
    if connexion.request.is_json:
        body = Bill.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
