# Event Markers

**NOTE: These requests require the *Analytics* API scope. (see [Scopes](scopes.md))**

## List Study Event Markers

Returns a list of Event Markers within the requested study.

**Request:**

```http
GET /analytics/v3/Studies/{studyId}/Subjects/{subjectId}/EventMarkers
```

**Query Options**

|Field|Type|Description|
|-----|----|-----------|
|**algorithmSettingId**|String (GUID)|GUID of the Settings Used To Create the Event Markers|
|**fromDate**|String (ISO8601 Date)|Starting Date for the Event Markers Query (Inclusive)|
|**toDate**|String (ISO8601 Date)|Ending Date for the Event Markers Query (Inclusive)|

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|**id**|Number|Event Marker ID|
|**subjectId**|Number|CentrePoint Subject ID (see [Subjects](subjects.md))|
|**activityMonitorSerial**|Number|The Monitor Used to Collect the Event Marker Data|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**algorithmSettingId**|GUID of the Settings Used To Create the Event Markers|
|**timestampUtc**|String (ISO8601 Date)|Date/Time when the Event Marker was created|
|**longPressCount**|Number|The Number of Long Press Events that Occurred|
|**pressCount**|Number|The Number of Press Events that Occurred|
|**releaseCount**|Number|The Number of Release Events that Occurred|

**Response Example:**

```json
{
    "items": [
        {
            "id": 796,
            "studyId": 2196,
            "algorithmSettingId": "c8fee8c1-9fec-ea11-af8c-000d3a102b0e",
            "subjectId": 21669,
            "activityMonitorSerial": "CPW1A00000001",
            "timestampUtc": "2020-05-15T15:07:46+00:00",
            "longPressCount": 0,
            "pressCount": 2,
            "releaseCount": 2
        },
        {
            "id": 7952,
            "studyId": 2196,
            "algorithmSettingId": "1bf9b82f-d3f2-ea11-af8c-000d3a102b0e",
            "subjectId": 21669,
            "activityMonitorSerial": "CPW1A00000001",
            "timestampUtc": "2020-05-15T15:07:47+00:00",
            "longPressCount": 0,
            "pressCount": 2,
            "releaseCount": 2
        },
        {
            "id": 798,
            "studyId": 2196,
            "algorithmSettingId": "c8fee8c1-9fec-ea11-af8c-000d3a102b0e",
            "subjectId": 21669,
            "activityMonitorSerial": "CPW1A00000001",
            "timestampUtc": "2020-05-15T15:07:48+00:00",
            "longPressCount": 0,
            "pressCount": 1,
            "releaseCount": 0
        }
    ],
    "links": {},
    "totalCount": 70,
    "limit": 100,
    "offset": 0
}
```


## List Study Event Marker Settings

Returns a list of Event Marker Settings within the requested study.

**Request:**

```http
GET /analytics/v3/Studies/{studyId}/EventMarkerSettings
```

**Query Options**

|Field|Type|Description|
|-----|----|-----------|
|**ids**|String Array of GUIDs|GUIDs of the Event Marker Settings|

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|**id**|String (GUID)|Event Marker Setting ID|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**name**|String|The Custom Name of the Event Marker Setting|
|**algorithmType**|String|The Algorithm Type for the Setting|

**Response Example:**

```json
{
    "items": [
        {
            "id": "c8fee8c1-9fec-ea11-af8c-000d3a102b0e",
            "studyId": 2196,
            "name": "Event Markers",
            "algorithmType": "Event Markers"
        }
    ],
    "links": {},
    "totalCount": 1,
    "limit": 100,
    "offset": 0
}
```


## Retrieve Event Marker Setting

Returns a single Event Marker Setting by ID within the requested study.

**Request:**

```http
GET /analytics/v3/Studies/{studyId}/EventMarkerSettings/{eventMarkerSettingId}
```

**Response:**

|Field|Type|Description|
|-----|----|-----------|
|**id**|String (GUID)|Event Marker Setting ID|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**name**|String|The Custom Name of the Event Marker Setting|
|**algorithmType**|String|The Algorithm Type for the Setting|

**Response Example:**

```json
{
    "id": "c8fee8c1-9fec-ea11-af8c-000d3a102b0e",
    "studyId": 2196,
    "name": "Event Markers",
    "algorithmType": "Event Markers"
}
```