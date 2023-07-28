# Subjects

**NOTE: These requests require the *CentrePoint* API scope. (see [Scopes](scopes.md))**

## List Study Subjects

Returns a list of all subjects within the requested study.

### Request

```http
GET /centrepoint/v3/Studies/{studyId}/Subjects
```

### Response

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

```json
{
    "items": [
        {
            "id": 17910,
            "studyId": 242,
            "siteId": 2931,
            "siteIdentifier": "123",
            "subjectIdentifier": "TEST001",
            "dob": "2019-01-01",
            "gender": "Male",
            "timezone": "Africa/Abidjan",
            "wearPosition": "Left Wrist",
            "weight": 100.00,
            "weightUnit": "Lbs",
            "assignmentStatus": "Assigned",
            "assignmentId": 1423
        },
        {
            "id": 17911,
            "studyId": 242,
            "siteId": 2931,
            "siteIdentifier": "123",
            "subjectIdentifier": "TEST002",
            "dob": "1970-01-01",
            "gender": "Female",
            "timezone": "Africa/Abidjan",
            "wearPosition": "Right Wrist",
            "weight": 176.37,
            "weightUnit": "Lbs",
            "assignmentStatus": "Not Assigned"
        }
    ],
    "links": {},
    "totalCount": 2,
    "limit": 100,
    "offset": 0
}
```

**Response Properties:**

Field|Type|Description|Notes
-----|----|-----------|-----
id|Number|CentrePoint Subject ID||
studyId|Number|CentrePoint Study ID (see [Studies](studies.md))||
siteId|Number|CentrePoint Site ID (see [Sites](sites.md))||
siteIdentifier|String|User-specified Site Identifier that is unique within the study.|Used as a prefix to the subject identifier
subjectIdentifier|String|User-specified Subject Identifier that is unique within the study.|
dob|ISO8601 Date|Subject's Date of Birth|(if collected by study)|
gender|String|Subject's gender|(if collected by study)|
timezone|String|Subject's Timezone||
wearPosition|String|Subject's activity monitor wear position|
weight|Number|Subject's weight|(if collected by study)|
weightUnit|String|Pounds (lbs) or Kilograms (kg)|
assignmentStatus|String|Indicates if activity monitor is assigned to subject|
assignmentId|Number|The ID of the subject's current assignment if the subject has an active assignment|

## Subject Details

Returns detailed information about the requested subject.

**Request:**

```http
GET /centrepoint/v3/Studies/{studyId}/Subjects/{subjectId}
```

**Response:**

```json
{
    "id": 17911,
    "studyId": 242,
    "siteId": 2931,
    "siteIdentifier": "123",
    "subjectIdentifier": "TEST002",
    "dob": "1970-01-01",
    "gender": "Female",
    "timezone": "Africa/Abidjan",
    "wearPosition": "Right Wrist",
    "weight": 176.37,
    "weightUnit": "Lbs",
    "assignmentStatus": "Not Assigned"
}
```

## Add Subject

Creates a new subject. Subjects are created at the site level.  List sites to find out which you can access. The new subject's ID is returned upon successful creation along with a 201 Created response.

**Request:**

```http
POST /centrepoint/v3/Studies/{studyId}/subjects
Content-Type: application/json
{
    "subjectIdentifier": "TEST003",
    "siteId": 2931,
    "dob": "1990-07-10",
    "gender": "Male",
    "weight": 100,
    "weightUnit": "Lbs",
    "height": 200,
    "heightUnit": 'cm',
    "wearPosition": "Left Wrist"
}
```

**Request Properties:**

Field|Type|Min|Max|Required|Accepted Values|Description|Notes
-----|----|---|---|--------|---------------|-----------|-----
subjectIdentifier|String|||Yes||User specified Subject Identifier that is unique within study|Subject Identifier should NOT be prefixed with Site Identifier.|
siteId|Number|||Yes|||see [Sites](sites.md)
dob|ISO8601 Date||day before present day|Yes (if allowed by site)|||must be day before present day
gender|String|||Yes (if allowed by site)|<ul><li>Male</li><li>Female</li></ul>||Study/site shall be configured to utilize this field
weight|Number|1|2000|Yes (if allowed by site)|||Study/site shall be configured to utilize this field
weightUnit|String|||Yes (if allowed by site)|lbs, kg||
height|Number|1|300|Yes (if allowed by site)|||Study/site shall be configured to utilize this field
heightUnit|String|||Yes (if allowed by site)|cm, inches||
wearPosition|String|||Yes (if changes allowed by study)|<ul><li>Non-Dominant Wrist</li><li>Dominant Wrist</li><li>Left Non-Dominant Wrist</li><li>Left Dominant Wrist</li><li>Right Non-Dominant Wrist</li><li>Right Dominant Wrist</li><li>Waist</li><li>Left Wrist</li><li>Right Wrist</li><li>Ankle</li></ul>||Study/site shall be configured in order to utilize this field

**Additional Notes:**

- Depending on the study/site configuration of subject being added, the **gender**, **dob**, and/or **weight**, and/or **height** fields may or may not be allowed. If the fields are allowed, then they will be required. If not allowed, then these fields must be excluded from the JSON request.
- Depending on the study/site configuration of subject being added, the **wearPosition** may or may not be limited to only one of the following values:
  - Left Non-Dominant Wrist
  - Right Non-Dominant Wrist
  - Left Dominant Wrist
  - Right Dominant Wrist
  - Non-Dominant Wrist
  - Dominant Wrist
  - Left Wrist
  - Right Wrist
  - Waist
  - Ankle

**Response:**

201 Created

```json
{
    "id": 1234,
    "studyId": 1,
    "siteId": 2931,
    "siteIdentifier": "123",
    "subjectIdentifier": "TEST003",
    "dob": "1990-07-10",
    "gender": "Male",
    "timezone": "Africa/Abidjan",
    "wearPosition": "Left Wrist",
    "weight": 100,
    "weightUnit": "Lbs",
    "height": 200,
    "heightUnit": "cm",
    "assignmentStatus": "Not Assigned"
}
```

## Edit Subject

Modifies an existing subject.  List sites to find out which you can access. A 200 OK response is returned for a successfully edited subject.

**Request:**

```http
PUT /centrepoint/v3/Studies/{studyId}/Subjects/{subjectId}
Content-Type: application/json
{
    "subjectIdentifier": "string",
    "dob": "2019-07-10T18:56:43.609Z",
    "gender": "Male",
    "weight": 180,
    "weightUnit": "Lbs",
    "height": 200,
    "heightUnit": 'cm',
    "wearPosition": "Left Wrist",
    "changeReason": "string"
}
```

**Request Properties:**

Field|Type|Min|Max|Required|Accepted Values|Description|Notes
-----|----|---|---|--------|---------------|-----------|-----
subjectIdentifier|String|||Yes|||Unique within study
dob|ISO8601 Date||day before present day|Yes|||must be day before present day
gender|String|||Yes|<ul><li>Male</li><li>Female</li></ul>||Study/site shall be configured to utilize this field
weight|Number|1|1000|Yes|||Study/site shall be configured to utilize this field
weightUnit|String|||Yes|lbs or kg||Study/site shall be configured to utilize this field
height|Number|1|300|Yes (if allowed by site)|||Study/site shall be configured to utilize this field
heightUnit|String|||Yes (if allowed by site)|cm or inches||
wearPosition|String|||Yes|<ul><li>Non-Dominant Wrist</li><li>Dominant Wrist</li><li>Left Non-Dominant Wrist</li><li>Left Dominant Wrist</li><li>Right Non-Dominant Wrist</li><li>Right Dominant Wrist</li><li>Waist</li><li>Left Wrist</li><li>Right Wrist</li><li>Ankle</li></ul>||Study/site shall be configured to utilize this field
changeReason|String|||Yes|||Study/site shall be configured to utilize this field. Captured in operator audit record in accordance  with FDA 21 CFR Part 11.

**Additional Notes:**

- Depending on the study/site configuration of subject being edited, the **Gender**, **DOB**, and/or **Weight**, and/or **Height** fields may or may not be allowed. If the fields are allowed, then they will be required. If not allowed, then these fields must be excluded from the JSON request.
- Depending on the study/site configuration of subject being edited, the **WearPosition** may or may not limit to utilize only one of the following values:
  - Left Non-Dominant Wrist
  - Right Non-Dominant Wrist
  - Left Dominant Wrist
  - Right Dominant Wrist
  - Non-Dominant Wrist
  - Dominant Wrist
  - Left Wrist
  - Right Wrist
  - Waist
  - Ankle
- **changeReason** is required for all study configurations in CentrePoint.

**Response:**

200 OK

## Get Subject Milestones

Retrieves list of subject milestones

**Request:**

```http
GET /centrepoint/v3/Studies/{studyId}/Subjects/{subjectId}/milestones
```

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|**id**|Number|Subject Milestone ID|
|**name**|String|Name inherited from the Study Milestone|
|**subjectId**|Number|CentrePoint Subject ID (see [Subjects](subjects.md))|
|**studyMilestoneId**|Number|Study Milestone ID (see [Study Milestones](study_milestones.md))|
|**timestamp**|String (ISO8601 Date)|Timestamp of milestone in UTC|
|**timestampSubjectTZ**|String (ISO8601 Date)|Timestamp of milestone in subject's timezone|

```json
{
    "items": [
        {
            "id": 78,
            "name": "Visit 1",
            "subjectId": 596,
            "studyMilestoneId": 16,
            "timestamp": "2014-05-28T00:00:00Z",
            "timestampSubjectTZ": "2014-05-27T19:00:00-05:00"
        },
        {
            "id": 205,
            "name": "Visit 2",
            "subjectId": 596,
            "studyMilestoneId": 17,
            "timestamp": "2014-06-04T00:00:00Z",
            "timestampSubjectTZ": "2014-06-03T19:00:00-05:00"
        },
        {
            "id": 319,
            "name": "Visit 3",
            "subjectId": 596,
            "studyMilestoneId": 19,
            "timestamp": "2014-06-18T00:00:00Z",
            "timestampSubjectTZ": "2014-06-17T19:00:00-05:00"
        },
        {
            "id": 12856,
            "name": "Visit 4",
            "subjectId": 596,
            "studyMilestoneId": 20,
            "timestamp": "2017-09-02T04:59:59Z",
            "timestampSubjectTZ": "2017-09-01T23:59:59-05:00"
        }
    ],
    "links": {},
    "totalCount": 4,
    "limit": 100,
    "offset": 0
}
```

## Get Subject Timezone History

Retrieves list of subject timezone history entries

**Request:**

```http
GET /centrepoint/v3/Studies/{studyId}/Subjects/{subjectId}/TimezoneHistory
```

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|**subjectId**|Number|CentrePoint Subject ID (see [Subjects](subjects.md))|
|**timezone**|String|IANA timezone name|
|**effectiveDateUtc**|String (ISO8601 Date)|Timestamp of when the subject was placed in the timezone|

```json
{
    "items": [
        {
            "subjectId": 596,
            "timezone": "US/Central",
            "effectiveDateUtc": "2014-05-27T19:00:00Z"
        }
    ],
    "links": {},
    "totalCount": 1,
    "limit": 100,
    "offset": 0
}
```
