# Raw Activity Data Request

-----

**NOTE: These requests require the *DataRetrieval* API scope. (see [Scopes](scopes.md))**

## Make request for raw activity data

**Request:**

```http
POST /dataretrieval/v1/RawActivityRequests
```

```json
{
  "fileFormat": "gt3x",
  "studyId": 236,
  "subjectId": 17896,
  "beginTimestampUtc": "2019-07-11T17:31:36.860Z",
  "endTimestampUtc": "2019-07-11T17:31:36.860Z"
}
```

**Request Parameters:**

|Field|Description|Allowed Values|
|-----|-----------|--------------|
|**fileFormat**|The requested file format for the exported raw data.|gt3x, csv, avro|
|**studyId**|CentrePoint Study ID (see [Studies](studies.md))||
|**subjectId**|CentrePoint Subject ID (see [Subjects](subjects.md))||
|**beginTimestampUtc**|The start of the time range in UTC for which export data.||
|**beginTimestampUtc**|The end of the time range in UTC for which export data.||

## Get information about a raw activity data request

**Request:**

```http
GET /dataretrieval/v1/RawActivityRequests/{trackingId}
```

**Response:**

|Field|Description|
|-----|-----------|
|**fileFormat**|gt3x, csv, or avro (see [Raw Data File Formats](raw_data_file_formats.md))|
|**id**|Data Retrieval Requests Tracking ID|
|**studyId**|CentrePoint Study ID (see [Studies](studies.md))|
|**subjectId**|CentrePoint Subject ID (see [Subjects](subjects.md))|
|**status**|pending, processing, completed, error|
|**createdDateTimeUtc**|Date of assignment creation|
|**startDateTimeUtc**|Date request processing started|
|**completedDateTimeUtc**|Date request processing completed|

```json
{
    "fileFormat": "gt3x",
    "id": "8b2fbb54-f635-47e6-8cb9-e187d3457b8c",
    "studyId": 236,
    "subjectId": 17896,
    "status": "pending",
    "createdDateTimeUtc": "2019-07-11T18:36:38.2171641+00:00"
}
```

## Get information about data files for a completed raw activity data request

**Request:**

```http
GET /dataretrieval/v1/RawActivityRequests/{trackingId}/datafiles
```

**Response:**

|Field|Description|
|-----|-----------|
|**id**|Data file ID|
|**fileName**|Data file name|
|**expirationDateUtc**|Date time after which Data File will no longer be available|
|**fileSizeBytes**|File size in bytes|

```json
[
    {
        "id": "255037a7-c163-483d-182a-08d7062fed2c",
        "fileName": "17896_TAS1F39160337_1561494008_1561645376_1ab3.csv",
        "expirationDateUtc": "2019-08-10T18:10:19.9895852+00:00",
        "fileSizeBytes": 199292255
    },
    {
        "id": "19688216-d13b-4403-182b-08d7062fed2c",
        "fileName": "17896_c7eb337a-584a-4d2e-96b3-06a2e5a15563-0531.json",
        "expirationDateUtc": "2019-08-10T18:10:19.9895852+00:00",
        "fileSizeBytes": 296
    }
]
```

## Get details about a specific data file for a completed raw activity data request

**Request:**

```http
GET /dataretrieval/v1/RawActivityRequests/{trackingId}/datafiles/{dataFileId}
```

**Response:**

```json
{
    "id": "255037a7-c163-483d-182a-08d7062fed2c",
    "fileName": "17896_TAS1F39160337_1561494008_1561645376_1ab3.csv",
    "expirationDateUtc": "2019-08-10T18:10:19.9895852+00:00",
    "fileSizeBytes": 199292255
}
```

## Get download URL for a specific data file for a completed raw activity data request

**Request:**

```http
GET /dataretrieval/v1/RawActivityRequests/{trackingId}/datafiles/{dataFileId}/downloadurl
```

**Response:**

|Field|Description|
|-----|-----------|
|**downloadUrl**|URL to download data file|
|**expirationDateUtc**|Date time after which download link expires. For security reasons, data file URL's are only valid for a short length of time. If the link has expired, you can make another request to receive a new one.|

```json
{
    "downloadUrl": "https://example.blob.core.windows.net/dataretrieval-study-0000000236/17896_c7eb337a-584a-4d2e-96b3-06a2e5a15563-3f1f_1.csv?sv=2018-03-28&sr=b&sig=ihKXpfo7s1AKdML7JjngT2heT6mILyAwV%2FNH2Rn6DyI%3D&st=2019-07-11T19%3A31%3A37Z&se=2019-07-11T19%3A33%3A38Z&sp=r&rscd=attachment%3B%20filename%3D17896_TAS1Z12345678_1561494008_1561645376_1ab3.csv",
    "expirationDateUtc": "2019-07-11T19:33:38.3716487+00:00"
}
```
