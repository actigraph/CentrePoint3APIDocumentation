# Pagination

All list type responses from the CentrePoint API will be paginated.

## Pagination Request Parameters

|Parameter|Description|
|---------|-----------|
|**limit**|The maximum number (betweeen 1 and 100) of items to return|
|**offset**|The zero based starting point of the request.|

**Pagination Request Example:**

The request below would return the third and fourth items of a collection.

```http
POST centrepoint/v1/Studies?offset=2&limit=2
```

**Pagination Response Example:**

```json
{
    "items": [
        {
            "id": 239,
            "name": "Example Study",
            "organizationName": "Example Organization",
            "createdDateTime": "2019-06-26T13:34:02.07Z",
            "studyStatus": "Active",
            "defaultWearPosition": "Left Non-Dominant Wrist",
            "wearPositions": [
                "Left Non-Dominant Wrist"
            ]
        },
        {
            "id": 240,
            "name": "Example Study 2",
            "organizationName": "Example Organization",
            "createdDateTime": "2019-06-26T13:34:02.07Z",
            "studyStatus": "Active",
            "defaultWearPosition": "Left Non-Dominant Wrist",
            "wearPositions": [
                "Left Non-Dominant Wrist"
            ]
        }
    ],
    "links": {
        "next": "https://ag-api-management-service.azure-api.net/Studies?offset=4&limit=2",
        "prev": "https://ag-api-management-service.azure-api.net/Studies?offset=0&limit=2"
    },
    "totalCount": 6,
    "limit": 2,
    "offset": 2
}
```

## Pagination Response Fields

|Field|Description|
|-----|-----------|
|**items**|An array of objects for the requested resource list. The schema of the object is specific to the resource type being requested.|
|**links**|Contains navigation links to next and previous pages if applicable.|
|**totalCount**|The total count of items available. This will be greater than *limit* if there is more than one page available.|
|**limit**|The limit of items returned per request.|
|**offset**|The zero based offset where items up to the limit are returned.|
