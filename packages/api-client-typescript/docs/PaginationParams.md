
# PaginationParams

Pagination configuration received from the client and returned by the API.

## Properties

Name | Type
------------ | -------------
`page` | number
`numItems` | number
`minPage` | number
`maxPage` | number
`totalItems` | number

## Example

```typescript
import type { PaginationParams } from 'api-client-typescript'

// TODO: Update the object below with actual values
const example = {
  "page": null,
  "numItems": null,
  "minPage": null,
  "maxPage": null,
  "totalItems": null,
} satisfies PaginationParams

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as PaginationParams
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


