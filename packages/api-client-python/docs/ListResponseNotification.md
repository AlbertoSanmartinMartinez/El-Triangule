# ListResponseNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Notification]**](Notification.md) |  | 
**pagination** | [**PaginationParams**](PaginationParams.md) |  | 
**order** | [**OrderParams**](OrderParams.md) |  | 

## Example

```python
from api-client-python.models.list_response_notification import ListResponseNotification

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseNotification from a JSON string
list_response_notification_instance = ListResponseNotification.from_json(json)
# print the JSON string representation of the object
print(ListResponseNotification.to_json())

# convert the object into a dict
list_response_notification_dict = list_response_notification_instance.to_dict()
# create an instance of ListResponseNotification from a dict
list_response_notification_from_dict = ListResponseNotification.from_dict(list_response_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


