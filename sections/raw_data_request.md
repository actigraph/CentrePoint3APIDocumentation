# Raw Activity Data Request

**IMPORTANT:**
It is now recommended to use the [Data Access Files](data_access_files.md) for retrieving raw accelerometer data.

NOTE: It is now recommended to use the [Data Access Files](data_access_files.md) endpoint instead of the Data Retrieval endpoint for retrieving all raw accelerometer data. There may be fees associated for historical data access file generation if the study has not been previously setup.

RAW data retrieval requests SHALL NOT be performed to retrieve ALL the historic RAW data for all subjects in a given study. Instead, requests shall be used in conjunction with the raw-processing-complete webhook to support the retrieval of raw data for a given upload as it is uploaded/processed in a near real-time fashion. Due to the heavy computation required to create a file in the GT3X format, the time range for GT3X format requests is limited to 15 days.

A maximum of 10 active requests are allowed at one time. If attempting to submit more than 10 active requests, the following error will be received:

"There are currently 10 active requests. The maximum concurrent active requests limit is 10."

Status requests can be made for the tracking id's to identify the status of the individual requests.

The webhook [data_retrieval_complete](https://github.com/actigraph/CentrePointWebhookDocumentation/blob/main/Event%20Types/data_retrieval_complete_event.md) can be used to receive notifications of when a request has completed.

Data retrieval requests will be automatically cancelled if they reach a 6 hour execution time from the time they begin processing. If this occurs, a new request can be submitted with a shorter date range.

**NOTE: These requests require the *DataRetrieval* API scope. (see [Scopes](scopes.md))**

## Make request for raw activity data

**Request:**

```http
POST /dataretrieval/v3/RawActivityRequests
```

```json
{
  "fileFormat": "avro",
  "studyId": 236,
  "subjectId": 17896,
  "beginTimestampUtc": "2019-07-11T17:31:36.860Z",
  "endTimestampUtc": "2019-07-11T17:31:36.860Z"
}
```

**Request Parameters:**

|Field|Type|Description|Allowed Values|
|-----|----|-----------|--------------|
|**fileFormat**|String|The requested file format for the exported raw data.|gt3x, csv, avro (see [Raw Data File Formats](raw_data_file_formats.md))|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))||
|**subjectId**|Number|CentrePoint Subject ID (see [Subjects](subjects.md))||
|**beginTimestampUtc**|String (ISO8601 Date)|The start of the time range in UTC for which export data.||
|**endTimestampUtc**|String (ISO8601 Date)|The end of the time range in UTC for which export data.||

## Get information about a raw activity data request

**Request:**

```http
GET /dataretrieval/v3/RawActivityRequests/{trackingId}
```

**Response:**

|Field|Type|Description|
|-----|----|-----------|
|**fileFormat**|String|gt3x, csv, or avro (see [Raw Data File Formats](raw_data_file_formats.md))|
|**id**|String (GUID)|Data Retrieval Requests Tracking ID|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**subjectId**|Number|CentrePoint Subject ID (see [Subjects](subjects.md))|
|**status**|String|pending, processing, completed, error|
|**createdDateTimeUtc**|String (ISO8601 Date)|Date of assignment creation|
|**startDateTimeUtc**|String (ISO8601 Date)|Date request processing started|
|**completedDateTimeUtc**|String (ISO8601 Date)|Date request processing completed|

```json
{
    "fileFormat": "avro",
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
GET /dataretrieval/v3/RawActivityRequests/{trackingId}/datafiles
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

## Get download URL for a specific data file for a completed raw activity data request

This endpoint provides a download URL for a data file generated by a data retrieval request.

**Request:**

```http
GET /dataretrieval/v3/DataFiles/{dataFileId}/downloadurl
```

**Response:**

|Field|Type|Description|
|-----|----|-----------|
|**downloadUrl**|String|URL to download data file|
|**expirationDateUtc**|String (ISO8601 Date)|Date time after which download link expires. For security reasons, data file URL's are only valid for a short length of time. If the link has expired, you can make another request to receive a new download URL.|

```json
{
    "downloadUrl": "https://example.blob.core.windows.net/dataretrieval-study-0000000236/17896_c7eb337a-584a-4d2e-96b3-06a2e5a15563-3f1f_1.csv?sv=2018-03-28&sr=b&sig=ihKXpfo7s1AKdML7JjngT2heT6mILyAwV%2FNH2Rn6DyI%3D&st=2019-07-11T19%3A31%3A37Z&se=2019-07-11T19%3A33%3A38Z&sp=r&rscd=attachment%3B%20filename%3D17896_TAS1Z12345678_1561494008_1561645376_1ab3.csv",
    "expirationDateUtc": "2019-07-11T19:33:38.3716487+00:00"
}
```
