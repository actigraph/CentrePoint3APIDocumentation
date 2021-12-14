# Data Access Files

**NOTE: These requests require the *DataAccess* API scope. (see [Scopes](scopes.md))**

## Query Subject Data Files

A list of data files that can be accessed.

**Request:**

```http
GET /dataaccess/v3/files/studies/{studyId}/subjects/{subjectId}/{dataCategory}?sortOrder={sortOrderOption}&fileFormat={fileFormatOption}&startDate={dateTimeValue}&endDate={dateTimeValue}
```

**Query Parameters:**

All query parameters are optional.

|Field|Type|Description|
|-----|----|-----------|
|sortOrder|String|Values: asc, desc (Defaults to asc)|
|fileFormat|String|Values: csv, avro|
|startDate|String (ISO8601 Date)|Inclusive date time to limit the start of the time range of data files|
|endDate|String (ISO8601 Date)|Inclusive date time to limit the end of the time range of data files|

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|studyId|Number|CentrePoint Study ID (see [Studies](studies.md))|
|subjectId|Number|CentrePoint Subject ID (see [Subjects](subjects.md))|
|dataCategory|String|Values: raw-accelerometer|
|date|String (ISO8601 Date)|The day date of the data contained in the file
|fileName|String|Name of the data file 
|fileFormat|String|Values: csv, avro 
|modifiedDate|String (ISO8601 Date)|The date of the last modification to the particular day of data
|downloadUrl|String|The signed URL that can be used to download the file
|downloadUrlExpiresOn|String (ISO8601 Date)|The date that the download URL expires

```json
{
    "items": [
        {
            "studyId": 652,
            "subjectId": 47589,
            "dataCategory": "raw-accelerometer",
            "date": "2021-01-01T00:00:00+00:00",
            "fileName": "raw-accelerometer_2021-01-01_7eee8e85.csv.gz",
            "fileFormat": "csv",
            "modifiedDate": "2021-01-02T20:43:57+00:00",
            "downloadUrl": "https://datafiles.actigraphcorp.com/study-0000000652/subject-0000047589/raw-accelerometer/2021/01/01/raw-accelerometer_2021-01-01_7eee8e85.csv.gz?sp=r&st=2021-01-30T17:10:52Z&se=2021-02-01T01:10:52Z&spr=https&sv=2020-08-04&sr=b&sig=u2L1XjnWh0BxxXrsE%2FD%2FXXRAGSSoQ8Wbpg19Le2YTDw%3D",
            "downloadUrlExpiresOn": "2021-01-03T03:45:32+00:00"
        },
        {
            "studyId": 652,
            "subjectId": 47589,
            "dataCategory": "raw-accelerometer",
            "date": "2021-01-01T00:00:00+00:00",
            "fileName": "raw-accelerometer_2021-01-01_7eee8e85.avro",
            "fileFormat": "avro",
            "modifiedDate": "2021-01-02T20:43:57+00:00",
            "downloadUrl": "https://datafiles.actigraphcorp.com/study-0000000652/subject-0000047589/raw-accelerometer/2021/01/01/raw-accelerometer_2021-01-01_7eee8e85.avro?sp=r&st=2021-01-30T17:10:52Z&se=2021-02-01T01:10:52Z&spr=https&sv=2020-08-04&sr=b&sig=u2L1XjnWh0BxxXrsE%2FD%2FXXRAGSSoQ8Wbpg19Le2YTDw%3D",
            "downloadUrlExpiresOn": "2021-01-03T03:45:32+00:00"
        },
        {
            "studyId": 652,
            "subjectId": 47589,
            "dataCategory": "raw-accelerometer",
            "date": "2021-01-02T00:00:00+00:00",
            "fileName": "raw-accelerometer_2021-01-02_f7f4d916.csv.gz",
            "fileFormat": "csv",
            "modifiedDate": "2021-01-03T20:43:57+00:00",
            "downloadUrl": "https://datafiles.actigraphcorp.com/study-0000000652/subject-0000047589/raw-accelerometer/2021/01/02/raw-accelerometer_2021-01-02_f7f4d916.csv.gz?sp=r&st=2021-01-30T17:10:52Z&se=2021-02-01T01:10:52Z&spr=https&sv=2020-08-04&sr=b&sig=u2L1XjnWh0BxxXrsE%2FD%2FXXRAGSSoQ8Wbpg19Le2YTDw%3D",
            "downloadUrlExpiresOn": "2021-01-03T03:45:32+00:00"
        },
        {
            "studyId": 652,
            "subjectId": 47589,
            "dataCategory": "raw-accelerometer",
            "date": "2021-01-02T00:00:00+00:00",
            "fileName": "raw-accelerometer_2021-01-02_f7f4d916.avro",
            "fileFormat": "avro",
            "modifiedDate": "2021-01-03T20:43:57+00:00",
            "downloadUrl": "https://datafiles.actigraphcorp.com/study-0000000652/subject-0000047589/raw-accelerometer/2021/01/02/raw-accelerometer_2021-01-02_f7f4d916.avro?sp=r&st=2021-01-30T17:10:52Z&se=2021-02-01T01:10:52Z&spr=https&sv=2020-08-04&sr=b&sig=u2L1XjnWh0BxxXrsE%2FD%2FXXRAGSSoQ8Wbpg19Le2YTDw%3D",
            "downloadUrlExpiresOn": "2021-01-03T03:45:32+00:00"
        }
    ],
    "links": {},
    "totalCount": 4,
    "limit": 100,
    "offset": 0
}
```

## Query Subject Data Files By Year

A list of data files that can be accessed for a particular year.

**Request:**

```http
GET /dataaccess/v3/files/studies/{studyId}/subjects/{subjectId}/{dataCategory}/{year}?sortOrder={sortOrderOption}&fileFormat={fileFormatOption}
```

**Query Parameters:**

All query parameters are optional.

|Field|Type|Description|
|-----|----|-----------|
|sortOrder|String|Values: asc, desc (Defaults to asc)|
|fileFormat|String|Values: csv, avro|

**Response:**

Same response format as Query Subject Data Files

## Query Subject Data Files By Month

A list of data files that can be accessed for a particular month.

**Request:**

```http
GET /dataaccess/v3/files/studies/{studyId}/subjects/{subjectId}/{dataCategory}/{year}/{month}?sortOrder={sortOrderOption}&fileFormat={fileFormatOption}
```

**Query Parameters:**

All query parameters are optional.

|Field|Type|Description|
|-----|----|-----------|
|sortOrder|String|Values: asc, desc (Defaults to asc)|
|fileFormat|String|Values: csv, avro|

**Response:**

Same response format as Query Subject Data Files

## Query Subject Data Files By Day

A list of data files that can be accessed for a particular day.

**Request:**

```http
GET /dataaccess/v3/files/studies/{studyId}/subjects/{subjectId}/{dataCategory}/{year}/{month}/{day}?sortOrder={sortOrderOption}&fileFormat={fileFormatOption}
```

**Query Parameters:**

All query parameters are optional.

|Field|Type|Description|
|-----|----|-----------|
|sortOrder|String|Values: asc, desc (Defaults to asc)|
|fileFormat|String|Values: csv, avro|

**Response:**

Same response format as Query Subject Data Files
