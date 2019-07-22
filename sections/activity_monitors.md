# Activity Monitors

**NOTE: These requests require the *CentrePoint* API scope. (see [Scopes](scopes.md))**

## List Study Activity Monitors

Returns a list of activity monitors within a study.

**Request:**

```http
GET /centrepoint/v3/Studies/{studyId}/ActivityMonitors
```

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|**serial**|String|Activity monitor serial number|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**assignmentId**|Number|Assignment ID if the activity monitor is assigned to a Subject (see [Assignments](assignments.md))|
|**assignmentStatus**|String|Indicates if monitor is assigned or not|
|**dataHubSerialNumber**|String|The CentrePoint DataHub (CDH) device serial number that was packaged/distributed with the activity monitor (if applicable)|

```json
{
    "items": [
        {
            "serial": "TAS1Z12345678",
            "studyId": 242,
            "assignmentId": 23440,
            "assignmentStatus": "Assigned",
            "dataHubSerialNumber": "CDM1A06170010"
        },
        {
            "serial": "TAS1Z12345679",
            "studyId": 242,
            "assignmentId": 23441,
            "assignmentStatus": "Assigned",
            "dataHubSerialNumber": "CDM1A06170011"
        }
    ],
    "links": {},
    "totalCount": 2,
    "limit": 100,
    "offset": 0
}
```

## Get Activity Monitor Details by Serial Number

Returns a list of activity monitors within a study.

**Request:**

```http
GET /centrepoint/v3/Studies/{studyId}/ActivityMonitors/{activityMonitorSerial}
```

**Response:**

```json
{
    "serial": "TAS1Z12345678",
    "studyId": 242,
    "assignmentId": 23440,
    "assignmentStatus": "Assigned",
    "dataHubSerialNumber": "CDM1A06170010"
}
```
