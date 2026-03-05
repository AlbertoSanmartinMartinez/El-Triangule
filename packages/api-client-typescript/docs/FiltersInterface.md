
# FiltersInterface

Unified filters payload shared by routers, controllers and repositories.

## Properties

Name | Type
------------ | -------------
`search` | [Array&lt;SearchParams&gt;](SearchParams.md)
`includeRelations` | Array&lt;string&gt;
`pagination` | [PaginationParams1](PaginationParams1.md)
`order` | [OrderParams1](OrderParams1.md)

## Example

```typescript
import type { FiltersInterface } from 'api-client-typescript'

// TODO: Update the object below with actual values
const example = {
  "search": null,
  "includeRelations": null,
  "pagination": null,
  "order": null,
} satisfies FiltersInterface

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FiltersInterface
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


