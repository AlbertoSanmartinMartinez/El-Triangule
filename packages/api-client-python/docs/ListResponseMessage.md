# ListResponseMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Message]**](Message.md) |  | 
**pagination** | [**PaginationParams**](PaginationParams.md) |  | 
**order** | [**OrderParams**](OrderParams.md) |  | 

## Example

```python
from api-client-python.models.list_response_message import ListResponseMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseMessage from a JSON string
list_response_message_instance = ListResponseMessage.from_json(json)
# print the JSON string representation of the object
print(ListResponseMessage.to_json())

# convert the object into a dict
list_response_message_dict = list_response_message_instance.to_dict()
# create an instance of ListResponseMessage from a dict
list_response_message_from_dict = ListResponseMessage.from_dict(list_response_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


