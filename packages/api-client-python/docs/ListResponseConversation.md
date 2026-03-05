# ListResponseConversation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Conversation]**](Conversation.md) |  | 
**pagination** | [**PaginationParams**](PaginationParams.md) |  | 
**order** | [**OrderParams**](OrderParams.md) |  | 

## Example

```python
from api-client-python.models.list_response_conversation import ListResponseConversation

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseConversation from a JSON string
list_response_conversation_instance = ListResponseConversation.from_json(json)
# print the JSON string representation of the object
print(ListResponseConversation.to_json())

# convert the object into a dict
list_response_conversation_dict = list_response_conversation_instance.to_dict()
# create an instance of ListResponseConversation from a dict
list_response_conversation_from_dict = ListResponseConversation.from_dict(list_response_conversation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


