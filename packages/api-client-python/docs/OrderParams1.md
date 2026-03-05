# OrderParams1

Ordering configuration for list endpoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** |  | [optional] [default to 'uuid']
**direction** | **str** | Allowed ordering directions. | [optional] 

## Example

```python
from api-client-python.models.order_params1 import OrderParams1

# TODO update the JSON string below
json = "{}"
# create an instance of OrderParams1 from a JSON string
order_params1_instance = OrderParams1.from_json(json)
# print the JSON string representation of the object
print(OrderParams1.to_json())

# convert the object into a dict
order_params1_dict = order_params1_instance.to_dict()
# create an instance of OrderParams1 from a dict
order_params1_from_dict = OrderParams1.from_dict(order_params1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


