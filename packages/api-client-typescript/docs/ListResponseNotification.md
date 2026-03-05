
# ListResponseNotification


## Properties

Name | Type
------------ | -------------
`items` | [Array&lt;Notification&gt;](Notification.md)
`pagination` | [PaginationParams](PaginationParams.md)
`order` | [OrderParams](OrderParams.md)

## Example

```typescript
import type { ListResponseNotification } from 'api-client-typescript'

// TODO: Update the object below with actual values
const example = {
  "items": null,
  "pagination": null,
  "order": null,
} satisfies ListResponseNotification

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListResponseNotification
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


