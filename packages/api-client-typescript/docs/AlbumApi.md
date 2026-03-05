# AlbumApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createApiImagesAlbumPost**](AlbumApi.md#createapiimagesalbumpost) | **POST** /api/images/album | Create |
| [**deleteApiImagesAlbumPkDelete**](AlbumApi.md#deleteapiimagesalbumpkdelete) | **DELETE** /api/images/album/{pk} | Delete |
| [**detailApiImagesAlbumPkGet**](AlbumApi.md#detailapiimagesalbumpkget) | **GET** /api/images/album/{pk} | Detail |
| [**listApiImagesAlbumGet**](AlbumApi.md#listapiimagesalbumget) | **GET** /api/images/album | List |
| [**updateApiImagesAlbumPkPatch**](AlbumApi.md#updateapiimagesalbumpkpatch) | **PATCH** /api/images/album/{pk} | Update |



## createApiImagesAlbumPost

> Album createApiImagesAlbumPost(album)

Create

### Example

```ts
import {
  Configuration,
  AlbumApi,
} from 'api-client-typescript';
import type { CreateApiImagesAlbumPostRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new AlbumApi();

  const body = {
    // Album
    album: ...,
  } satisfies CreateApiImagesAlbumPostRequest;

  try {
    const data = await api.createApiImagesAlbumPost(body);
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
| **album** | [Album](Album.md) |  | |

### Return type

[**Album**](Album.md)

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


## deleteApiImagesAlbumPkDelete

> deleteApiImagesAlbumPkDelete(pk)

Delete

### Example

```ts
import {
  Configuration,
  AlbumApi,
} from 'api-client-typescript';
import type { DeleteApiImagesAlbumPkDeleteRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new AlbumApi();

  const body = {
    // string
    pk: pk_example,
  } satisfies DeleteApiImagesAlbumPkDeleteRequest;

  try {
    const data = await api.deleteApiImagesAlbumPkDelete(body);
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


## detailApiImagesAlbumPkGet

> Album detailApiImagesAlbumPkGet(pk, includeRelations)

Detail

### Example

```ts
import {
  Configuration,
  AlbumApi,
} from 'api-client-typescript';
import type { DetailApiImagesAlbumPkGetRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new AlbumApi();

  const body = {
    // string
    pk: pk_example,
    // Array<string> (optional)
    includeRelations: ...,
  } satisfies DetailApiImagesAlbumPkGetRequest;

  try {
    const data = await api.detailApiImagesAlbumPkGet(body);
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

[**Album**](Album.md)

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


## listApiImagesAlbumGet

> ListResponseAlbum listApiImagesAlbumGet(filters)

List

### Example

```ts
import {
  Configuration,
  AlbumApi,
} from 'api-client-typescript';
import type { ListApiImagesAlbumGetRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new AlbumApi();

  const body = {
    // FiltersInterface | FiltersInterface encoded as a deep object (filters[...]) (optional)
    filters: ...,
  } satisfies ListApiImagesAlbumGetRequest;

  try {
    const data = await api.listApiImagesAlbumGet(body);
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

[**ListResponseAlbum**](ListResponseAlbum.md)

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


## updateApiImagesAlbumPkPatch

> Album updateApiImagesAlbumPkPatch(pk, body)

Update

### Example

```ts
import {
  Configuration,
  AlbumApi,
} from 'api-client-typescript';
import type { UpdateApiImagesAlbumPkPatchRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new AlbumApi();

  const body = {
    // string
    pk: pk_example,
    // any
    body: ...,
  } satisfies UpdateApiImagesAlbumPkPatchRequest;

  try {
    const data = await api.updateApiImagesAlbumPkPatch(body);
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

[**Album**](Album.md)

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

