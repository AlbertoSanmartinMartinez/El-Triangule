# NotificationApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createApiNotificationsNotificationPost**](NotificationApi.md#createapinotificationsnotificationpost) | **POST** /api/notifications/notification | Create |
| [**deleteApiNotificationsNotificationPkDelete**](NotificationApi.md#deleteapinotificationsnotificationpkdelete) | **DELETE** /api/notifications/notification/{pk} | Delete |
| [**detailApiNotificationsNotificationPkGet**](NotificationApi.md#detailapinotificationsnotificationpkget) | **GET** /api/notifications/notification/{pk} | Detail |
| [**listApiNotificationsNotificationGet**](NotificationApi.md#listapinotificationsnotificationget) | **GET** /api/notifications/notification | List |
| [**markAllReadApiNotificationsNotificationReadAllPatch**](NotificationApi.md#markallreadapinotificationsnotificationreadallpatch) | **PATCH** /api/notifications/notification/read-all | Mark all notifications as read |
| [**markReadApiNotificationsNotificationUuidReadPatch**](NotificationApi.md#markreadapinotificationsnotificationuuidreadpatch) | **PATCH** /api/notifications/notification/{uuid}/read | Mark notification as read |
| [**unreadCountApiNotificationsNotificationUnreadCountGet**](NotificationApi.md#unreadcountapinotificationsnotificationunreadcountget) | **GET** /api/notifications/notification/unread-count | Unread notifications count |
| [**updateApiNotificationsNotificationPkPatch**](NotificationApi.md#updateapinotificationsnotificationpkpatch) | **PATCH** /api/notifications/notification/{pk} | Update |



## createApiNotificationsNotificationPost

> Notification createApiNotificationsNotificationPost(notification)

Create

### Example

```ts
import {
  Configuration,
  NotificationApi,
} from 'api-client-typescript';
import type { CreateApiNotificationsNotificationPostRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new NotificationApi();

  const body = {
    // Notification
    notification: ...,
  } satisfies CreateApiNotificationsNotificationPostRequest;

  try {
    const data = await api.createApiNotificationsNotificationPost(body);
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
| **notification** | [Notification](Notification.md) |  | |

### Return type

[**Notification**](Notification.md)

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


## deleteApiNotificationsNotificationPkDelete

> deleteApiNotificationsNotificationPkDelete(pk)

Delete

### Example

```ts
import {
  Configuration,
  NotificationApi,
} from 'api-client-typescript';
import type { DeleteApiNotificationsNotificationPkDeleteRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new NotificationApi();

  const body = {
    // string
    pk: pk_example,
  } satisfies DeleteApiNotificationsNotificationPkDeleteRequest;

  try {
    const data = await api.deleteApiNotificationsNotificationPkDelete(body);
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


## detailApiNotificationsNotificationPkGet

> Notification detailApiNotificationsNotificationPkGet(pk, includeRelations)

Detail

### Example

```ts
import {
  Configuration,
  NotificationApi,
} from 'api-client-typescript';
import type { DetailApiNotificationsNotificationPkGetRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new NotificationApi();

  const body = {
    // string
    pk: pk_example,
    // Array<string> (optional)
    includeRelations: ...,
  } satisfies DetailApiNotificationsNotificationPkGetRequest;

  try {
    const data = await api.detailApiNotificationsNotificationPkGet(body);
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

[**Notification**](Notification.md)

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


## listApiNotificationsNotificationGet

> ListResponseNotification listApiNotificationsNotificationGet(filters)

List

### Example

```ts
import {
  Configuration,
  NotificationApi,
} from 'api-client-typescript';
import type { ListApiNotificationsNotificationGetRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new NotificationApi();

  const body = {
    // FiltersInterface | FiltersInterface encoded as a deep object (filters[...]) (optional)
    filters: ...,
  } satisfies ListApiNotificationsNotificationGetRequest;

  try {
    const data = await api.listApiNotificationsNotificationGet(body);
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

[**ListResponseNotification**](ListResponseNotification.md)

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


## markAllReadApiNotificationsNotificationReadAllPatch

> any markAllReadApiNotificationsNotificationReadAllPatch()

Mark all notifications as read

### Example

```ts
import {
  Configuration,
  NotificationApi,
} from 'api-client-typescript';
import type { MarkAllReadApiNotificationsNotificationReadAllPatchRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new NotificationApi();

  try {
    const data = await api.markAllReadApiNotificationsNotificationReadAllPatch();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

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
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## markReadApiNotificationsNotificationUuidReadPatch

> any markReadApiNotificationsNotificationUuidReadPatch(uuid)

Mark notification as read

### Example

```ts
import {
  Configuration,
  NotificationApi,
} from 'api-client-typescript';
import type { MarkReadApiNotificationsNotificationUuidReadPatchRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new NotificationApi();

  const body = {
    // string
    uuid: uuid_example,
  } satisfies MarkReadApiNotificationsNotificationUuidReadPatchRequest;

  try {
    const data = await api.markReadApiNotificationsNotificationUuidReadPatch(body);
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
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## unreadCountApiNotificationsNotificationUnreadCountGet

> any unreadCountApiNotificationsNotificationUnreadCountGet()

Unread notifications count

### Example

```ts
import {
  Configuration,
  NotificationApi,
} from 'api-client-typescript';
import type { UnreadCountApiNotificationsNotificationUnreadCountGetRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new NotificationApi();

  try {
    const data = await api.unreadCountApiNotificationsNotificationUnreadCountGet();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

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
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateApiNotificationsNotificationPkPatch

> Notification updateApiNotificationsNotificationPkPatch(pk, body)

Update

### Example

```ts
import {
  Configuration,
  NotificationApi,
} from 'api-client-typescript';
import type { UpdateApiNotificationsNotificationPkPatchRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new NotificationApi();

  const body = {
    // string
    pk: pk_example,
    // any
    body: ...,
  } satisfies UpdateApiNotificationsNotificationPkPatchRequest;

  try {
    const data = await api.updateApiNotificationsNotificationPkPatch(body);
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

[**Notification**](Notification.md)

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

