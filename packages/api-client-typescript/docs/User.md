
# User


## Properties

Name | Type
------------ | -------------
`uuid` | string
`email` | string
`password` | string
`isActive` | boolean
`role` | [Role](Role.md)

## Example

```typescript
import type { User } from 'api-client-typescript'

// TODO: Update the object below with actual values
const example = {
  "uuid": null,
  "email": null,
  "password": null,
  "isActive": null,
  "role": null,
} satisfies User

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as User
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


