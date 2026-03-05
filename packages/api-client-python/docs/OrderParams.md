# OrderParams

Ordering configuration for list endpoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** |  | [optional] [default to 'uuid']
**direction** | [**OrderDirection**](OrderDirection.md) |  | [optional] 

## Example

```python
from api-client-python.models.order_params import OrderParams

# TODO update the JSON string below
json = "{}"
# create an instance of OrderParams from a JSON string
order_params_instance = OrderParams.from_json(json)
# print the JSON string representation of the object
print(OrderParams.to_json())

# convert the object into a dict
order_params_dict = order_params_instance.to_dict()
# create an instance of OrderParams from a dict
order_params_from_dict = OrderParams.from_dict(order_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


