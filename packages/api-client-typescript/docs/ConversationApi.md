# ConversationApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addMemberApiMessagesConversationUuidMemberPost**](ConversationApi.md#addmemberapimessagesconversationuuidmemberpost) | **POST** /api/messages/conversation/{uuid}/member | Add member to conversation |
| [**createApiMessagesConversationPost**](ConversationApi.md#createapimessagesconversationpost) | **POST** /api/messages/conversation | Create |
| [**deleteApiMessagesConversationPkDelete**](ConversationApi.md#deleteapimessagesconversationpkdelete) | **DELETE** /api/messages/conversation/{pk} | Delete |
| [**detailApiMessagesConversationPkGet**](ConversationApi.md#detailapimessagesconversationpkget) | **GET** /api/messages/conversation/{pk} | Detail |
| [**listApiMessagesConversationGet**](ConversationApi.md#listapimessagesconversationget) | **GET** /api/messages/conversation | List |
| [**removeMemberApiMessagesConversationUuidMemberUserUuidDelete**](ConversationApi.md#removememberapimessagesconversationuuidmemberuseruuiddelete) | **DELETE** /api/messages/conversation/{uuid}/member/{user_uuid} | Remove member from conversation |
| [**updateApiMessagesConversationPkPatch**](ConversationApi.md#updateapimessagesconversationpkpatch) | **PATCH** /api/messages/conversation/{pk} | Update |



## addMemberApiMessagesConversationUuidMemberPost

> ConversationMember addMemberApiMessagesConversationUuidMemberPost(uuid, addMemberRequest)

Add member to conversation

### Example

```ts
import {
  Configuration,
  ConversationApi,
} from 'api-client-typescript';
import type { AddMemberApiMessagesConversationUuidMemberPostRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new ConversationApi();

  const body = {
    // string
    uuid: uuid_example,
    // AddMemberRequest
    addMemberRequest: ...,
  } satisfies AddMemberApiMessagesConversationUuidMemberPostRequest;

  try {
    const data = await api.addMemberApiMessagesConversationUuidMemberPost(body);
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
| **addMemberRequest** | [AddMemberRequest](AddMemberRequest.md) |  | |

### Return type

[**ConversationMember**](ConversationMember.md)

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


## createApiMessagesConversationPost

> Conversation createApiMessagesConversationPost(conversation)

Create

### Example

```ts
import {
  Configuration,
  ConversationApi,
} from 'api-client-typescript';
import type { CreateApiMessagesConversationPostRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new ConversationApi();

  const body = {
    // Conversation
    conversation: ...,
  } satisfies CreateApiMessagesConversationPostRequest;

  try {
    const data = await api.createApiMessagesConversationPost(body);
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
| **conversation** | [Conversation](Conversation.md) |  | |

### Return type

[**Conversation**](Conversation.md)

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


## deleteApiMessagesConversationPkDelete

> deleteApiMessagesConversationPkDelete(pk)

Delete

### Example

```ts
import {
  Configuration,
  ConversationApi,
} from 'api-client-typescript';
import type { DeleteApiMessagesConversationPkDeleteRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new ConversationApi();

  const body = {
    // string
    pk: pk_example,
  } satisfies DeleteApiMessagesConversationPkDeleteRequest;

  try {
    const data = await api.deleteApiMessagesConversationPkDelete(body);
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


## detailApiMessagesConversationPkGet

> Conversation detailApiMessagesConversationPkGet(pk, includeRelations)

Detail

### Example

```ts
import {
  Configuration,
  ConversationApi,
} from 'api-client-typescript';
import type { DetailApiMessagesConversationPkGetRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new ConversationApi();

  const body = {
    // string
    pk: pk_example,
    // Array<string> (optional)
    includeRelations: ...,
  } satisfies DetailApiMessagesConversationPkGetRequest;

  try {
    const data = await api.detailApiMessagesConversationPkGet(body);
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

[**Conversation**](Conversation.md)

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


## listApiMessagesConversationGet

> ListResponseConversation listApiMessagesConversationGet(filters)

List

### Example

```ts
import {
  Configuration,
  ConversationApi,
} from 'api-client-typescript';
import type { ListApiMessagesConversationGetRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new ConversationApi();

  const body = {
    // FiltersInterface | FiltersInterface encoded as a deep object (filters[...]) (optional)
    filters: ...,
  } satisfies ListApiMessagesConversationGetRequest;

  try {
    const data = await api.listApiMessagesConversationGet(body);
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

[**ListResponseConversation**](ListResponseConversation.md)

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


## removeMemberApiMessagesConversationUuidMemberUserUuidDelete

> removeMemberApiMessagesConversationUuidMemberUserUuidDelete(uuid, userUuid)

Remove member from conversation

### Example

```ts
import {
  Configuration,
  ConversationApi,
} from 'api-client-typescript';
import type { RemoveMemberApiMessagesConversationUuidMemberUserUuidDeleteRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new ConversationApi();

  const body = {
    // string
    uuid: uuid_example,
    // string
    userUuid: userUuid_example,
  } satisfies RemoveMemberApiMessagesConversationUuidMemberUserUuidDeleteRequest;

  try {
    const data = await api.removeMemberApiMessagesConversationUuidMemberUserUuidDelete(body);
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
| **userUuid** | `string` |  | [Defaults to `undefined`] |

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


## updateApiMessagesConversationPkPatch

> Conversation updateApiMessagesConversationPkPatch(pk, body)

Update

### Example

```ts
import {
  Configuration,
  ConversationApi,
} from 'api-client-typescript';
import type { UpdateApiMessagesConversationPkPatchRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new ConversationApi();

  const body = {
    // string
    pk: pk_example,
    // any
    body: ...,
  } satisfies UpdateApiMessagesConversationPkPatchRequest;

  try {
    const data = await api.updateApiMessagesConversationPkPatch(body);
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

[**Conversation**](Conversation.md)

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

