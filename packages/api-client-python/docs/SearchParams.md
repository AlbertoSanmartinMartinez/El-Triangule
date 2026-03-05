# SearchParams

Normalized search condition shared across repositories.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** |  | 
**operator** | **str** | Allowed operators for search filters.  Declared as an Enum so that: - Pydantic validates the operator value automatically. - FastAPI/OpenAPI exposes it as an enum in the schema, so code generators   create a strongly-typed client. | 
**value** | **object** |  | [optional] 

## Example

```python
from api-client-python.models.search_params import SearchParams

# TODO update the JSON string below
json = "{}"
# create an instance of SearchParams from a JSON string
search_params_instance = SearchParams.from_json(json)
# print the JSON string representation of the object
print(SearchParams.to_json())

# convert the object into a dict
search_params_dict = search_params_instance.to_dict()
# create an instance of SearchParams from a dict
search_params_from_dict = SearchParams.from_dict(search_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


