# PaginationParams

Pagination configuration received from the client and returned by the API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 1]
**num_items** | **int** |  | [optional] [default to 50]
**min_page** | **int** |  | [optional] 
**max_page** | **int** |  | [optional] 
**total_items** | **int** |  | [optional] 

## Example

```python
from api-client-python.models.pagination_params import PaginationParams

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationParams from a JSON string
pagination_params_instance = PaginationParams.from_json(json)
# print the JSON string representation of the object
print(PaginationParams.to_json())

# convert the object into a dict
pagination_params_dict = pagination_params_instance.to_dict()
# create an instance of PaginationParams from a dict
pagination_params_from_dict = PaginationParams.from_dict(pagination_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


