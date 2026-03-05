# ListResponsePayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Payment]**](Payment.md) |  | 
**pagination** | [**PaginationParams**](PaginationParams.md) |  | 
**order** | [**OrderParams**](OrderParams.md) |  | 

## Example

```python
from api-client-python.models.list_response_payment import ListResponsePayment

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponsePayment from a JSON string
list_response_payment_instance = ListResponsePayment.from_json(json)
# print the JSON string representation of the object
print(ListResponsePayment.to_json())

# convert the object into a dict
list_response_payment_dict = list_response_payment_instance.to_dict()
# create an instance of ListResponsePayment from a dict
list_response_payment_from_dict = ListResponsePayment.from_dict(list_response_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


