import connexion
import six

from swagger_server.models.bill import Bill  # noqa: E501
from swagger_server import util


def process_post(body):  # noqa: E501
    """Process a bill.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Bill.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
