# Studies

**NOTE: These requests require the *CentrePoint* API scope. (see [Scopes](scopes.md))**

## List Studies

Returns a list of studies that are within your organization.

**Request:**

```http
GET /centrepoint/v3/Studies
```

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|**id**|Number|CentrePoint Study ID|
|**name**|String|CentrePoint Study Name|
|**organizationName**|String|CentrePoint Organization Name|
|**createdDateTime**|String (ISO8601 Date)|Creation Date of Study|
|**studyStatus**|String|The study status.|
|**defaultWearPosition**|String|The default wear position for the study.|
|**wearPositions**|Array(String)|The wear positions allowed by the study.|
|**monitorDataCollectionMode**|String|Indicates if monitors are collection Raw data, Epoch data, or both for the study.|

```json
{
    "items": [
        {
            "id": 1,
            "name": "Example Study",
            "organizationName": "Demo Organization",
            "createdDateTime": "2019-06-03T20:38:44.03Z",
            "studyStatus": "Active",
            "defaultWearPosition": "Left Non-Dominant Wrist",
            "wearPositions": [
                "Left Non-Dominant Wrist"
            ],
            "monitorDataCollectionMode": "Raw Only"
        },
        {
            "id": 2,
            "name": "Example Study 2",
            "organizationName": "Demo Organization",
            "createdDateTime": "2019-06-26T13:32:14.34Z",
            "studyStatus": "Active",
            "defaultWearPosition": "Left Non-Dominant Wrist",
            "wearPositions": [
                "Left Non-Dominant Wrist"
            ],
            "monitorDataCollectionMode": "Epoch+Raw"
        }
    ],
    "links": {},
    "totalCount": 2,
    "limit": 100,
    "offset": 0
}
```

## Study Details

Returns detailed information about the requested study.

**Request:**

```http
GET /centrepoint/v3/Studies/{studyId}
```

**Response:**

```json
{
    "id": 1,
    "name": "Example Study",
    "organizationName": "Demo Organization",
    "createdDateTime": "2019-06-03T20:38:44.03Z",
    "studyStatus": "Active",
    "defaultWearPosition": "Left Non-Dominant Wrist",
    "wearPositions": [
        "Left Non-Dominant Wrist"
    ],
    "monitorDataCollectionMode": "Raw Only"
}
