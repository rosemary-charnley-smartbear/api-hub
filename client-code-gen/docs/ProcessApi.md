# swagger_client.ProcessApi

All URIs are relative to *https://virtserver.swaggerhub.com/Charnley-Test/Billing-Flower-Shop/2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_post**](ProcessApi.md#process_post) | **POST** /process | Process a bill.

# **process_post**
> process_post(body)

Process a bill.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProcessApi()
body = swagger_client.Bill() # Bill | 

try:
    # Process a bill.
    api_instance.process_post(body)
except ApiException as e:
    print("Exception when calling ProcessApi->process_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Bill**](Bill.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

