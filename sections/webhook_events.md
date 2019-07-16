# Webhook Events

**NOTE: These requests require the *CentrePoint* API scope. (see [Scopes](scopes.md))**

## List Webhook Events

Returns a list of webhook events to which you can subscribe.

### Request

```http
GET /centrepoint/v1/WebhookEvents
```

### Response

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|**id**|Number|CentrePoint Webhook Event ID|
|**name**|String|Webhook Event Name|
|**description**|String|Webhook Event Description|

```json
{
    "items": [
        {
            "id": 4,
            "name": "data_retrieval_complete",
            "description": "Data retrieval completed"
        },
        {
            "id": 5,
            "name": "raw_processing_complete",
            "description": "Raw data processing is complete"
        },
        {
            "id": 3,
            "name": "upload",
            "description": "All events relating to uploads, such as started, completed and error"
        }
    ],
    "links": {},
    "totalCount": 3,
    "limit": 100,
    "offset": 0
}
```
