# swagger_client.BillApi

All URIs are relative to *https://virtserver.swaggerhub.com/Charnley-Test/Billing-Flower-Shop/2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bill_id_get**](BillApi.md#bill_id_get) | **GET** /bill/{id} | Get a bill.
[**bill_post**](BillApi.md#bill_post) | **POST** /bill | Submit a bill.

# **bill_id_get**
> Bill bill_id_get(id)

Get a bill.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillApi()
id = 'id_example' # str | Bill id.

try:
    # Get a bill.
    api_response = api_instance.bill_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillApi->bill_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Bill id. | 

### Return type

[**Bill**](Bill.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bill_post**
> Bill bill_post(body)

Submit a bill.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillApi()
body = swagger_client.Bill() # Bill | 

try:
    # Submit a bill.
    api_response = api_instance.bill_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillApi->bill_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Bill**](Bill.md)|  | 

### Return type

[**Bill**](Bill.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

