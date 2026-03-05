# ListResponseAlbum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Album]**](Album.md) |  | 
**pagination** | [**PaginationParams**](PaginationParams.md) |  | 
**order** | [**OrderParams**](OrderParams.md) |  | 

## Example

```python
from api-client-python.models.list_response_album import ListResponseAlbum

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseAlbum from a JSON string
list_response_album_instance = ListResponseAlbum.from_json(json)
# print the JSON string representation of the object
print(ListResponseAlbum.to_json())

# convert the object into a dict
list_response_album_dict = list_response_album_instance.to_dict()
# create an instance of ListResponseAlbum from a dict
list_response_album_from_dict = ListResponseAlbum.from_dict(list_response_album_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


