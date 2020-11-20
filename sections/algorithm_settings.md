# Algorithm Settings

**NOTE: These requests require the *Analytics* API scope. (see [Scopes](scopes.md))**

## List Study Algorithm Settings

Returns a list of Algorithm Settings that are associated with a given study.

**Request:**

```http
GET /analytics/v3/Studies/{studyId}/AlgorithmSettings
```

**Query Options**

|Field|Type|Description|
|-----|----|-----------|
|**algorithmType**|String|Name of the Algorithm Type of the Settings|

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|**id**|String (GUID)|Algorithm Setting ID|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**name**|String|The Custom Name of the Algorithm Setting|
|**algorithmType**|String|The Algorithm Type for the Setting|

**Response Example:**

```json
{
    "items": [
        {
            "id": "e9d14cd0-c903-eb11-96f5-000d3a102a21",
            "studyId": 2196,
            "name": "Epoch Summary 60 sec",
            "algorithmType": "Epoch Summary"
        },
        {
            "id": "ead14cd0-c903-eb11-96f5-000d3a102a21",
            "studyId": 2196,
            "name": "Dustin Tracy Sleep Periods - Adult Wrist-Worn",
            "algorithmType": "Dustin Tracy Sleep Periods"
        },
        {
            "id": "ebd14cd0-c903-eb11-96f5-000d3a102a21",
            "studyId": 2196,
            "name": "Choi Wear Periods",
            "algorithmType": "Choi Wear Periods"
        },
        {
            "id": "ecd14cd0-c903-eb11-96f5-000d3a102a21",
            "studyId": 2196,
            "name": "Uwf Steps",
            "algorithmType": "UWF Steps"
        },
        {
            "id": "edd14cd0-c903-eb11-96f5-000d3a102a21",
            "studyId": 2196,
            "name": "Crouter Child Cutpoints",
            "algorithmType": "Crouter Child Cutpoints"
        },
        {
            "id": "eed14cd0-c903-eb11-96f5-000d3a102a21",
            "studyId": 2196,
            "name": "Staudenmayer Cutpoints",
            "algorithmType": "Staudenmayer Cutpoints"
        }
    ],
    "links": {},
    "totalCount": 6,
    "limit": 100,
    "offset": 0
}
```
