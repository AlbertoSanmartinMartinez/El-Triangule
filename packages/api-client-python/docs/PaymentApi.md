# api-client-python.PaymentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_payments_payment_post**](PaymentApi.md#create_api_payments_payment_post) | **POST** /api/payments/payment | Create
[**delete_api_payments_payment_pk_delete**](PaymentApi.md#delete_api_payments_payment_pk_delete) | **DELETE** /api/payments/payment/{pk} | Delete
[**detail_api_payments_payment_pk_get**](PaymentApi.md#detail_api_payments_payment_pk_get) | **GET** /api/payments/payment/{pk} | Detail
[**list_api_payments_payment_get**](PaymentApi.md#list_api_payments_payment_get) | **GET** /api/payments/payment | List
[**refund_payment_api_payments_payment_uuid_refund_post**](PaymentApi.md#refund_payment_api_payments_payment_uuid_refund_post) | **POST** /api/payments/payment/{uuid}/refund | Refund payment
[**update_api_payments_payment_pk_patch**](PaymentApi.md#update_api_payments_payment_pk_patch) | **PATCH** /api/payments/payment/{pk} | Update


# **create_api_payments_payment_post**
> Payment create_api_payments_payment_post(payment)

Create

### Example


```python
import api-client-python
from api-client-python.models.payment import Payment
from api-client-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = api-client-python.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with api-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api-client-python.PaymentApi(api_client)
    payment = api-client-python.Payment() # Payment | 

    try:
        # Create
        api_response = api_instance.create_api_payments_payment_post(payment)
        print("The response of PaymentApi->create_api_payments_payment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->create_api_payments_payment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment** | [**Payment**](Payment.md)|  | 

### Return type

[**Payment**](Payment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_payments_payment_pk_delete**
> delete_api_payments_payment_pk_delete(pk)

Delete

### Example


```python
import api-client-python
from api-client-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = api-client-python.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with api-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api-client-python.PaymentApi(api_client)
    pk = 'pk_example' # str | 

    try:
        # Delete
        api_instance.delete_api_payments_payment_pk_delete(pk)
    except Exception as e:
        print("Exception when calling PaymentApi->delete_api_payments_payment_pk_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_api_payments_payment_pk_get**
> Payment detail_api_payments_payment_pk_get(pk, include_relations=include_relations)

Detail

### Example


```python
import api-client-python
from api-client-python.models.payment import Payment
from api-client-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = api-client-python.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with api-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api-client-python.PaymentApi(api_client)
    pk = 'pk_example' # str | 
    include_relations = ['include_relations_example'] # List[str] |  (optional)

    try:
        # Detail
        api_response = api_instance.detail_api_payments_payment_pk_get(pk, include_relations=include_relations)
        print("The response of PaymentApi->detail_api_payments_payment_pk_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->detail_api_payments_payment_pk_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **str**|  | 
 **include_relations** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**Payment**](Payment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_payments_payment_get**
> ListResponsePayment list_api_payments_payment_get(filters=filters)

List

### Example


```python
import api-client-python
from api-client-python.models.filters_interface import FiltersInterface
from api-client-python.models.list_response_payment import ListResponsePayment
from api-client-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = api-client-python.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with api-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api-client-python.PaymentApi(api_client)
    filters = api-client-python.FiltersInterface() # FiltersInterface | FiltersInterface encoded as a deep object (filters[...]) (optional)

    try:
        # List
        api_response = api_instance.list_api_payments_payment_get(filters=filters)
        print("The response of PaymentApi->list_api_payments_payment_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->list_api_payments_payment_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | [**FiltersInterface**](.md)| FiltersInterface encoded as a deep object (filters[...]) | [optional] 

### Return type

[**ListResponsePayment**](ListResponsePayment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_payment_api_payments_payment_uuid_refund_post**
> Payment refund_payment_api_payments_payment_uuid_refund_post(uuid)

Refund payment

### Example


```python
import api-client-python
from api-client-python.models.payment import Payment
from api-client-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = api-client-python.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with api-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api-client-python.PaymentApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Refund payment
        api_response = api_instance.refund_payment_api_payments_payment_uuid_refund_post(uuid)
        print("The response of PaymentApi->refund_payment_api_payments_payment_uuid_refund_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->refund_payment_api_payments_payment_uuid_refund_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**Payment**](Payment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_payments_payment_pk_patch**
> Payment update_api_payments_payment_pk_patch(pk, body)

Update

### Example


```python
import api-client-python
from api-client-python.models.payment import Payment
from api-client-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = api-client-python.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with api-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api-client-python.PaymentApi(api_client)
    pk = 'pk_example' # str | 
    body = None # object | 

    try:
        # Update
        api_response = api_instance.update_api_payments_payment_pk_patch(pk, body)
        print("The response of PaymentApi->update_api_payments_payment_pk_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->update_api_payments_payment_pk_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**Payment**](Payment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

