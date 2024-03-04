# DataSet Export Files

**NOTE: These requests require the *DataAccess* API scope. (see [Scopes](scopes.md))**

## Query DataSet Export Files

**Request:**

```http
GET /studies/{studyId}/datasetexportfiles
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
|fileName|String|Name of the dataset export file|
|fileFormat|String|Values: csv|
|modifiedDate|String (ISO8601 Date)|The date of the last modification of data|
|fileUrl|String|The signed URL that can be used to download the dataset export file|
|lastSuccessfulProgramExecutionTimeStamp|String (ISO8601 Date)|The date last successful execution of the study program happened|

```examples
/studies/234/dataSetExportFiles
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
            "studyProgramId": "5b342a11-2fb9-4ad9-a7be-4d410181f51c",
            "dataSetName": "ActivityDaily8",
            "subjectId": 10821,
            "fileName": "10821_5e65f4e3-6996-41fe-a5aa-c79210285f7e.csv.gz",
            "fileFormat": "csv",
            "modifiedDate": "2024-02-29T10:09:20.5899754+00:00",
            "lastSuccessfulProgramExecutionTimeStamp": "2024-02-29T10:05:08.0962163+00:00",
            "fileUrl": "https://agdasstoragedev1.blob.core.windows.net/study-0000000234/subject-0000010821/datasetexports/5b342a11-2fb9-4ad9-a7be-4d410181f51c/activitydaily8/10821_5e65f4e3-6996-41fe-a5aa-c79210285f7e.csv.gz?skoid=444eeefb-b1cf-4b7b-804f-65129cd5fa9e&sktid=c004fd6f-8ed9-42bd-9303-191038d839e2&skt=2024-02-29T15%3A00%3A51Z&ske=2024-02-29T19%3A00%3A51Z&sks=b&skv=2022-11-02&sv=2022-11-02&se=2024-02-29T19%3A00%3A51Z&sr=b&sp=r&sig=0ncZbEZk7FTpC5k8S4SdYytr7I9JTaBVUsBRob%2BYiWw%3D"
        },
        {
            "studyId": 234,
            "studyProgramId": "5b342a11-2fb9-4ad9-a7be-4d410181f51c",
            "dataSetName": "ActivityEpochs10",
            "subjectId": 10821,
            "fileName": "10821_5e65f4e3-6996-41fe-a5aa-c79210285f7e.csv.gz",
            "fileFormat": "csv",
            "modifiedDate": "2024-02-29T10:09:22.374792+00:00",
            "lastSuccessfulProgramExecutionTimeStamp": "2024-02-29T10:05:08.0962163+00:00",
            "fileUrl": "https://agdasstoragedev1.blob.core.windows.net/study-0000000234/subject-0000010821/datasetexports/5b342a11-2fb9-4ad9-a7be-4d410181f51c/activityepochs10/10821_5e65f4e3-6996-41fe-a5aa-c79210285f7e.csv.gz?skoid=444eeefb-b1cf-4b7b-804f-65129cd5fa9e&sktid=c004fd6f-8ed9-42bd-9303-191038d839e2&skt=2024-02-29T15%3A00%3A51Z&ske=2024-02-29T19%3A00%3A51Z&sks=b&skv=2022-11-02&sv=2022-11-02&se=2024-02-29T19%3A00%3A51Z&sr=b&sp=r&sig=0ZFraO%2BrTyreLUOLVWmdhUA4hLyyL2IjDrta2Vp%2F9u0%3D"
        }
    ],
    "links": {},
    "totalCount": 2,
    "limit": 100,
    "offset": 0
}
```
