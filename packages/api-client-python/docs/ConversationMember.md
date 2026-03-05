# ConversationMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**uuid** | **UUID** |  | [optional] 
**conversation_uuid** | **str** |  | 
**user_uuid** | **str** |  | 
**role** | [**MemberRole**](MemberRole.md) |  | [optional] 

## Example

```python
from api-client-python.models.conversation_member import ConversationMember

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMember from a JSON string
conversation_member_instance = ConversationMember.from_json(json)
# print the JSON string representation of the object
print(ConversationMember.to_json())

# convert the object into a dict
conversation_member_dict = conversation_member_instance.to_dict()
# create an instance of ConversationMember from a dict
conversation_member_from_dict = ConversationMember.from_dict(conversation_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


