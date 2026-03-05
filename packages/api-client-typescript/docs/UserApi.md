# UserApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createApiAuthUserPost**](UserApi.md#createapiauthuserpost) | **POST** /api/auth/user | Create |
| [**deleteApiAuthUserPkDelete**](UserApi.md#deleteapiauthuserpkdelete) | **DELETE** /api/auth/user/{pk} | Delete |
| [**detailApiAuthUserPkGet**](UserApi.md#detailapiauthuserpkget) | **GET** /api/auth/user/{pk} | Detail |
| [**listApiAuthUserGet**](UserApi.md#listapiauthuserget) | **GET** /api/auth/user | List |
| [**loginApiAuthUserLoginPost**](UserApi.md#loginapiauthuserloginpost) | **POST** /api/auth/user/login | User login |
| [**refreshApiAuthUserRefreshPost**](UserApi.md#refreshapiauthuserrefreshpost) | **POST** /api/auth/user/refresh | Refresh token |
| [**registerApiAuthUserRegisterPost**](UserApi.md#registerapiauthuserregisterpost) | **POST** /api/auth/user/register | User register |
| [**updateApiAuthUserPkPatch**](UserApi.md#updateapiauthuserpkpatch) | **PATCH** /api/auth/user/{pk} | Update |



## createApiAuthUserPost

> User createApiAuthUserPost(user)

Create

### Example

```ts
import {
  Configuration,
  UserApi,
} from 'api-client-typescript';
import type { CreateApiAuthUserPostRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new UserApi();

  const body = {
    // User
    user: ...,
  } satisfies CreateApiAuthUserPostRequest;

  try {
    const data = await api.createApiAuthUserPost(body);
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
| **user** | [User](User.md) |  | |

### Return type

[**User**](User.md)

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


## deleteApiAuthUserPkDelete

> deleteApiAuthUserPkDelete(pk)

Delete

### Example

```ts
import {
  Configuration,
  UserApi,
} from 'api-client-typescript';
import type { DeleteApiAuthUserPkDeleteRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new UserApi();

  const body = {
    // string
    pk: pk_example,
  } satisfies DeleteApiAuthUserPkDeleteRequest;

  try {
    const data = await api.deleteApiAuthUserPkDelete(body);
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


## detailApiAuthUserPkGet

> User detailApiAuthUserPkGet(pk, includeRelations)

Detail

### Example

```ts
import {
  Configuration,
  UserApi,
} from 'api-client-typescript';
import type { DetailApiAuthUserPkGetRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new UserApi();

  const body = {
    // string
    pk: pk_example,
    // Array<string> (optional)
    includeRelations: ...,
  } satisfies DetailApiAuthUserPkGetRequest;

  try {
    const data = await api.detailApiAuthUserPkGet(body);
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

[**User**](User.md)

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


## listApiAuthUserGet

> ListResponseUser listApiAuthUserGet(filters)

List

### Example

```ts
import {
  Configuration,
  UserApi,
} from 'api-client-typescript';
import type { ListApiAuthUserGetRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new UserApi();

  const body = {
    // FiltersInterface | FiltersInterface encoded as a deep object (filters[...]) (optional)
    filters: ...,
  } satisfies ListApiAuthUserGetRequest;

  try {
    const data = await api.listApiAuthUserGet(body);
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

[**ListResponseUser**](ListResponseUser.md)

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


## loginApiAuthUserLoginPost

> TokenResponse loginApiAuthUserLoginPost(loginRequest)

User login

### Example

```ts
import {
  Configuration,
  UserApi,
} from 'api-client-typescript';
import type { LoginApiAuthUserLoginPostRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new UserApi();

  const body = {
    // LoginRequest
    loginRequest: ...,
  } satisfies LoginApiAuthUserLoginPostRequest;

  try {
    const data = await api.loginApiAuthUserLoginPost(body);
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
| **loginRequest** | [LoginRequest](LoginRequest.md) |  | |

### Return type

[**TokenResponse**](TokenResponse.md)

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


## refreshApiAuthUserRefreshPost

> TokenResponse refreshApiAuthUserRefreshPost(refreshRequest)

Refresh token

### Example

```ts
import {
  Configuration,
  UserApi,
} from 'api-client-typescript';
import type { RefreshApiAuthUserRefreshPostRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new UserApi();

  const body = {
    // RefreshRequest
    refreshRequest: ...,
  } satisfies RefreshApiAuthUserRefreshPostRequest;

  try {
    const data = await api.refreshApiAuthUserRefreshPost(body);
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
| **refreshRequest** | [RefreshRequest](RefreshRequest.md) |  | |

### Return type

[**TokenResponse**](TokenResponse.md)

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


## registerApiAuthUserRegisterPost

> TokenResponse registerApiAuthUserRegisterPost(registerRequest)

User register

### Example

```ts
import {
  Configuration,
  UserApi,
} from 'api-client-typescript';
import type { RegisterApiAuthUserRegisterPostRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new UserApi();

  const body = {
    // RegisterRequest
    registerRequest: ...,
  } satisfies RegisterApiAuthUserRegisterPostRequest;

  try {
    const data = await api.registerApiAuthUserRegisterPost(body);
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
| **registerRequest** | [RegisterRequest](RegisterRequest.md) |  | |

### Return type

[**TokenResponse**](TokenResponse.md)

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


## updateApiAuthUserPkPatch

> User updateApiAuthUserPkPatch(pk, body)

Update

### Example

```ts
import {
  Configuration,
  UserApi,
} from 'api-client-typescript';
import type { UpdateApiAuthUserPkPatchRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new UserApi();

  const body = {
    // string
    pk: pk_example,
    // any
    body: ...,
  } satisfies UpdateApiAuthUserPkPatchRequest;

  try {
    const data = await api.updateApiAuthUserPkPatch(body);
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

[**User**](User.md)

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

