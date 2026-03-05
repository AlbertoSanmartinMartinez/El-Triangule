# Payment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**uuid** | **UUID** |  | [optional] 
**user_uuid** | **str** |  | 
**event_uuid** | **str** |  | 
**amount** | **float** |  | 
**currency** | **str** |  | [optional] [default to 'EUR']
**payment_method** | **str** |  | 
**status** | **str** |  | [optional] [default to 'pending']
**transaction_id** | **str** |  | [optional] 

## Example

```python
from api-client-python.models.payment import Payment

# TODO update the JSON string below
json = "{}"
# create an instance of Payment from a JSON string
payment_instance = Payment.from_json(json)
# print the JSON string representation of the object
print(Payment.to_json())

# convert the object into a dict
payment_dict = payment_instance.to_dict()
# create an instance of Payment from a dict
payment_from_dict = Payment.from_dict(payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


