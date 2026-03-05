# api-client-python.ImageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_images_image_post**](ImageApi.md#create_api_images_image_post) | **POST** /api/images/image | Create
[**delete_api_images_image_pk_delete**](ImageApi.md#delete_api_images_image_pk_delete) | **DELETE** /api/images/image/{pk} | Delete
[**detail_api_images_image_pk_get**](ImageApi.md#detail_api_images_image_pk_get) | **GET** /api/images/image/{pk} | Detail
[**list_api_images_image_get**](ImageApi.md#list_api_images_image_get) | **GET** /api/images/image | List
[**update_api_images_image_pk_patch**](ImageApi.md#update_api_images_image_pk_patch) | **PATCH** /api/images/image/{pk} | Update


# **create_api_images_image_post**
> Image create_api_images_image_post(image)

Create

### Example


```python
import api-client-python
from api-client-python.models.image import Image
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
    api_instance = api-client-python.ImageApi(api_client)
    image = api-client-python.Image() # Image | 

    try:
        # Create
        api_response = api_instance.create_api_images_image_post(image)
        print("The response of ImageApi->create_api_images_image_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->create_api_images_image_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | [**Image**](Image.md)|  | 

### Return type

[**Image**](Image.md)

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

# **delete_api_images_image_pk_delete**
> delete_api_images_image_pk_delete(pk)

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
    api_instance = api-client-python.ImageApi(api_client)
    pk = 'pk_example' # str | 

    try:
        # Delete
        api_instance.delete_api_images_image_pk_delete(pk)
    except Exception as e:
        print("Exception when calling ImageApi->delete_api_images_image_pk_delete: %s\n" % e)
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

# **detail_api_images_image_pk_get**
> Image detail_api_images_image_pk_get(pk, include_relations=include_relations)

Detail

### Example


```python
import api-client-python
from api-client-python.models.image import Image
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
    api_instance = api-client-python.ImageApi(api_client)
    pk = 'pk_example' # str | 
    include_relations = ['include_relations_example'] # List[str] |  (optional)

    try:
        # Detail
        api_response = api_instance.detail_api_images_image_pk_get(pk, include_relations=include_relations)
        print("The response of ImageApi->detail_api_images_image_pk_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->detail_api_images_image_pk_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **str**|  | 
 **include_relations** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**Image**](Image.md)

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

# **list_api_images_image_get**
> ListResponseImage list_api_images_image_get(filters=filters)

List

### Example


```python
import api-client-python
from api-client-python.models.filters_interface import FiltersInterface
from api-client-python.models.list_response_image import ListResponseImage
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
    api_instance = api-client-python.ImageApi(api_client)
    filters = api-client-python.FiltersInterface() # FiltersInterface | FiltersInterface encoded as a deep object (filters[...]) (optional)

    try:
        # List
        api_response = api_instance.list_api_images_image_get(filters=filters)
        print("The response of ImageApi->list_api_images_image_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->list_api_images_image_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | [**FiltersInterface**](.md)| FiltersInterface encoded as a deep object (filters[...]) | [optional] 

### Return type

[**ListResponseImage**](ListResponseImage.md)

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

# **update_api_images_image_pk_patch**
> Image update_api_images_image_pk_patch(pk, body)

Update

### Example


```python
import api-client-python
from api-client-python.models.image import Image
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
    api_instance = api-client-python.ImageApi(api_client)
    pk = 'pk_example' # str | 
    body = None # object | 

    try:
        # Update
        api_response = api_instance.update_api_images_image_pk_patch(pk, body)
        print("The response of ImageApi->update_api_images_image_pk_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->update_api_images_image_pk_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**Image**](Image.md)

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

