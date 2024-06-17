# DataSet Export Subjects

**NOTE: These requests require the *DataAccess* API scope (see [Scopes](scopes.md)) AND a request for processing should have already been submitted.  If a request for processing has not been submitted the responses below will be empty.**

To submit a request for processing please email CPDprocessing@theactigraph.com. From there your request will be submitted and a confirmation email will be sent once completed.  Please allow 1-2 business days from the submission to process this request. At this time, we ask that only one user from your organization submit one request per study, once you have received confirmation that the request is closed at that time another request can be submitted.

## Query Subjects

**Request:**

```http
GET /dataaccess/v3/studies/{studyId}/subjects
```

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|studyId|Number|CentrePoint Study ID (see [Studies](studies.md))|
|subjectId|Number|CentrePoint Subject ID (see [Subjects](subjects.md))|
|lastRawUploadedTimeStamp|DateTimeOffset|Last Raw Data Uploaded Timestamp|
|studyProgramExecutions|List|List of all the programs that were executed for the subject|

The study program executions will have following fields.

|Field|Type|Description|
|-----|----|-----------|
|studyProgramId|Guid|Study Program Id of a particular program|
|studyProgramName|String|Study Program Name of a particular program|
|lastSuccessfulProgramExecutionTimeStamp|DateTimeOffset|Timestamp when the program was successfully exscuted for the subject|

```examples
/dataaccess/v3/studies/234/subjects
```

```json
{
    "items": [
        {
            "studyId": 234,
            "subjectId": 10820,
            "lastRawUploadedTimeStamp": "2024-03-07T09:27:02.6983354+00:00",
            "studyProgramExecutions": [
                {
                    "studyProgramId": "1f08d07a-a507-47df-bc89-09412ae42352",
                    "studyProgramName": "LeapBarometer (17)",
                    "lastSuccessfulProgramExecutionTimeStamp": "0001-01-01T00:00:00+00:00"
                }
            ]
        },
        {
            "studyId": 234,
            "subjectId": 10821,
            "lastRawUploadedTimeStamp": "0001-01-01T00:00:00+00:00",
            "studyProgramExecutions": [
                {
                    "studyProgramId": "5b342a11-2fb9-4ad9-a7be-4d410181f51c",
                    "studyProgramName": "Activity (30)",
                    "lastSuccessfulProgramExecutionTimeStamp": "2024-03-07T06:58:03.6743755+00:00"
                }
            ]
        }
    ],
    "links": {},
    "totalCount": 2,
    "limit": 100,
    "offset": 0
}
```

## Query Subject Details

**Request:**

```http
GET /dataaccess/v3/studies/{studyId}/subjects/{subjectId}
```

**Response:**

|Field|Type|Description|
|-----|----|-----------|
|studyId|Number|CentrePoint Study ID (see [Studies](studies.md))|
|subjectId|Number|CentrePoint Subject ID (see [Subjects](subjects.md))|
|lastRawUploadedTimeStamp|DateTimeOffset|Last Raw Data Uploaded Timestamp|
|studyProgramExecutions|List|List of all the programs that were executed for the subject|

The study program executions will have following fields.

|Field|Type|Description|
|-----|----|-----------|
|studyProgramId|Guid|Study Program Id of a particular program|
|studyProgramName|String|Study Program Name of a particular program|
|lastSuccessfulProgramExecutionTimeStamp|DateTimeOffset|Timestamp when the program was successfully exscuted for the subject|

```examples
/dataaccess/v3/studies/234/subjects/10820
```

```json
{
    "studyId": 234,
    "subjectId": 10820,
    "lastRawUploadedTimeStamp": "2024-03-07T09:27:02.6983354+00:00",
    "studyProgramExecutions": [
        {
            "studyProgramId": "1f08d07a-a507-47df-bc89-09412ae42352",
            "studyProgramName": "LeapBarometer (17)",
            "lastSuccessfulProgramExecutionTimeStamp": "2024-03-12T13:26:19.0936591+00:00"
        }
    ]
}
```
