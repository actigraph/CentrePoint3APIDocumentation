# Uploads

**NOTE: These requests require the *CentrePoint* API scope. (see [Scopes](scopes.md))**

## List Subject Uploads

Returns a list of all uploads for a subject.

### Request

```http
GET /centrepoint/v3/Studies/{studyId}/Subjects/{subjectId}/Uploads
```



### Response

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

**Response Properties:**

Field|Type|Description|Notes
-----|----|-----------|-----
**id**|Number|CentrePoint Upload ID||
**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))||
**subjectId**|Number|CentrePoint Subject ID (see [Subjects](subjects.md))||
**activityMonitorSerial**|String|Serial of the recording monitor||
**assignmentId**|Number|CentrePoint Assignment ID (see [Assignment](assignments.md))||
**dateUploadedUtc**|String (ISO8601 Date)|Date when the upload was received||
**activityMonitorBatteryVoltage**|Number|Voltage of the monitor when the upload was received||
**activityMonitorFirmware**|String|Firmware version of the monitor when the upload was received||
**activityMonitorSampleRateHz**|Number|Sample rate of the monitor when the upload was received||
**uploadFiles**|Object Array (see UploadFile)|The file(s) received for the upload||

**Upload File Properties:**

Field|Type|Description|Notes
-----|----|-----------|-----
**id**|Number|CentrePoint Upload File ID||
**fileType**|String|Type of the data contained in the file||
**totalRecords**|Number|Total number of records contained in the file||
**recordsInserted**|Number|Total number of records inserted for storage in CentrePoint||
**beginOfData**|Number|The start UTC timestamp of the data in the upload file||
**endOfData**|Number|The end UTC timestamp of the data in the upload file||

**Response Example**

```json
{
  "items": [
    {
      "id": 5461,
      "studyId": 1156,
      "subjectId": 2114,
      "activityMonitorSerial": "CPW1B21356478",
      "assignmentId": 3125,
      "dateUploadedUtc": "2020-10-26T18:39:57Z",
      "activityMonitorBatteryVoltage": 3.821,
      "activityMonitorFirmware": "1.1.2",
      "activityMonitorSampleRateHz": 32,
      "uploadFiles": [
        {
          "id": 8456,
          "fileType": "RAW",
          "totalRecords": 322,
          "recordsInserted": 322,
          "beginOfData": "2020-10-20T18:39:57Z",
          "endOfData": "2020-10-26T18:39:57Z"
        }
      ]
    }
  ],
  "links": {},
  "totalCount": 1,
  "limit": 100,
  "offset": 0
}
```



## Subject Upload Details

Returns detailed information about the requested upload.

**Request:**

```http
GET /centrepoint/v3/Studies/{studyId}/Subjects/{subjectId}/Uploads/{uploadId}
```

**Response:**

```json
{
    "id": 5461,
    "studyId": 1156,
    "subjectId": 2114,
    "activityMonitorSerial": "CPW1B21356478",
    "assignmentId": 3125,
    "dateUploadedUtc": "2020-10-26T18:39:57Z",
    "activityMonitorBatteryVoltage": 3.821,
    "activityMonitorFirmware": "1.1.2",
    "activityMonitorSampleRateHz": 32,
    "uploadFiles": [
    {
        "id": 8456,
        "fileType": "RAW",
        "totalRecords": 322,
        "recordsInserted": 322,
        "beginOfData": "2020-10-20T18:39:57Z",
        "endOfData": "2020-10-26T18:39:57Z"
    }]
}
```