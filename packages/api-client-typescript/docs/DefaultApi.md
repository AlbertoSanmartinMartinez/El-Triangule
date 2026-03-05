# DefaultApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**healthCheckApiHealthGet**](DefaultApi.md#healthcheckapihealthget) | **GET** /api/health | Health Check |



## healthCheckApiHealthGet

> any healthCheckApiHealthGet()

Health Check

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from 'api-client-typescript';
import type { HealthCheckApiHealthGetRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.healthCheckApiHealthGet();
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

