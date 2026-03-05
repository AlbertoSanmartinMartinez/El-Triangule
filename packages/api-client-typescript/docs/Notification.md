
# Notification


## Properties

Name | Type
------------ | -------------
`createdBy` | string
`createdAt` | Date
`updatedAt` | Date
`uuid` | string
`userUuid` | string
`title` | string
`body` | string
`notificationType` | string
`referenceUuid` | string
`isRead` | boolean

## Example

```typescript
import type { Notification } from 'api-client-typescript'

// TODO: Update the object below with actual values
const example = {
  "createdBy": null,
  "createdAt": null,
  "updatedAt": null,
  "uuid": null,
  "userUuid": null,
  "title": null,
  "body": null,
  "notificationType": null,
  "referenceUuid": null,
  "isRead": null,
} satisfies Notification

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Notification
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


