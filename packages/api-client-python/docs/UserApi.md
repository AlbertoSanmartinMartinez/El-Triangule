# api-client-python.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_auth_user_post**](UserApi.md#create_api_auth_user_post) | **POST** /api/auth/user | Create
[**delete_api_auth_user_pk_delete**](UserApi.md#delete_api_auth_user_pk_delete) | **DELETE** /api/auth/user/{pk} | Delete
[**detail_api_auth_user_pk_get**](UserApi.md#detail_api_auth_user_pk_get) | **GET** /api/auth/user/{pk} | Detail
[**list_api_auth_user_get**](UserApi.md#list_api_auth_user_get) | **GET** /api/auth/user | List
[**login_api_auth_user_login_post**](UserApi.md#login_api_auth_user_login_post) | **POST** /api/auth/user/login | User login
[**refresh_api_auth_user_refresh_post**](UserApi.md#refresh_api_auth_user_refresh_post) | **POST** /api/auth/user/refresh | Refresh token
[**register_api_auth_user_register_post**](UserApi.md#register_api_auth_user_register_post) | **POST** /api/auth/user/register | User register
[**update_api_auth_user_pk_patch**](UserApi.md#update_api_auth_user_pk_patch) | **PATCH** /api/auth/user/{pk} | Update


# **create_api_auth_user_post**
> User create_api_auth_user_post(user)

Create

### Example


```python
import api-client-python
from api-client-python.models.user import User
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
    api_instance = api-client-python.UserApi(api_client)
    user = api-client-python.User() # User | 

    try:
        # Create
        api_response = api_instance.create_api_auth_user_post(user)
        print("The response of UserApi->create_api_auth_user_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->create_api_auth_user_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

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

# **delete_api_auth_user_pk_delete**
> delete_api_auth_user_pk_delete(pk)

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
    api_instance = api-client-python.UserApi(api_client)
    pk = 'pk_example' # str | 

    try:
        # Delete
        api_instance.delete_api_auth_user_pk_delete(pk)
    except Exception as e:
        print("Exception when calling UserApi->delete_api_auth_user_pk_delete: %s\n" % e)
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

# **detail_api_auth_user_pk_get**
> User detail_api_auth_user_pk_get(pk, include_relations=include_relations)

Detail

### Example


```python
import api-client-python
from api-client-python.models.user import User
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
    api_instance = api-client-python.UserApi(api_client)
    pk = 'pk_example' # str | 
    include_relations = ['include_relations_example'] # List[str] |  (optional)

    try:
        # Detail
        api_response = api_instance.detail_api_auth_user_pk_get(pk, include_relations=include_relations)
        print("The response of UserApi->detail_api_auth_user_pk_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->detail_api_auth_user_pk_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **str**|  | 
 **include_relations** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**User**](User.md)

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

# **list_api_auth_user_get**
> ListResponseUser list_api_auth_user_get(filters=filters)

List

### Example


```python
import api-client-python
from api-client-python.models.filters_interface import FiltersInterface
from api-client-python.models.list_response_user import ListResponseUser
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
    api_instance = api-client-python.UserApi(api_client)
    filters = api-client-python.FiltersInterface() # FiltersInterface | FiltersInterface encoded as a deep object (filters[...]) (optional)

    try:
        # List
        api_response = api_instance.list_api_auth_user_get(filters=filters)
        print("The response of UserApi->list_api_auth_user_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->list_api_auth_user_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | [**FiltersInterface**](.md)| FiltersInterface encoded as a deep object (filters[...]) | [optional] 

### Return type

[**ListResponseUser**](ListResponseUser.md)

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

# **login_api_auth_user_login_post**
> TokenResponse login_api_auth_user_login_post(login_request)

User login

### Example


```python
import api-client-python
from api-client-python.models.login_request import LoginRequest
from api-client-python.models.token_response import TokenResponse
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
    api_instance = api-client-python.UserApi(api_client)
    login_request = api-client-python.LoginRequest() # LoginRequest | 

    try:
        # User login
        api_response = api_instance.login_api_auth_user_login_post(login_request)
        print("The response of UserApi->login_api_auth_user_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->login_api_auth_user_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

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

# **refresh_api_auth_user_refresh_post**
> TokenResponse refresh_api_auth_user_refresh_post(refresh_request)

Refresh token

### Example


```python
import api-client-python
from api-client-python.models.refresh_request import RefreshRequest
from api-client-python.models.token_response import TokenResponse
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
    api_instance = api-client-python.UserApi(api_client)
    refresh_request = api-client-python.RefreshRequest() # RefreshRequest | 

    try:
        # Refresh token
        api_response = api_instance.refresh_api_auth_user_refresh_post(refresh_request)
        print("The response of UserApi->refresh_api_auth_user_refresh_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->refresh_api_auth_user_refresh_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_request** | [**RefreshRequest**](RefreshRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

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

# **register_api_auth_user_register_post**
> TokenResponse register_api_auth_user_register_post(register_request)

User register

### Example


```python
import api-client-python
from api-client-python.models.register_request import RegisterRequest
from api-client-python.models.token_response import TokenResponse
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
    api_instance = api-client-python.UserApi(api_client)
    register_request = api-client-python.RegisterRequest() # RegisterRequest | 

    try:
        # User register
        api_response = api_instance.register_api_auth_user_register_post(register_request)
        print("The response of UserApi->register_api_auth_user_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->register_api_auth_user_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_request** | [**RegisterRequest**](RegisterRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

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

# **update_api_auth_user_pk_patch**
> User update_api_auth_user_pk_patch(pk, body)

Update

### Example


```python
import api-client-python
from api-client-python.models.user import User
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
    api_instance = api-client-python.UserApi(api_client)
    pk = 'pk_example' # str | 
    body = None # object | 

    try:
        # Update
        api_response = api_instance.update_api_auth_user_pk_patch(pk, body)
        print("The response of UserApi->update_api_auth_user_pk_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_api_auth_user_pk_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**User**](User.md)

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

