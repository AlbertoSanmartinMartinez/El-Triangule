
# ListResponseConversation


## Properties

Name | Type
------------ | -------------
`items` | [Array&lt;Conversation&gt;](Conversation.md)
`pagination` | [PaginationParams](PaginationParams.md)
`order` | [OrderParams](OrderParams.md)

## Example

```typescript
import type { ListResponseConversation } from 'api-client-typescript'

// TODO: Update the object below with actual values
const example = {
  "items": null,
  "pagination": null,
  "order": null,
} satisfies ListResponseConversation

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListResponseConversation
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


