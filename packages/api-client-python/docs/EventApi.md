# api-client-python.EventApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_events_event_post**](EventApi.md#create_api_events_event_post) | **POST** /api/events/event | Create
[**delete_api_events_event_pk_delete**](EventApi.md#delete_api_events_event_pk_delete) | **DELETE** /api/events/event/{pk} | Delete
[**detail_api_events_event_pk_get**](EventApi.md#detail_api_events_event_pk_get) | **GET** /api/events/event/{pk} | Detail
[**list_api_events_event_get**](EventApi.md#list_api_events_event_get) | **GET** /api/events/event | List
[**register_event_api_events_event_uuid_register_post**](EventApi.md#register_event_api_events_event_uuid_register_post) | **POST** /api/events/event/{uuid}/register | Register to event
[**unregister_event_api_events_event_uuid_register_delete**](EventApi.md#unregister_event_api_events_event_uuid_register_delete) | **DELETE** /api/events/event/{uuid}/register | Unregister from event
[**update_api_events_event_pk_patch**](EventApi.md#update_api_events_event_pk_patch) | **PATCH** /api/events/event/{pk} | Update


# **create_api_events_event_post**
> Event create_api_events_event_post(event)

Create

### Example


```python
import api-client-python
from api-client-python.models.event import Event
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
    api_instance = api-client-python.EventApi(api_client)
    event = api-client-python.Event() # Event | 

    try:
        # Create
        api_response = api_instance.create_api_events_event_post(event)
        print("The response of EventApi->create_api_events_event_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->create_api_events_event_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event** | [**Event**](Event.md)|  | 

### Return type

[**Event**](Event.md)

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

# **delete_api_events_event_pk_delete**
> delete_api_events_event_pk_delete(pk)

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
    api_instance = api-client-python.EventApi(api_client)
    pk = 'pk_example' # str | 

    try:
        # Delete
        api_instance.delete_api_events_event_pk_delete(pk)
    except Exception as e:
        print("Exception when calling EventApi->delete_api_events_event_pk_delete: %s\n" % e)
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

# **detail_api_events_event_pk_get**
> Event detail_api_events_event_pk_get(pk, include_relations=include_relations)

Detail

### Example


```python
import api-client-python
from api-client-python.models.event import Event
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
    api_instance = api-client-python.EventApi(api_client)
    pk = 'pk_example' # str | 
    include_relations = ['include_relations_example'] # List[str] |  (optional)

    try:
        # Detail
        api_response = api_instance.detail_api_events_event_pk_get(pk, include_relations=include_relations)
        print("The response of EventApi->detail_api_events_event_pk_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->detail_api_events_event_pk_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **str**|  | 
 **include_relations** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**Event**](Event.md)

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

# **list_api_events_event_get**
> ListResponseEvent list_api_events_event_get(filters=filters)

List

### Example


```python
import api-client-python
from api-client-python.models.filters_interface import FiltersInterface
from api-client-python.models.list_response_event import ListResponseEvent
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
    api_instance = api-client-python.EventApi(api_client)
    filters = api-client-python.FiltersInterface() # FiltersInterface | FiltersInterface encoded as a deep object (filters[...]) (optional)

    try:
        # List
        api_response = api_instance.list_api_events_event_get(filters=filters)
        print("The response of EventApi->list_api_events_event_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->list_api_events_event_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | [**FiltersInterface**](.md)| FiltersInterface encoded as a deep object (filters[...]) | [optional] 

### Return type

[**ListResponseEvent**](ListResponseEvent.md)

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

# **register_event_api_events_event_uuid_register_post**
> object register_event_api_events_event_uuid_register_post(uuid)

Register to event

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
    api_instance = api-client-python.EventApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Register to event
        api_response = api_instance.register_event_api_events_event_uuid_register_post(uuid)
        print("The response of EventApi->register_event_api_events_event_uuid_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->register_event_api_events_event_uuid_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_event_api_events_event_uuid_register_delete**
> unregister_event_api_events_event_uuid_register_delete(uuid)

Unregister from event

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
    api_instance = api-client-python.EventApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Unregister from event
        api_instance.unregister_event_api_events_event_uuid_register_delete(uuid)
    except Exception as e:
        print("Exception when calling EventApi->unregister_event_api_events_event_uuid_register_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

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

# **update_api_events_event_pk_patch**
> Event update_api_events_event_pk_patch(pk, body)

Update

### Example


```python
import api-client-python
from api-client-python.models.event import Event
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
    api_instance = api-client-python.EventApi(api_client)
    pk = 'pk_example' # str | 
    body = None # object | 

    try:
        # Update
        api_response = api_instance.update_api_events_event_pk_patch(pk, body)
        print("The response of EventApi->update_api_events_event_pk_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->update_api_events_event_pk_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**Event**](Event.md)

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

