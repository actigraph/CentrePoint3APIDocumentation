# Study Milestones

**NOTE: These requests require the *CentrePoint* API scope. (see [Scopes](scopes.md))**

## List Study Milestones

Returns a list of all study milestones within the requested study.

**Request:**

```http
GET /centrepoint/v3/Studies/{studyId}/Milestones
```

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|id|Number|Subejct Milestone ID|
|studyId|Number|CentrePoint Study ID|
|name|String|Milestone Name|
|order|Number|Milestone Order|

```json
{
    "items": [
        {
            "id": 538,
            "studyId": 240,
            "name": "Milestone 1",
            "order": 1
        },
        {
            "id": 539,
            "studyId": 240,
            "name": "Milestone 2",
            "order": 2
        },
        {
            "id": 540,
            "studyId": 240,
            "name": "Milestone 3",
            "order": 3
        }
    ],
    "links": {},
    "totalCount": 3,
    "limit": 100,
    "offset": 0
}
```
