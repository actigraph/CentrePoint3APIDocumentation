# Sites

**NOTE: These requests require the *CentrePoint* API scope. (see [Scopes](scopes.md))**

## List Sites

A list of sites you can access.

**Request:**

```http
GET /centrepoint/v3/Studies/{studyId}/Sites
```

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|id|Number|CentrePoint Site ID|
|studyId|Number|CentrePoint Study ID (see [Studies](studies.md))|
|siteName|String|Site Name|
|siteIdentifier|String|Unique site identifier (used as prefix to subject identifier)|
|description|String|Site description|
|requireDob|Boolean|Indicates if subject date of birth is required based on study/site configuration|
|requireGender|Boolean|Indicates if subject gender is required based on study/site configuration|
|requireWeight|Boolean|Indicates if subject weight is required based on study/site configuration|
|requireHeight|Boolean|Indicates if subject height is required based on study/site configuration|
|defaultShipmentCountryCode|String|Default shipment country code for site|
|depot|Boolean|Indicates if selected site is Depot or not|

```json
{
    "items": [
        {
            "id": 2931,
            "studyId": 242,
            "siteName": "Default",
            "siteIdentifier": "123",
            "description": "This site was automatically generated when the study was created",
            "requireDob": true,
            "requireGender": true,
            "requireWeight": true,
            "requireHeight": true,
            "defaultShipmentCountryCode": "USA",
            "depot": true
        },
        {
            "id": 2932,
            "studyId": 242,
            "siteName": "Test Site 2",
            "siteIdentifier": "999",
            "requireDob": false,
            "requireGender": false,
            "requireWeight": false,
            "requireHeight": false,
            "defaultShipmentCountryCode": "PRI",
            "depot": false
        }
    ],
    "links": {},
    "totalCount": 2,
    "limit": 100,
    "offset": 0
}
```

## Get Site by ID

Retrieves site details by ID.

**Request:**

```http
GET /centrepoint/v3/Studies/{studyId}/Sites/{siteId}
```

**Response:**

```json
{
    "id": 2931,
    "studyId": 242,
    "siteName": "Default",
    "siteIdentifier": "123",
    "description": "This site was automatically generated when the study was created",
    "requireDob": true,
    "requireGender": true,
    "requireWeight": true,
    "requireHeight": true,
    "defaultShipmentCountryCode": "USA",
    "depot": true
}
```
