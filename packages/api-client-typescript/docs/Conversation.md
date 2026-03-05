
# Conversation


## Properties

Name | Type
------------ | -------------
`createdBy` | string
`createdAt` | Date
`updatedAt` | Date
`uuid` | string
`name` | string
`type` | [ConversationType](ConversationType.md)
`imageUrl` | string

## Example

```typescript
import type { Conversation } from 'api-client-typescript'

// TODO: Update the object below with actual values
const example = {
  "createdBy": null,
  "createdAt": null,
  "updatedAt": null,
  "uuid": null,
  "name": null,
  "type": null,
  "imageUrl": null,
} satisfies Conversation

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Conversation
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


