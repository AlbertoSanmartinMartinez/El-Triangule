# ListResponseImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Image]**](Image.md) |  | 
**pagination** | [**PaginationParams**](PaginationParams.md) |  | 
**order** | [**OrderParams**](OrderParams.md) |  | 

## Example

```python
from api-client-python.models.list_response_image import ListResponseImage

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseImage from a JSON string
list_response_image_instance = ListResponseImage.from_json(json)
# print the JSON string representation of the object
print(ListResponseImage.to_json())

# convert the object into a dict
list_response_image_dict = list_response_image_instance.to_dict()
# create an instance of ListResponseImage from a dict
list_response_image_from_dict = ListResponseImage.from_dict(list_response_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


