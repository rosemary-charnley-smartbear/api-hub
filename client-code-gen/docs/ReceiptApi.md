# swagger_client.ReceiptApi

All URIs are relative to *https://virtserver.swaggerhub.com/Charnley-Test/Billing-Flower-Shop/2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**receipt_id_get**](ReceiptApi.md#receipt_id_get) | **GET** /receipt/{id} | Get a receipt.
[**receipt_post**](ReceiptApi.md#receipt_post) | **POST** /receipt | Create a receipt.

# **receipt_id_get**
> Receipt receipt_id_get(id)

Get a receipt.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReceiptApi()
id = 'id_example' # str | Receipt id.

try:
    # Get a receipt.
    api_response = api_instance.receipt_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptApi->receipt_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Receipt id. | 

### Return type

[**Receipt**](Receipt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receipt_post**
> Receipt receipt_post(body)

Create a receipt.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReceiptApi()
body = swagger_client.Receipt() # Receipt | 

try:
    # Create a receipt.
    api_response = api_instance.receipt_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptApi->receipt_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Receipt**](Receipt.md)|  | 

### Return type

[**Receipt**](Receipt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

