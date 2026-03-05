# Conversation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**uuid** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**ConversationType**](ConversationType.md) |  | [optional] 
**image_url** | **str** |  | [optional] 

## Example

```python
from api-client-python.models.conversation import Conversation

# TODO update the JSON string below
json = "{}"
# create an instance of Conversation from a JSON string
conversation_instance = Conversation.from_json(json)
# print the JSON string representation of the object
print(Conversation.to_json())

# convert the object into a dict
conversation_dict = conversation_instance.to_dict()
# create an instance of Conversation from a dict
conversation_from_dict = Conversation.from_dict(conversation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


