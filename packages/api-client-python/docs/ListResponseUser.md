# ListResponseUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[User]**](User.md) |  | 
**pagination** | [**PaginationParams**](PaginationParams.md) |  | 
**order** | [**OrderParams**](OrderParams.md) |  | 

## Example

```python
from api-client-python.models.list_response_user import ListResponseUser

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseUser from a JSON string
list_response_user_instance = ListResponseUser.from_json(json)
# print the JSON string representation of the object
print(ListResponseUser.to_json())

# convert the object into a dict
list_response_user_dict = list_response_user_instance.to_dict()
# create an instance of ListResponseUser from a dict
list_response_user_from_dict = ListResponseUser.from_dict(list_response_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


