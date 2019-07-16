# Sites

**NOTE: These requests require the *CentrePoint* API scope. (see [Scopes](scopes.md))**

## List Sites

A list of sites you can access.

**Request:**

```http
GET /centrepoint/v1/Studies/{studyId}/Sites
```

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|id|Number|CentrePoint Site ID|
|studyId|Number|CentrePoint Study ID (see [Studies](studies.md))|
|siteName|String|Site Name|
|siteIdentifier|String|Unique site identifier (used as prefix to subject identifier)|
|Description|String|Site description

```json
{
    "items": [
        {
            "id": 2931,
            "studyId": 242,
            "siteName": "Default",
            "siteIdentifier": "123",
            "description": "This site was automatically generated when the study was created"
        },
        {
            "id": 2932,
            "studyId": 242,
            "siteName": "Test Site 2",
            "siteIdentifier": "999"
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
GET /centrepoint/v1/Studies/{studyId}/Sites/{siteId}
```

**Response:**

```json
{
    "id": 2931,
    "studyId": 242,
    "siteName": "Default",
    "siteIdentifier": "123",
    "description": "This site was automatically generated when the study was created"
}
```
