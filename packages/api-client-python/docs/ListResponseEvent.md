# ListResponseEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Event]**](Event.md) |  | 
**pagination** | [**PaginationParams**](PaginationParams.md) |  | 
**order** | [**OrderParams**](OrderParams.md) |  | 

## Example

```python
from api-client-python.models.list_response_event import ListResponseEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseEvent from a JSON string
list_response_event_instance = ListResponseEvent.from_json(json)
# print the JSON string representation of the object
print(ListResponseEvent.to_json())

# convert the object into a dict
list_response_event_dict = list_response_event_instance.to_dict()
# create an instance of ListResponseEvent from a dict
list_response_event_from_dict = ListResponseEvent.from_dict(list_response_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


