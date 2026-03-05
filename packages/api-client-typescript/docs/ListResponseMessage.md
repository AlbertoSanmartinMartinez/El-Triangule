
# ListResponseMessage


## Properties

Name | Type
------------ | -------------
`items` | [Array&lt;Message&gt;](Message.md)
`pagination` | [PaginationParams](PaginationParams.md)
`order` | [OrderParams](OrderParams.md)

## Example

```typescript
import type { ListResponseMessage } from 'api-client-typescript'

// TODO: Update the object below with actual values
const example = {
  "items": null,
  "pagination": null,
  "order": null,
} satisfies ListResponseMessage

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListResponseMessage
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


