# Retrieval of Study Programs and Dataset Names

**NOTE: These requests require the *DataAccess* API scope (see [Scopes](scopes.md)) AND Study Programs to already be configured based on your study contract and specifications. If you are unsure of what has been contracted and or programed, please reach out to your Project Manager.**

Once the above confirmation and Study Programs have been applied, the following steps can be used to confirm the List of Study Programs. 

If your Study Programs have not been configured the responses below will be empty.

## List of Study Programs

Returns a list of study programs that are available for the given Study ID.

**Request:**

```http
GET /dataaccess/v3/Studies/{studyId}/programs
```

**Route Parameters:**

|Field|Type|Description|
|-----|----|-----------|
|**studyId**|Number|CentrePoint Study ID|

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|**studyId**|Number|CentrePoint Study ID|
|**studyProgramId**|Number|ID of a particular Study Program|
|**studyProgramName**|String|Name of a particular Study Program|

```json
{
    "items": [
        {
            "studyProgramId": "5b342a11-2fb9-4ad9-a7be-4d410181f51c",
            "studyId": 234,
            "studyProgramName": "Activity (30)"
        },
        {
            "studyProgramId": "1f08d07a-a507-47df-bc89-09412ae42352",
            "studyId": 234,
            "studyProgramName": "LeapBarometer (17)"
        },
        {
            "studyProgramId": "b21eb025-f1d9-4c97-a77a-b2878d860ade",
            "studyId": 234,
            "studyProgramName": "LeapPpgData (28)"
        },
        {
            "studyProgramId": "3d0cda8d-77a4-408b-afeb-02413a91c966",
            "studyId": 234,
            "studyProgramName": "ParamsAndSubject (31)"
        },
        {
            "studyProgramId": "1feadeea-d7e8-4e7e-878d-1cd5e205f7d1",
            "studyId": 234,
            "studyProgramName": "ParamsAndSubject (31)"
        }
    ],
    "links": {},
    "totalCount": 5,
    "limit": 100,
    "offset": 0
}
```

## Get a Study Program

Returns a specific study program that is available.

**Request:**

```http
GET /dataaccess/v3/Studies/{studyId}/programs/{studyProgramId}
```

**Route Parameters:**

|Field|Type|Description|
|-----|----|-----------|
|**studyId**|Number|CentrePoint Study ID|
|**studyProgramId**|Number|ID of a particular Study Program|

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|**studyId**|Number|CentrePoint Study ID|
|**studyProgramId**|Number|ID of a particular Study Program|
|**studyProgramName**|String|Name of a particular Study Program|

```json
{
    "studyProgramId": "1f08d07a-a507-47df-bc89-09412ae42352",
    "studyId": 234,
    "studyProgramName": "LeapBarometer (17)"
}
```

## Get Study Program Dataset Names

Returns a list of study program dataset names for a particular study programs that is available.

**Request:**

```http
GET /dataaccess/v3/Studies/{studyId}/programs/{studyProgramId}/datasets
```

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|**studyProgramId**|Number|ID of a particular Study Program|
|**dataSetName**|Number|Dataset name of a particular Study Program|

```json
{
    "items": [
        {
            "studyProgramId": "1f08d07a-a507-47df-bc89-09412ae42352",
            "dataSetName": "LeapAvgBarometer"
        }
    ],
    "links": {},
    "totalCount": 1,
    "limit": 100,
    "offset": 0
}
```
