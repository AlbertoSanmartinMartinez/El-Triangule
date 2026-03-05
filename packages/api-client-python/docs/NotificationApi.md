# api-client-python.NotificationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_notifications_notification_post**](NotificationApi.md#create_api_notifications_notification_post) | **POST** /api/notifications/notification | Create
[**delete_api_notifications_notification_pk_delete**](NotificationApi.md#delete_api_notifications_notification_pk_delete) | **DELETE** /api/notifications/notification/{pk} | Delete
[**detail_api_notifications_notification_pk_get**](NotificationApi.md#detail_api_notifications_notification_pk_get) | **GET** /api/notifications/notification/{pk} | Detail
[**list_api_notifications_notification_get**](NotificationApi.md#list_api_notifications_notification_get) | **GET** /api/notifications/notification | List
[**mark_all_read_api_notifications_notification_read_all_patch**](NotificationApi.md#mark_all_read_api_notifications_notification_read_all_patch) | **PATCH** /api/notifications/notification/read-all | Mark all notifications as read
[**mark_read_api_notifications_notification_uuid_read_patch**](NotificationApi.md#mark_read_api_notifications_notification_uuid_read_patch) | **PATCH** /api/notifications/notification/{uuid}/read | Mark notification as read
[**unread_count_api_notifications_notification_unread_count_get**](NotificationApi.md#unread_count_api_notifications_notification_unread_count_get) | **GET** /api/notifications/notification/unread-count | Unread notifications count
[**update_api_notifications_notification_pk_patch**](NotificationApi.md#update_api_notifications_notification_pk_patch) | **PATCH** /api/notifications/notification/{pk} | Update


# **create_api_notifications_notification_post**
> Notification create_api_notifications_notification_post(notification)

Create

### Example


```python
import api-client-python
from api-client-python.models.notification import Notification
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
    api_instance = api-client-python.NotificationApi(api_client)
    notification = api-client-python.Notification() # Notification | 

    try:
        # Create
        api_response = api_instance.create_api_notifications_notification_post(notification)
        print("The response of NotificationApi->create_api_notifications_notification_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->create_api_notifications_notification_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification** | [**Notification**](Notification.md)|  | 

### Return type

[**Notification**](Notification.md)

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

# **delete_api_notifications_notification_pk_delete**
> delete_api_notifications_notification_pk_delete(pk)

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
    api_instance = api-client-python.NotificationApi(api_client)
    pk = 'pk_example' # str | 

    try:
        # Delete
        api_instance.delete_api_notifications_notification_pk_delete(pk)
    except Exception as e:
        print("Exception when calling NotificationApi->delete_api_notifications_notification_pk_delete: %s\n" % e)
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

# **detail_api_notifications_notification_pk_get**
> Notification detail_api_notifications_notification_pk_get(pk, include_relations=include_relations)

Detail

### Example


```python
import api-client-python
from api-client-python.models.notification import Notification
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
    api_instance = api-client-python.NotificationApi(api_client)
    pk = 'pk_example' # str | 
    include_relations = ['include_relations_example'] # List[str] |  (optional)

    try:
        # Detail
        api_response = api_instance.detail_api_notifications_notification_pk_get(pk, include_relations=include_relations)
        print("The response of NotificationApi->detail_api_notifications_notification_pk_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->detail_api_notifications_notification_pk_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **str**|  | 
 **include_relations** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**Notification**](Notification.md)

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

# **list_api_notifications_notification_get**
> ListResponseNotification list_api_notifications_notification_get(filters=filters)

List

### Example


```python
import api-client-python
from api-client-python.models.filters_interface import FiltersInterface
from api-client-python.models.list_response_notification import ListResponseNotification
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
    api_instance = api-client-python.NotificationApi(api_client)
    filters = api-client-python.FiltersInterface() # FiltersInterface | FiltersInterface encoded as a deep object (filters[...]) (optional)

    try:
        # List
        api_response = api_instance.list_api_notifications_notification_get(filters=filters)
        print("The response of NotificationApi->list_api_notifications_notification_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->list_api_notifications_notification_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | [**FiltersInterface**](.md)| FiltersInterface encoded as a deep object (filters[...]) | [optional] 

### Return type

[**ListResponseNotification**](ListResponseNotification.md)

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

# **mark_all_read_api_notifications_notification_read_all_patch**
> object mark_all_read_api_notifications_notification_read_all_patch()

Mark all notifications as read

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
    api_instance = api-client-python.NotificationApi(api_client)

    try:
        # Mark all notifications as read
        api_response = api_instance.mark_all_read_api_notifications_notification_read_all_patch()
        print("The response of NotificationApi->mark_all_read_api_notifications_notification_read_all_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->mark_all_read_api_notifications_notification_read_all_patch: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_read_api_notifications_notification_uuid_read_patch**
> object mark_read_api_notifications_notification_uuid_read_patch(uuid)

Mark notification as read

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
    api_instance = api-client-python.NotificationApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Mark notification as read
        api_response = api_instance.mark_read_api_notifications_notification_uuid_read_patch(uuid)
        print("The response of NotificationApi->mark_read_api_notifications_notification_uuid_read_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->mark_read_api_notifications_notification_uuid_read_patch: %s\n" % e)
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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unread_count_api_notifications_notification_unread_count_get**
> object unread_count_api_notifications_notification_unread_count_get()

Unread notifications count

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
    api_instance = api-client-python.NotificationApi(api_client)

    try:
        # Unread notifications count
        api_response = api_instance.unread_count_api_notifications_notification_unread_count_get()
        print("The response of NotificationApi->unread_count_api_notifications_notification_unread_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->unread_count_api_notifications_notification_unread_count_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_notifications_notification_pk_patch**
> Notification update_api_notifications_notification_pk_patch(pk, body)

Update

### Example


```python
import api-client-python
from api-client-python.models.notification import Notification
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
    api_instance = api-client-python.NotificationApi(api_client)
    pk = 'pk_example' # str | 
    body = None # object | 

    try:
        # Update
        api_response = api_instance.update_api_notifications_notification_pk_patch(pk, body)
        print("The response of NotificationApi->update_api_notifications_notification_pk_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->update_api_notifications_notification_pk_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**Notification**](Notification.md)

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

