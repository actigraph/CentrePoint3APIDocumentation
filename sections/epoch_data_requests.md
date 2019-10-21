# Epoch Data Requests

**NOTE: These requests require the *DataRetrieval* scope. (see [Scopes](scopes.md))**

## Make request for epoch summary data

**Request:**

```http
POST /dataretrieval/v3/EpochRequests
```

```json
{
  "fileFormat": "csv",
  "summaryLengthSeconds": 60,
  "includePartialEpochs": true,
  "activityMonitorSerial": "CPW1A23190055",
  "studyId": 1,
  "subjectId": 123,
  "beginTimestampUtc": "2019-07-11T19:44:08.417Z",
  "endTimestampUtc": "2019-07-11T19:44:08.417Z"
}
```

**Request Parameters:**

|Field|Type|Description|Allowed Values|
|-----|----|-----------|--------------|
|**fileFormat**|String|The requested file format for the exported raw data.|csv (see [Epoch Data File Formats](epoch_data_file_formats.md))|
|**summaryLengthSeconds**|Number|Epoch summary length in seconds|1 - 3600
|**includePartialEpochs**|Boolean|Indicates whether or not to include epochs with less than epoch summary length of data (defaults to false)|true or false
|**activityMonitorSerial**|String|Activity monitor serial number|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))||
|**subjectId**|Number|CentrePoint Subject ID (see [Subjects](subjects.md))||
|**beginTimestampUtc**|String (ISO8601 Date)|The start of the time range in UTC for which export data.||
|**endTimestampUtc**|String (ISO8601 Date)|The end of the time range in UTC for which export data.||

**Response**


```json
{
    "fileFormat": "Csv",
    "summaryLengthSeconds": 60,
    "includePartialEpochs": false,
    "id": "4b911d04-45c4-480b-a1c6-e53894f41869",
    "studyId": 1,
    "subjectId": 123,
    "status": "Pending",
    "beginTimestampUtc": "2019-07-11T19:44:08.417Z",
    "endTimestampUtc": "2019-07-11T19:44:08.417Z",
    "createdDateTimeUtc": "2019-10-21T14:13:33.5082033+00:00"
}
```
**Response Parameters:**

|Field|Type|Description|
|-----|----|-----------|
|**id**|String|Epoch Data Retrieval Request Tracking ID|



## Get information about a epoch data request

**Request:**

```http
GET /dataretrieval/v3/EpochRequests/{trackingId}
```

**Response:**

|Field|Type|Description|
|-----|----|-----------|
|**fileFormat**|String|csv|
|**summaryLengthSeconds**|Number|Epoch summary length in seconds|
|**includePartialEpochs**|Boolean|Indicates if request includes epochs with less than epoch summary length of data|
|**id**|String (GUID)|Data Retrieval Requests Tracking ID|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**subjectId**|Number|CentrePoint Subject ID (see [Subjects](subjects.md))|
|**status**|String|pending, processing, completed, error|
|**createdDateTimeUtc**|String (ISO8601 Date)|Date of assignment creation|
|**startDateTimeUtc**|String (ISO8601 Date)|Date request processing started|
|**completedDateTimeUtc**|String (ISO8601 Date)|Date request processing completed|

```json
{
    "fileFormat": "csv",
    "summaryLengthSeconds": 60,
    "includePartialEpochs": false,
    "id": "9e9df727-ab76-4ed0-be25-22771a8b7e20",
    "studyId": 236,
    "subjectId": 17896,
    "status": "processing",
    "createdDateTimeUtc": "2019-07-11T19:51:29.9092125+00:00",
    "startDateTimeUtc": "2019-07-11T19:51:35.9870351+00:00"
}
```

## Get information about data files for a completed epoch data request

**Request:**

```http
GET /dataretrieval/v3/EpochRequests/{trackingId}/datafiles
```

**Response:**

|Field|Type|Description|
|-----|----|-----------|
|**id**|String (GUID)|Data file ID|
|**fileName**|String|Data file name|
|**expirationDateUtc**|String (ISO8601 Date)|Date time after which Data File will no longer be available|
|**fileSizeBytes**|Number|File size in bytes|

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
GET /dataretrieval/v3/DataFiles/{dataFileId}
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

## Get download URL for a specific data file for a completed epoch data request

**Request:**

```http
GET /dataretrieval/v3/DataFiles/{dataFileId}/downloadurl
```

**Response:**

|Field|Type|Description|
|-----|----|-----------|
|**downloadUrl**|String (URL)|URL to download data file|
|**expirationDateUtc**|String (ISO8601 Date)|Date time after which download link expires. For security reasons, data file URL's are only valid for a short length of time. If the link has expired, you can make another request to receive a new download URL.|

```json
{
    "downloadUrl": "https://example.blob.core.windows.net/dataretrieval-study-0000000236/17896_c7eb337a-584a-4d2e-96b3-06a2e5a15563-3f1f_1.csv?sv=2018-03-28&sr=b&sig=ihKXpfo7s1AKdML7JjngT2heT6mILyAwV%2FNH2Rn6DyI%3D&st=2019-07-11T19%3A31%3A37Z&se=2019-07-11T19%3A33%3A38Z&sp=r&rscd=attachment%3B%20filename%3D17896_TAS1Z12345678_1561494008_1561645376_1ab3.csv",
    "expirationDateUtc": "2019-07-11T19:33:38.3716487+00:00"
}
```
