# PaymentApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createApiPaymentsPaymentPost**](PaymentApi.md#createapipaymentspaymentpost) | **POST** /api/payments/payment | Create |
| [**deleteApiPaymentsPaymentPkDelete**](PaymentApi.md#deleteapipaymentspaymentpkdelete) | **DELETE** /api/payments/payment/{pk} | Delete |
| [**detailApiPaymentsPaymentPkGet**](PaymentApi.md#detailapipaymentspaymentpkget) | **GET** /api/payments/payment/{pk} | Detail |
| [**listApiPaymentsPaymentGet**](PaymentApi.md#listapipaymentspaymentget) | **GET** /api/payments/payment | List |
| [**refundPaymentApiPaymentsPaymentUuidRefundPost**](PaymentApi.md#refundpaymentapipaymentspaymentuuidrefundpost) | **POST** /api/payments/payment/{uuid}/refund | Refund payment |
| [**updateApiPaymentsPaymentPkPatch**](PaymentApi.md#updateapipaymentspaymentpkpatch) | **PATCH** /api/payments/payment/{pk} | Update |



## createApiPaymentsPaymentPost

> Payment createApiPaymentsPaymentPost(payment)

Create

### Example

```ts
import {
  Configuration,
  PaymentApi,
} from 'api-client-typescript';
import type { CreateApiPaymentsPaymentPostRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new PaymentApi();

  const body = {
    // Payment
    payment: ...,
  } satisfies CreateApiPaymentsPaymentPostRequest;

  try {
    const data = await api.createApiPaymentsPaymentPost(body);
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
| **payment** | [Payment](Payment.md) |  | |

### Return type

[**Payment**](Payment.md)

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


## deleteApiPaymentsPaymentPkDelete

> deleteApiPaymentsPaymentPkDelete(pk)

Delete

### Example

```ts
import {
  Configuration,
  PaymentApi,
} from 'api-client-typescript';
import type { DeleteApiPaymentsPaymentPkDeleteRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new PaymentApi();

  const body = {
    // string
    pk: pk_example,
  } satisfies DeleteApiPaymentsPaymentPkDeleteRequest;

  try {
    const data = await api.deleteApiPaymentsPaymentPkDelete(body);
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


## detailApiPaymentsPaymentPkGet

> Payment detailApiPaymentsPaymentPkGet(pk, includeRelations)

Detail

### Example

```ts
import {
  Configuration,
  PaymentApi,
} from 'api-client-typescript';
import type { DetailApiPaymentsPaymentPkGetRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new PaymentApi();

  const body = {
    // string
    pk: pk_example,
    // Array<string> (optional)
    includeRelations: ...,
  } satisfies DetailApiPaymentsPaymentPkGetRequest;

  try {
    const data = await api.detailApiPaymentsPaymentPkGet(body);
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

[**Payment**](Payment.md)

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


## listApiPaymentsPaymentGet

> ListResponsePayment listApiPaymentsPaymentGet(filters)

List

### Example

```ts
import {
  Configuration,
  PaymentApi,
} from 'api-client-typescript';
import type { ListApiPaymentsPaymentGetRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new PaymentApi();

  const body = {
    // FiltersInterface | FiltersInterface encoded as a deep object (filters[...]) (optional)
    filters: ...,
  } satisfies ListApiPaymentsPaymentGetRequest;

  try {
    const data = await api.listApiPaymentsPaymentGet(body);
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

[**ListResponsePayment**](ListResponsePayment.md)

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


## refundPaymentApiPaymentsPaymentUuidRefundPost

> Payment refundPaymentApiPaymentsPaymentUuidRefundPost(uuid)

Refund payment

### Example

```ts
import {
  Configuration,
  PaymentApi,
} from 'api-client-typescript';
import type { RefundPaymentApiPaymentsPaymentUuidRefundPostRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new PaymentApi();

  const body = {
    // string
    uuid: uuid_example,
  } satisfies RefundPaymentApiPaymentsPaymentUuidRefundPostRequest;

  try {
    const data = await api.refundPaymentApiPaymentsPaymentUuidRefundPost(body);
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

[**Payment**](Payment.md)

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


## updateApiPaymentsPaymentPkPatch

> Payment updateApiPaymentsPaymentPkPatch(pk, body)

Update

### Example

```ts
import {
  Configuration,
  PaymentApi,
} from 'api-client-typescript';
import type { UpdateApiPaymentsPaymentPkPatchRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new PaymentApi();

  const body = {
    // string
    pk: pk_example,
    // any
    body: ...,
  } satisfies UpdateApiPaymentsPaymentPkPatchRequest;

  try {
    const data = await api.updateApiPaymentsPaymentPkPatch(body);
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

[**Payment**](Payment.md)

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

