
# Image


## Properties

Name | Type
------------ | -------------
`createdBy` | string
`createdAt` | Date
`updatedAt` | Date
`uuid` | string
`albumUuid` | string
`fileUrl` | string
`thumbnailUrl` | string
`mediaType` | string

## Example

```typescript
import type { Image } from 'api-client-typescript'

// TODO: Update the object below with actual values
const example = {
  "createdBy": null,
  "createdAt": null,
  "updatedAt": null,
  "uuid": null,
  "albumUuid": null,
  "fileUrl": null,
  "thumbnailUrl": null,
  "mediaType": null,
} satisfies Image

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Image
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


