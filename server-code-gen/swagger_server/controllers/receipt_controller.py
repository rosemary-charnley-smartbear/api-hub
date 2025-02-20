import connexion
import six

from swagger_server.models.receipt import Receipt  # noqa: E501
from swagger_server import util


def receipt_id_get(id):  # noqa: E501
    """Get a receipt.

     # noqa: E501

    :param id: Receipt id.
    :type id: str

    :rtype: Receipt
    """
    return 'do some magic!'


def receipt_post(body):  # noqa: E501
    """Create a receipt.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Receipt
    """
    if connexion.request.is_json:
        body = Receipt.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
