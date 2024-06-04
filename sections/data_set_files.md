# DataSet Files

**NOTE: These requests require the *DataAccess* API scope. (see [Scopes](scopes.md))**

## Query DataSet Files

**Request:**

```http
GET /dataaccess/v3/studies/{studyId}/datasetfiles
```

**Body Parameters:**
All body parameters are optional.
|Field|Type|Description|
|-----|----|-----------|
|subjectId|long|Should be a valid Id of Subject|
|studyProgramId|String|Should be vaid Guid of Study Program|
|dataSetName|String|Should be valid DataSet Name|

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|studyId|Number|CentrePoint Study ID (see [Studies](studies.md))|
|subjectId|Number|CentrePoint Subject ID (see [Subjects](subjects.md))|
|studyProgramId|Guid|Study Program Id of a particular program|
|dataSetName|String|DataSet Name present in Study Program|
|fileName|String|Name of the dataset file|
|fileFormat|String|Values: csv|
|modifiedDate|String (ISO8601 Date)|The date of the last modification of data|
|fileUrl|String|The signed URL that can be used to download the dataset file|
|lastSuccessfulProgramExecutionTimeStamp|String (ISO8601 Date)|The date last successful execution of the study program happened|

```examples
/dataaccess/v3/studies/234/dataSetFiles
Body Parameters
{
} or
{
    "studyProgramId": "5b342a11-2fb9-4ad9-a7be-4d410181f51c"
} or
{
    "studyProgramId": "5b342a11-2fb9-4ad9-a7be-4d410181f51c",
    "subjectId": 10821
} or
{
    "studyProgramId": "5b342a11-2fb9-4ad9-a7be-4d410181f51c",
    "subjectId": 10821,
    "dataSetName": "ActivityDaily8"
}
```

```json
{
    "items": [
        {
            "studyId": 234,
            "studyVersion": 48,
            "studyProgramId": "5b342a11-2fb9-4ad9-a7be-4d410181f51c",
            "dataSetName": "ActivityDaily8",
            "subjectId": 10821,
            "fileName": "10821_0bbb9509-f20c-468b-8361-1684f7a50819_activitydaily8.csv.gz",
            "fileFormat": "csv",
            "modifiedDate": "2024-03-05T13:15:37.6848275+00:00",
            "lastSuccessfulProgramExecutionTimeStamp": "2024-03-05T13:10:06.4396436+00:00",
            "fileUrl": "https://datafiles.actigraphcorp.com/study-0000000234/subject-0000010821/datasetexports/5b342a11-2fb9-4ad9-a7be-4d410181f51c/activitydaily8/10821_0bbb9509-f20c-468b-8361-1684f7a50819_activitydaily8.csv.gz?skoid=444eeefb-b1cf-4b7b-804f-65129cd5fa9e&sktid=c004fd6f-8ed9-42bd-9303-191038d839e2&skt=2024-03-05T14%3A31%3A23Z&ske=2024-03-05T18%3A31%3A23Z&sks=b&skv=2022-11-02&sv=2022-11-02&se=2024-03-05T18%3A31%3A23Z&sr=b&sp=r&sig=eX7aeQRVUNleF%2FIFXv6kOwgaA7yJtVpRITvtGEZl4kU%3D",
            "downloadUrlExpiresOn": "2024-03-05T18:31:23+00:00"
        },
        {
            "studyId": 234,
            "studyVersion": 48,
            "studyProgramId": "5b342a11-2fb9-4ad9-a7be-4d410181f51c",
            "dataSetName": "ActivityEpochs10",
            "subjectId": 10821,
            "fileName": "10821_0bbb9509-f20c-468b-8361-1684f7a50819_activityepochs10.csv.gz",
            "fileFormat": "csv",
            "modifiedDate": "2024-03-05T13:15:39.0782758+00:00",
            "lastSuccessfulProgramExecutionTimeStamp": "2024-03-05T13:10:06.4396436+00:00",
            "fileUrl": "https://datafiles.actigraphcorp.com/study-0000000234/subject-0000010821/datasetexports/5b342a11-2fb9-4ad9-a7be-4d410181f51c/activityepochs10/10821_0bbb9509-f20c-468b-8361-1684f7a50819_activityepochs10.csv.gz?skoid=444eeefb-b1cf-4b7b-804f-65129cd5fa9e&sktid=c004fd6f-8ed9-42bd-9303-191038d839e2&skt=2024-03-05T14%3A31%3A23Z&ske=2024-03-05T18%3A31%3A23Z&sks=b&skv=2022-11-02&sv=2022-11-02&se=2024-03-05T18%3A31%3A23Z&sr=b&sp=r&sig=7AP6Qv2E3HQa0jG0Vi7NYNvQEnes7JtKNs5n6%2FhdYvc%3D",
            "downloadUrlExpiresOn": "2024-03-05T18:31:23+00:00"
        }
    ],
    "links": {},
    "totalCount": 2,
    "limit": 100,
    "offset": 0
}
```