# Assignments

**NOTE: These requests require the *CentrePoint* API scope. (see [Scopes](scopes.md))**

See [Subject Activity Monitor Assignment Workflow](assignment_workflow.md) for details on the assignment workflow process.

## List Study Subject Device Assignments

Returns a list of all study subject device assignments within the requested study.

**Request:**

```http
GET /centrepoint/v3/Studies/{studyId}/Assignments
```

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|**id**|Number|Assignment ID|
|**activityMonitorSerial**|String|Activity Monitor Serial Number (see [Activity Monitors](activity_monitors.md))|
|**subjectId**|Number|CentrePoint Subject ID (see [Subjects](subjects.md))|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**createdDate**|String (ISO8601 Date)|Date of assignment creation|
|**collectionStartedDate**|String (ISO8601 Date)|Date/Time of activity monitor collection start|
|**collectionStoppedDate**|String (ISO8601 Date)|Date/Time of activity monitor collection end|
|**endedDate**|String (ISO8601 Date)|Date/Time of assignment ended|
|**scheduledCollectionStopDate**|String (ISO8601 Date)|Date/Time of scheduled collection stop date (see [Subject Activity Monitor Assignment Workflow](assignment_workflow.md))|
|**status**|String|Status of assignment|

**Response Example:**

```json
{
    "items": [
        {
            "id": 23407,
            "activityMonitorSerial": "TAS1Z12345678",
            "subjectId": 17911,
            "studyId": 242,
            "createdDate": "2019-07-01T13:31:52.113Z",
            "collectionStartedDate": "2019-07-01T13:32:42.613Z",
            "collectionStoppedDate": "2019-07-01T16:03:14.73Z",
            "endedDate": "2019-07-01T16:03:47.827Z",
            "status": "Ended"
        },
        {
            "id": 23408,
            "activityMonitorSerial": "TAS1Z12345678",
            "subjectId": 17912,
            "studyId": 242,
            "createdDate": "2019-07-01T16:47:03.423Z",
            "collectionStartedDate": "2019-07-01T16:47:46.74Z",
            "collectionStoppedDate": "2019-07-01T16:49:19.603Z",
            "endedDate": "2019-07-01T16:50:15.007Z",
            "status": "Ended"
        }
    ],
    "links": {},
    "totalCount": 2,
    "limit": 100,
    "offset": 0
}
```

## Get Study Subject Device Assignment Details By ID

Returns a list of all study subject device assignments within the requested study.

### Request

```http
GET /centrepoint/v3/Studies/{studyId}/Assignments/{assignmentId}
```

### Response

```json
{
    "id": 23407,
    "activityMonitorSerial": "TAS1Z12345678",
    "subjectId": 17911,
    "studyId": 242,
    "createdDate": "2019-07-01T13:31:52.113Z",
    "collectionStartedDate": "2019-07-01T13:32:42.613Z",
    "collectionStoppedDate": "2019-07-01T16:03:14.73Z",
    "endedDate": "2019-07-01T16:03:47.827Z",
    "status": "Ended"
}
```

## Create Study Subject Device Assignment

Creates a subject device assignment to link an activity monitor to a subject.

**Request:**

```http
POST /centrepoint/v3/Studies/{studyId}/Assignments
{
    "subjectId": 12345678,
    "activityMonitorSerial": "TAS1Z12345678"
}
```

**Request Body Parameters:**

|Field|Type|Description|
|-----|----|-----------|
|**subjectId**|Number|CentrePoint Subject ID (see [Subjects](subjects.md))|
|**activityMonitorSerial**|String|Activity Monitor Serial Number (see [Activity Monitors](activity_monitors.md))

**Response:**

```json
{
  "id": 1,
  "activityMonitorSerial": "TAS1Z12345678",
  "subjectId": 12345678,
  "studyId": 1,
  "createdDate": "2019-07-10T20:57:58.166Z",
  "collectionStartedDate": "2019-07-10T20:57:58.166Z",
  "collectionStoppedDate": "2019-07-10T20:57:58.166Z",
  "endedDate": "2019-07-10T20:57:58.166Z",
  "scheduledCollectionStopDate": "2019-07-10T20:57:58.166Z",
  "status": "Incomplete Assignment"
}
```

**Response Body Fields:**

|Field|Type|Description|
|-----|----|-----------|
|**id**|Number|Assignment ID|
|**activityMonitorSerial**|Activity Monitor Serial Number (see [Activity Monitors](activity_monitors.md))|
|**subjectId**|Number|CentrePoint Subject ID (see [Subjects](subjects.md))|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**createdDate**|String (ISO8601 Date)|Date/Time of assignment creation|
|**collectionStartedDate**|String (ISO8601 Date)|Date/Time of activity monitor collection start|
|**collectionStoppedDate**|String (ISO8601 Date)|Date/Time of activity monitor collection end|
|**endedDate**|String (ISO8601 Date)|Date/Time of assignment ended|
|**scheduledCollectionStopDate**|String (ISO8601 Date)|Date/Time of scheduled collection stop date (see [Subject Activity Monitor Assignment Workflow](assignment_workflow.md))|
|**status**|String|Status of assignment|

## Change Study Subject Device Assignment Status

Allows for stopping collection on or forcefully ending an assignment.

**Request:**

```http
PUT /centrepoint/v3/Studies/{studyId}/Assignments/{assignmentId}
{
    "status": "Collection Stopped"
}
```

**Request Body Parameters:**

|Field|Description|
|-----|-----------|
|**status**|Desired assignment status (Collection Stopped, Forcefully Ended)|

**NOTE: The *Forcefully Ended* status should only be set when it is not possible to end assignment through ActiSync or CentrePoint Data Hub. (i.e. lost or broken activity monitor)**

**Response:**

```json
{
  "id": 1,
  "activityMonitorSerial": "TAS1Z12345678",
  "subjectId": 12345678,
  "studyId": 1,
  "createdDate": "2019-07-10T20:57:58.166Z",
  "collectionStartedDate": "2019-07-10T20:57:58.166Z",
  "collectionStoppedDate": "2019-07-10T20:57:58.166Z",
  "status": "Collection Stopped"
}
```

**Response Body Fields:**

|Field|Type|Description|
|-----|----|-----------|
|**id**|Number|Assignment ID|
|**activityMonitorSerial**|String|Activity Monitor Serial Number (see [Activity Monitors](activity_monitors.md))|
|**subjectId**|Number|CentrePoint Subject ID (see [Subjects](subjects.md))|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**createdDate**|String (ISO8601 Date)|Date/Time of assignment creation|
|**collectionStartedDate**|String (ISO8601 Date)|Date/Time of activity monitor collection start|
|**collectionStoppedDate**|String (ISO8601 Date)|Date/Time of activity monitor collection end|
|**endedDate**|String (ISO8601 Date)|Date/Time of assignment ended|
|**scheduledCollectionStopDate**|String (ISO8601 Date)|Date/Time of scheduled collection stop date (see [Subject Activity Monitor Assignment Workflow](assignment_workflow.md))|
|**status**|String|Status of assignment|
