# Data Set Export Files

**NOTE: These requests require the *DataAccess* API scope. (see [Scopes](scopes.md))**

## Study Programs

The request will fetch the study programs for the latest locked study version of the study.

**Request:**

```http
GET /dataaccess/v1/studies/{studyId}/programs?limit={limit}&offset={offset}
```

**Query Parameters:**

All query parameters are optional.

|Field|Type|Description|
|-----|----|-----------|
|limit|Number|The maximum number of records to be fetched. Default value is 100.|
|offset|Number|The offset from which to fetch the records. Default value is 0.|

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|programFullName|String|The full name of the program
|studyProgramId|Guid|Study Program Id of the program
|newer|Boolean|Values: true, false. True, if there is a newer version of the program available else false.
|programKey|Guid|Program Key of the program
|libraryVer|Number|Library Version of the program
|description|String|Description of the program
|category|String|Values: CutPoint, Sleep, Gait, Activity, Wear, UpperLimb
|studyId|Number|CentrePoint Study ID (see [Studies](studies.md))|
|studyVersion|Number|Study Version of the program

```json
{
    "items": [
        {
            "programFullName": "ADXLMinuteAverageTemperature (8)",
            "studyProgramId": "5f759312-a6cc-4ac3-bc21-0b52cf18d738",
            "newer": true,
            "programKey": "7825c7cc-6476-4468-b256-39cf8cb6b26b",
            "libraryVer": 8,
            "description": "Provide minute level average temperature in Celsius from the ADXL CPIW sensor",
            "category": "UpperLimb",
            "studyId": 239,
            "studyVersion": 3
        },
        {
            "programFullName": "ErrorExit (9)",
            "studyProgramId": "bacb3051-6506-4bd6-aae8-cd97b2f7d3ea",
            "newer": false,
            "programKey": "bb818447-8dd0-44c6-a09f-83925a1befda",
            "libraryVer": 9,
            "description": "Set exit code and error message via parameters",
            "category": "CutPoint",
            "studyId": 239,
            "studyVersion": 3
        },
        {
            "programFullName": "MCUMinuteAverageTemperature (9)",
            "studyProgramId": "dadd2e3d-d5f1-452b-aa84-f1310728a22d",
            "newer": true,
            "programKey": "1e4707a3-97b9-4b33-999e-d965f9f76349",
            "libraryVer": 9,
            "description": "Update 2: Provide minute level average temperature in Celsius from the MCU CPIW sensor",
            "category": "UpperLimb",
            "studyId": 239,
            "studyVersion": 3
        },
        {
            "programFullName": "SleepMetricsDacnn (11)",
            "studyProgramId": "f546be7c-b0d6-44f3-86ee-870cd9d25435",
            "newer": true,
            "programKey": "4e9c07dc-9c9d-4887-ae22-45efe2f10bf1",
            "libraryVer": 11,
            "description": "Sleep metrics based on DACNN model. Added DEVICE data as input for testing.",
            "category": "Sleep",
            "studyId": 239,
            "studyVersion": 3
        },
        {
            "programFullName": "ErrorExit (15)",
            "studyProgramId": "52cb733e-cca1-4cee-9cdc-f78c4b5c3887",
            "newer": false,
            "programKey": "bb818447-8dd0-44c6-a09f-83925a1befda",
            "libraryVer": 15,
            "description": "Set exit code and error message via parameters",
            "category": "CutPoint",
            "studyId": 239,
            "studyVersion": 3
        }
    ],
    "links": {},
    "totalCount": 5,
    "limit": 100,
    "offset": 0
}
```

## Study Program

The request will fetch the specific study program's details for the latest locked study version of the study.

**Request:**

```http
GET /dataaccess/v1/studies/{studyId}/programs/{studyProgramId}
```

**Response:**

```json
{
    "programFullName": "ADXLMinuteAverageTemperature (8)",
    "studyProgramId": "5f759312-a6cc-4ac3-bc21-0b52cf18d738",
    "newer": true,
    "programKey": "7825c7cc-6476-4468-b256-39cf8cb6b26b",
    "libraryVer": 8,
    "description": "Provide minute level average temperature in Celsius from the ADXL CPIW sensor",
    "category": "UpperLimb",
    "studyId": 239,
    "studyVersion": 3
}
```
