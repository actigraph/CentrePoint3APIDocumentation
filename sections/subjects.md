# Subjects

-----

**NOTE: These requests require the *CentrePoint* API scope. (see [Scopes](scopes.md))**

## List Study Subjects

Returns a list of all subjects within the requested study.

### Request

```http
GET /centrepoint/v1/Studies/{studyId}/Subjects
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
            "timezone": "(UTC +00:00) Africa/Abidjan",
            "wearPosition": "Left Wrist",
            "weight": 100.00,
            "weightUnit": "Lbs",
            "assignmentStatus": "Not Assigned"
        },
        {
            "id": 17911,
            "studyId": 242,
            "siteId": 2931,
            "siteIdentifier": "123",
            "subjectIdentifier": "TEST002",
            "dob": "1970-01-01",
            "gender": "Female",
            "timezone": "(UTC +00:00) Africa/Abidjan",
            "wearPosition": "Right Wrist",
            "weight": 176.37,
            "weightUnit": "Lbs",
            "assignmentStatus": "Not Assigned"
        }
    ],
    "links": {},
    "totalCount": 40,
    "limit": 100,
    "offset": 0
}
```

**Response Properties:**

Field|Type|Accepted Values|Description|Notes
-----|----|----------|-----|-----
id|Number||Primary Key of Subject Id||
siteIdentifier|String||User-specified Site Identifier that is unique within the study.|Used as a prefix to the subject identifier
subjectIdentifier|String||User-specified Subject Identifier that is unique within the study.|
dob|ISO8601 Date||Subject's Date of Birth||
gender|String|<ul><li>Male</li><li>Female</li></ul>|||
timezone|String||Subject's Timezone||
wearPosition|String|<ul><li>Non-Dominant Wrist</li><li>Dominant Wrist</li><li>Left Non-Dominant Wrist</li><li>Left Dominant Wrist</li><li>Right Non-Dominant Wrist</li><li>Right Dominant Wrist</li><li>Waist</li><li>Left Wrist</li><li>Right Wrist</li><li>Ankle</li></ul>|| 
Device Serial|String||The serial number of the activity monitor currently assigned to subject.|If subject is not assigned to a monitor, this field will be set to `null`.|

## Subject Details

Returns detailed information about the requested subject.

**Request:**

```http
GET /centrepoint/v1/Studies/{studyId}/Subjects/{subjectId}
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
    "timezone": "(UTC +00:00) Africa/Abidjan",
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
POST /centrepoint/v1/Studies/{studyId}/subjects
Content-Type: application/json
{
    "subjectIdentifier": "TEST003",
    "siteId": 2931,
    "dob": "1990-07-10",
    "gender": "Male",
    "weight": 100,
    "weightUnit": "Lbs",
    "wearPosition": "Left Wrist"
}
```

**Request Properties:**

Field|Type|Min|Max|Required|Accepted Values|Description|Notes
-----|----|---|---|--------|---------------|-----------|-----
subjectIdentifier|String|||Yes||User specified Subject Identifier that is unique within study|Subject Identifier should NOT be prefixed with Site Identifier.|
siteId|Number|||Yes|||
dob|ISO8601 Date||day before present day|Yes (if allowed by site)|||must be day before present day
gender|String|||Yes (if allowed by site)|<ul><li>Male</li><li>Female</li></ul>||Study/site shall be configured to utilize this field
weight|Number|1|2000|Yes (if allowed by site)|||Study/site shall be configured to utilize this field
weightUnit|String|||Yes (if allowed by site)|lbs, kg||
wearPosition|String|||Yes (if changes allowed by study)|<ul><li>Non-Dominant Wrist</li><li>Dominant Wrist</li><li>Left Non-Dominant Wrist</li><li>Left Dominant Wrist</li><li>Right Non-Dominant Wrist</li><li>Right Dominant Wrist</li><li>Waist</li><li>Left Wrist</li><li>Right Wrist</li><li>Ankle</li></ul>||Study/site shall be configured in order to utilize this field

**Additional Notes:**

- Depending on the study/site configuration of subject being added, the **gender**, **dob**, and/or **weight** fields may or may not be allowed. If the fields are allowed, then they will be required. If not allowed, then these fields must be excluded from the JSON request.
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
    "timezone": "string",
    "wearPosition": "Left Wrist",
    "weight": 100,
    "weightUnit": "Lbs",
    "assignmentStatus": "Not Assigned"
}
```

## Edit Subject

Modifies an existing subject.  List sites to find out which you can access. A 200 OK response is returned for a successfully edited subject.

**Request:**

```http
PUT /centrepoint/v1/subjects
Content-Type: application/json
{
    "subjectIdentifier": "string",
    "dob": "2019-07-10T18:56:43.609Z",
    "gender": "Male",
    "weight": 0,
    "weightUnit": "Lbs",
    "wearPosition": "Left Wrist",
    "changeReason": "string"
}
```

**Request Properties:**

Field|Type|Min|Max|Required|Accepted Values|Description|Notes
-----|----|---|---|--------|---------------|-----------|-----
dob|ISO8601 Date||day before present day|Yes|||must be day before present day
gender|String|||Yes|<ul><li>Male</li><li>Female</li></ul>||Study/site shall be configured to utilize this field
siteId|Number|||Yes|||Site write access enforced
subjectId|Number|||Yes|||Site write access enforced
subjectIdentifier|String|||Yes|||Unique within study
wearPosition|String|||Yes|<ul><li>Non-Dominant Wrist</li><li>Dominant Wrist</li><li>Left Non-Dominant Wrist</li><li>Left Dominant Wrist</li><li>Right Non-Dominant Wrist</li><li>Right Dominant Wrist</li><li>Waist</li><li>Left Wrist</li><li>Right Wrist</li><li>Ankle</li></ul>||Study/site shall be configured to utilize this field
weight|Number|1|2000|Yes|||Study/site shall be configured to utilize this field
changeReason|String|||Yes|||Study/site shall be configured to utilize this field. Captured in operator audit record in accordance  with FDA 21 CFR Part 11.

**Additional Notes:**

- Depending on the study/site configuration of subject being edited, the **Gender**, **DOB**, and/or **Weight** fields may or may not be allowed. If the fields are allowed, then they will be required. If not allowed, then these fields must be excluded from the JSON request.
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
GET /centrepoint/v1/Studies/{studyId}/Subjects/{subjectId}/milestones
Content-Type: application/json
{
    "subjectIdentifier": "string",
    "dob": "2019-07-10T18:56:43.609Z",
    "gender": "Male",
    "weight": 0,
    "weightUnit": "Lbs",
    "wearPosition": "Left Wrist",
    "changeReason": "string"
}
```

**Request Properties:**

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Description|
|-----|-----------|
|**id**|Subject Milestone ID|
|**subjectId**|CentrePoint Subject ID (see [Subjects](subjects.md))|
|**studyMilestoneId**|Study Milestone ID (see [Study Milestones](study_milestones.md))|
|**timestamp**|Timestamp of milestone in UTC|
|**timestampSubjectTZ**|Timestamp of milestone in subject's timezone|

```json
{
    "items": [
        {
            "id": 78,
            "subjectId": 596,
            "studyMilestoneId": 16,
            "timestamp": "2014-05-28T00:00:00Z",
            "timestampSubjectTZ": "2014-05-27T19:00:00-05:00"
        },
        {
            "id": 205,
            "subjectId": 596,
            "studyMilestoneId": 17,
            "timestamp": "2014-06-04T00:00:00Z",
            "timestampSubjectTZ": "2014-06-03T19:00:00-05:00"
        },
        {
            "id": 319,
            "subjectId": 596,
            "studyMilestoneId": 19,
            "timestamp": "2014-06-18T00:00:00Z",
            "timestampSubjectTZ": "2014-06-17T19:00:00-05:00"
        },
        {
            "id": 12856,
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
