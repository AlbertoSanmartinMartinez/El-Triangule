# ImageApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createApiImagesImagePost**](ImageApi.md#createapiimagesimagepost) | **POST** /api/images/image | Create |
| [**deleteApiImagesImagePkDelete**](ImageApi.md#deleteapiimagesimagepkdelete) | **DELETE** /api/images/image/{pk} | Delete |
| [**detailApiImagesImagePkGet**](ImageApi.md#detailapiimagesimagepkget) | **GET** /api/images/image/{pk} | Detail |
| [**listApiImagesImageGet**](ImageApi.md#listapiimagesimageget) | **GET** /api/images/image | List |
| [**updateApiImagesImagePkPatch**](ImageApi.md#updateapiimagesimagepkpatch) | **PATCH** /api/images/image/{pk} | Update |



## createApiImagesImagePost

> Image createApiImagesImagePost(image)

Create

### Example

```ts
import {
  Configuration,
  ImageApi,
} from 'api-client-typescript';
import type { CreateApiImagesImagePostRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new ImageApi();

  const body = {
    // Image
    image: ...,
  } satisfies CreateApiImagesImagePostRequest;

  try {
    const data = await api.createApiImagesImagePost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **image** | [Image](Image.md) |  | |

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteApiImagesImagePkDelete

> deleteApiImagesImagePkDelete(pk)

Delete

### Example

```ts
import {
  Configuration,
  ImageApi,
} from 'api-client-typescript';
import type { DeleteApiImagesImagePkDeleteRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new ImageApi();

  const body = {
    // string
    pk: pk_example,
  } satisfies DeleteApiImagesImagePkDeleteRequest;

  try {
    const data = await api.deleteApiImagesImagePkDelete(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pk** | `string` |  | [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## detailApiImagesImagePkGet

> Image detailApiImagesImagePkGet(pk, includeRelations)

Detail

### Example

```ts
import {
  Configuration,
  ImageApi,
} from 'api-client-typescript';
import type { DetailApiImagesImagePkGetRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new ImageApi();

  const body = {
    // string
    pk: pk_example,
    // Array<string> (optional)
    includeRelations: ...,
  } satisfies DetailApiImagesImagePkGetRequest;

  try {
    const data = await api.detailApiImagesImagePkGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pk** | `string` |  | [Defaults to `undefined`] |
| **includeRelations** | `Array<string>` |  | [Optional] |

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listApiImagesImageGet

> ListResponseImage listApiImagesImageGet(filters)

List

### Example

```ts
import {
  Configuration,
  ImageApi,
} from 'api-client-typescript';
import type { ListApiImagesImageGetRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new ImageApi();

  const body = {
    // FiltersInterface | FiltersInterface encoded as a deep object (filters[...]) (optional)
    filters: ...,
  } satisfies ListApiImagesImageGetRequest;

  try {
    const data = await api.listApiImagesImageGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **filters** | [](.md) | FiltersInterface encoded as a deep object (filters[...]) | [Optional] [Defaults to `undefined`] |

### Return type

[**ListResponseImage**](ListResponseImage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateApiImagesImagePkPatch

> Image updateApiImagesImagePkPatch(pk, body)

Update

### Example

```ts
import {
  Configuration,
  ImageApi,
} from 'api-client-typescript';
import type { UpdateApiImagesImagePkPatchRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new ImageApi();

  const body = {
    // string
    pk: pk_example,
    // any
    body: ...,
  } satisfies UpdateApiImagesImagePkPatchRequest;

  try {
    const data = await api.updateApiImagesImagePkPatch(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pk** | `string` |  | [Defaults to `undefined`] |
| **body** | `any` |  | |

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

