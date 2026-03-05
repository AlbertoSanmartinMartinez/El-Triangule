# api-client-python.ConversationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_member_api_messages_conversation_uuid_member_post**](ConversationApi.md#add_member_api_messages_conversation_uuid_member_post) | **POST** /api/messages/conversation/{uuid}/member | Add member to conversation
[**create_api_messages_conversation_post**](ConversationApi.md#create_api_messages_conversation_post) | **POST** /api/messages/conversation | Create
[**delete_api_messages_conversation_pk_delete**](ConversationApi.md#delete_api_messages_conversation_pk_delete) | **DELETE** /api/messages/conversation/{pk} | Delete
[**detail_api_messages_conversation_pk_get**](ConversationApi.md#detail_api_messages_conversation_pk_get) | **GET** /api/messages/conversation/{pk} | Detail
[**list_api_messages_conversation_get**](ConversationApi.md#list_api_messages_conversation_get) | **GET** /api/messages/conversation | List
[**remove_member_api_messages_conversation_uuid_member_user_uuid_delete**](ConversationApi.md#remove_member_api_messages_conversation_uuid_member_user_uuid_delete) | **DELETE** /api/messages/conversation/{uuid}/member/{user_uuid} | Remove member from conversation
[**update_api_messages_conversation_pk_patch**](ConversationApi.md#update_api_messages_conversation_pk_patch) | **PATCH** /api/messages/conversation/{pk} | Update


# **add_member_api_messages_conversation_uuid_member_post**
> ConversationMember add_member_api_messages_conversation_uuid_member_post(uuid, add_member_request)

Add member to conversation

### Example


```python
import api-client-python
from api-client-python.models.add_member_request import AddMemberRequest
from api-client-python.models.conversation_member import ConversationMember
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
    api_instance = api-client-python.ConversationApi(api_client)
    uuid = 'uuid_example' # str | 
    add_member_request = api-client-python.AddMemberRequest() # AddMemberRequest | 

    try:
        # Add member to conversation
        api_response = api_instance.add_member_api_messages_conversation_uuid_member_post(uuid, add_member_request)
        print("The response of ConversationApi->add_member_api_messages_conversation_uuid_member_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationApi->add_member_api_messages_conversation_uuid_member_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **add_member_request** | [**AddMemberRequest**](AddMemberRequest.md)|  | 

### Return type

[**ConversationMember**](ConversationMember.md)

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

# **create_api_messages_conversation_post**
> Conversation create_api_messages_conversation_post(conversation)

Create

### Example


```python
import api-client-python
from api-client-python.models.conversation import Conversation
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
    api_instance = api-client-python.ConversationApi(api_client)
    conversation = api-client-python.Conversation() # Conversation | 

    try:
        # Create
        api_response = api_instance.create_api_messages_conversation_post(conversation)
        print("The response of ConversationApi->create_api_messages_conversation_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationApi->create_api_messages_conversation_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation** | [**Conversation**](Conversation.md)|  | 

### Return type

[**Conversation**](Conversation.md)

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

# **delete_api_messages_conversation_pk_delete**
> delete_api_messages_conversation_pk_delete(pk)

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
    api_instance = api-client-python.ConversationApi(api_client)
    pk = 'pk_example' # str | 

    try:
        # Delete
        api_instance.delete_api_messages_conversation_pk_delete(pk)
    except Exception as e:
        print("Exception when calling ConversationApi->delete_api_messages_conversation_pk_delete: %s\n" % e)
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

# **detail_api_messages_conversation_pk_get**
> Conversation detail_api_messages_conversation_pk_get(pk, include_relations=include_relations)

Detail

### Example


```python
import api-client-python
from api-client-python.models.conversation import Conversation
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
    api_instance = api-client-python.ConversationApi(api_client)
    pk = 'pk_example' # str | 
    include_relations = ['include_relations_example'] # List[str] |  (optional)

    try:
        # Detail
        api_response = api_instance.detail_api_messages_conversation_pk_get(pk, include_relations=include_relations)
        print("The response of ConversationApi->detail_api_messages_conversation_pk_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationApi->detail_api_messages_conversation_pk_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **str**|  | 
 **include_relations** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**Conversation**](Conversation.md)

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

# **list_api_messages_conversation_get**
> ListResponseConversation list_api_messages_conversation_get(filters=filters)

List

### Example


```python
import api-client-python
from api-client-python.models.filters_interface import FiltersInterface
from api-client-python.models.list_response_conversation import ListResponseConversation
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
    api_instance = api-client-python.ConversationApi(api_client)
    filters = api-client-python.FiltersInterface() # FiltersInterface | FiltersInterface encoded as a deep object (filters[...]) (optional)

    try:
        # List
        api_response = api_instance.list_api_messages_conversation_get(filters=filters)
        print("The response of ConversationApi->list_api_messages_conversation_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationApi->list_api_messages_conversation_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | [**FiltersInterface**](.md)| FiltersInterface encoded as a deep object (filters[...]) | [optional] 

### Return type

[**ListResponseConversation**](ListResponseConversation.md)

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

# **remove_member_api_messages_conversation_uuid_member_user_uuid_delete**
> remove_member_api_messages_conversation_uuid_member_user_uuid_delete(uuid, user_uuid)

Remove member from conversation

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
    api_instance = api-client-python.ConversationApi(api_client)
    uuid = 'uuid_example' # str | 
    user_uuid = 'user_uuid_example' # str | 

    try:
        # Remove member from conversation
        api_instance.remove_member_api_messages_conversation_uuid_member_user_uuid_delete(uuid, user_uuid)
    except Exception as e:
        print("Exception when calling ConversationApi->remove_member_api_messages_conversation_uuid_member_user_uuid_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **user_uuid** | **str**|  | 

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

# **update_api_messages_conversation_pk_patch**
> Conversation update_api_messages_conversation_pk_patch(pk, body)

Update

### Example


```python
import api-client-python
from api-client-python.models.conversation import Conversation
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
    api_instance = api-client-python.ConversationApi(api_client)
    pk = 'pk_example' # str | 
    body = None # object | 

    try:
        # Update
        api_response = api_instance.update_api_messages_conversation_pk_patch(pk, body)
        print("The response of ConversationApi->update_api_messages_conversation_pk_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationApi->update_api_messages_conversation_pk_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**Conversation**](Conversation.md)

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

