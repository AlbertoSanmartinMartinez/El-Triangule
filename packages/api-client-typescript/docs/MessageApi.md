# MessageApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createApiMessagesMessagePost**](MessageApi.md#createapimessagesmessagepost) | **POST** /api/messages/message | Create |
| [**deleteApiMessagesMessagePkDelete**](MessageApi.md#deleteapimessagesmessagepkdelete) | **DELETE** /api/messages/message/{pk} | Delete |
| [**detailApiMessagesMessagePkGet**](MessageApi.md#detailapimessagesmessagepkget) | **GET** /api/messages/message/{pk} | Detail |
| [**listApiMessagesMessageGet**](MessageApi.md#listapimessagesmessageget) | **GET** /api/messages/message | List |
| [**updateApiMessagesMessagePkPatch**](MessageApi.md#updateapimessagesmessagepkpatch) | **PATCH** /api/messages/message/{pk} | Update |



## createApiMessagesMessagePost

> Message createApiMessagesMessagePost(message)

Create

### Example

```ts
import {
  Configuration,
  MessageApi,
} from 'api-client-typescript';
import type { CreateApiMessagesMessagePostRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new MessageApi();

  const body = {
    // Message
    message: ...,
  } satisfies CreateApiMessagesMessagePostRequest;

  try {
    const data = await api.createApiMessagesMessagePost(body);
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
| **message** | [Message](Message.md) |  | |

### Return type

[**Message**](Message.md)

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


## deleteApiMessagesMessagePkDelete

> deleteApiMessagesMessagePkDelete(pk)

Delete

### Example

```ts
import {
  Configuration,
  MessageApi,
} from 'api-client-typescript';
import type { DeleteApiMessagesMessagePkDeleteRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new MessageApi();

  const body = {
    // string
    pk: pk_example,
  } satisfies DeleteApiMessagesMessagePkDeleteRequest;

  try {
    const data = await api.deleteApiMessagesMessagePkDelete(body);
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


## detailApiMessagesMessagePkGet

> Message detailApiMessagesMessagePkGet(pk, includeRelations)

Detail

### Example

```ts
import {
  Configuration,
  MessageApi,
} from 'api-client-typescript';
import type { DetailApiMessagesMessagePkGetRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new MessageApi();

  const body = {
    // string
    pk: pk_example,
    // Array<string> (optional)
    includeRelations: ...,
  } satisfies DetailApiMessagesMessagePkGetRequest;

  try {
    const data = await api.detailApiMessagesMessagePkGet(body);
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

[**Message**](Message.md)

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


## listApiMessagesMessageGet

> ListResponseMessage listApiMessagesMessageGet(filters)

List

### Example

```ts
import {
  Configuration,
  MessageApi,
} from 'api-client-typescript';
import type { ListApiMessagesMessageGetRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new MessageApi();

  const body = {
    // FiltersInterface | FiltersInterface encoded as a deep object (filters[...]) (optional)
    filters: ...,
  } satisfies ListApiMessagesMessageGetRequest;

  try {
    const data = await api.listApiMessagesMessageGet(body);
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

[**ListResponseMessage**](ListResponseMessage.md)

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


## updateApiMessagesMessagePkPatch

> Message updateApiMessagesMessagePkPatch(pk, body)

Update

### Example

```ts
import {
  Configuration,
  MessageApi,
} from 'api-client-typescript';
import type { UpdateApiMessagesMessagePkPatchRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new MessageApi();

  const body = {
    // string
    pk: pk_example,
    // any
    body: ...,
  } satisfies UpdateApiMessagesMessagePkPatchRequest;

  try {
    const data = await api.updateApiMessagesMessagePkPatch(body);
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

[**Message**](Message.md)

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

