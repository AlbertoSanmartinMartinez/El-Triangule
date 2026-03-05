# Album


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**uuid** | **UUID** |  | [optional] 
**name** | **str** |  | 
**cover_image_url** | **str** |  | [optional] 
**event_uuid** | **str** |  | [optional] 

## Example

```python
from api-client-python.models.album import Album

# TODO update the JSON string below
json = "{}"
# create an instance of Album from a JSON string
album_instance = Album.from_json(json)
# print the JSON string representation of the object
print(Album.to_json())

# convert the object into a dict
album_dict = album_instance.to_dict()
# create an instance of Album from a dict
album_from_dict = Album.from_dict(album_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


