# Studies

-----

**NOTE: These requests require the *CentrePoint* scope. (see [Scopes](scopes.md))**

## List Studies

Returns a list of studies that are within your organization.

**Request:**

```http
GET /centrepoint/v1/Studies
```

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Description|
|-----|-----------|
|**id**|CentrePoint Study ID|
|**name**|CentrePoint Study Name|
|**organizationName**|CentrePoint Organization Name|
|**createdDateTime**|Creation Date of Study|
|**studyStatus**|The study status.|
|**defaultWearPosition**|The default selected wear position for the study.|
|**wearPositions**|The allowed wear positions selected for the study.|

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
            ]
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
            ]
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
GET /centrepoint/v1/Studies/{studyId}
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
    ]
}
