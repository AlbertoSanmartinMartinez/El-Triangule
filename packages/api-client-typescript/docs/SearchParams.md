
# SearchParams

Normalized search condition shared across repositories.

## Properties

Name | Type
------------ | -------------
`attribute` | string
`operator` | string
`value` | any

## Example

```typescript
import type { SearchParams } from 'api-client-typescript'

// TODO: Update the object below with actual values
const example = {
  "attribute": null,
  "operator": null,
  "value": null,
} satisfies SearchParams

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SearchParams
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


