# EventApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createApiEventsEventPost**](EventApi.md#createapieventseventpost) | **POST** /api/events/event | Create |
| [**deleteApiEventsEventPkDelete**](EventApi.md#deleteapieventseventpkdelete) | **DELETE** /api/events/event/{pk} | Delete |
| [**detailApiEventsEventPkGet**](EventApi.md#detailapieventseventpkget) | **GET** /api/events/event/{pk} | Detail |
| [**listApiEventsEventGet**](EventApi.md#listapieventseventget) | **GET** /api/events/event | List |
| [**registerEventApiEventsEventUuidRegisterPost**](EventApi.md#registereventapieventseventuuidregisterpost) | **POST** /api/events/event/{uuid}/register | Register to event |
| [**unregisterEventApiEventsEventUuidRegisterDelete**](EventApi.md#unregistereventapieventseventuuidregisterdelete) | **DELETE** /api/events/event/{uuid}/register | Unregister from event |
| [**updateApiEventsEventPkPatch**](EventApi.md#updateapieventseventpkpatch) | **PATCH** /api/events/event/{pk} | Update |



## createApiEventsEventPost

> Event createApiEventsEventPost(event)

Create

### Example

```ts
import {
  Configuration,
  EventApi,
} from 'api-client-typescript';
import type { CreateApiEventsEventPostRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new EventApi();

  const body = {
    // Event
    event: ...,
  } satisfies CreateApiEventsEventPostRequest;

  try {
    const data = await api.createApiEventsEventPost(body);
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
| **event** | [Event](Event.md) |  | |

### Return type

[**Event**](Event.md)

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


## deleteApiEventsEventPkDelete

> deleteApiEventsEventPkDelete(pk)

Delete

### Example

```ts
import {
  Configuration,
  EventApi,
} from 'api-client-typescript';
import type { DeleteApiEventsEventPkDeleteRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new EventApi();

  const body = {
    // string
    pk: pk_example,
  } satisfies DeleteApiEventsEventPkDeleteRequest;

  try {
    const data = await api.deleteApiEventsEventPkDelete(body);
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


## detailApiEventsEventPkGet

> Event detailApiEventsEventPkGet(pk, includeRelations)

Detail

### Example

```ts
import {
  Configuration,
  EventApi,
} from 'api-client-typescript';
import type { DetailApiEventsEventPkGetRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new EventApi();

  const body = {
    // string
    pk: pk_example,
    // Array<string> (optional)
    includeRelations: ...,
  } satisfies DetailApiEventsEventPkGetRequest;

  try {
    const data = await api.detailApiEventsEventPkGet(body);
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

[**Event**](Event.md)

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


## listApiEventsEventGet

> ListResponseEvent listApiEventsEventGet(filters)

List

### Example

```ts
import {
  Configuration,
  EventApi,
} from 'api-client-typescript';
import type { ListApiEventsEventGetRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new EventApi();

  const body = {
    // FiltersInterface | FiltersInterface encoded as a deep object (filters[...]) (optional)
    filters: ...,
  } satisfies ListApiEventsEventGetRequest;

  try {
    const data = await api.listApiEventsEventGet(body);
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

[**ListResponseEvent**](ListResponseEvent.md)

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


## registerEventApiEventsEventUuidRegisterPost

> any registerEventApiEventsEventUuidRegisterPost(uuid)

Register to event

### Example

```ts
import {
  Configuration,
  EventApi,
} from 'api-client-typescript';
import type { RegisterEventApiEventsEventUuidRegisterPostRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new EventApi();

  const body = {
    // string
    uuid: uuid_example,
  } satisfies RegisterEventApiEventsEventUuidRegisterPostRequest;

  try {
    const data = await api.registerEventApiEventsEventUuidRegisterPost(body);
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
| **uuid** | `string` |  | [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## unregisterEventApiEventsEventUuidRegisterDelete

> unregisterEventApiEventsEventUuidRegisterDelete(uuid)

Unregister from event

### Example

```ts
import {
  Configuration,
  EventApi,
} from 'api-client-typescript';
import type { UnregisterEventApiEventsEventUuidRegisterDeleteRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new EventApi();

  const body = {
    // string
    uuid: uuid_example,
  } satisfies UnregisterEventApiEventsEventUuidRegisterDeleteRequest;

  try {
    const data = await api.unregisterEventApiEventsEventUuidRegisterDelete(body);
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
| **uuid** | `string` |  | [Defaults to `undefined`] |

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


## updateApiEventsEventPkPatch

> Event updateApiEventsEventPkPatch(pk, body)

Update

### Example

```ts
import {
  Configuration,
  EventApi,
} from 'api-client-typescript';
import type { UpdateApiEventsEventPkPatchRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new EventApi();

  const body = {
    // string
    pk: pk_example,
    // any
    body: ...,
  } satisfies UpdateApiEventsEventPkPatchRequest;

  try {
    const data = await api.updateApiEventsEventPkPatch(body);
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

[**Event**](Event.md)

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

