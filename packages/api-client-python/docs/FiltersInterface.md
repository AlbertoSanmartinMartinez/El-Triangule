# FiltersInterface

Unified filters payload shared by routers, controllers and repositories.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | [**List[SearchParams]**](SearchParams.md) |  | [optional] 
**include_relations** | **List[str]** |  | [optional] 
**pagination** | [**PaginationParams1**](PaginationParams1.md) |  | [optional] 
**order** | [**OrderParams1**](OrderParams1.md) |  | [optional] 

## Example

```python
from api-client-python.models.filters_interface import FiltersInterface

# TODO update the JSON string below
json = "{}"
# create an instance of FiltersInterface from a JSON string
filters_interface_instance = FiltersInterface.from_json(json)
# print the JSON string representation of the object
print(FiltersInterface.to_json())

# convert the object into a dict
filters_interface_dict = filters_interface_instance.to_dict()
# create an instance of FiltersInterface from a dict
filters_interface_from_dict = FiltersInterface.from_dict(filters_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


