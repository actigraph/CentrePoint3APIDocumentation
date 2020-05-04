# Webhooks

**NOTE: These requests require the *CentrePoint* API scope. (see [Scopes](scopes.md))**

## CentrePoint WebHooks System

For more info on CentrePoint Webhooks System, visit https://github.com/actigraph/CentrePointWebhookDocumentation

## List Webhook Registrations

Retrieves a list of webhooks to which a study is subscribed.

**Request:**

```http
GET /centrepoint/v3/Studies/{studyId}/Webhooks
```

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|**id**|Number|Webhook Registration ID|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**url**|String (URL)|Webhook URL|
|**createdDate**|String (ISO8601 Date)|Date webhook registration was created|
|**isDisabled**|Boolean|Is webhook disabled|
|**webhookEvents**|Array([Webhook Event](webhook_events.md))|List of webhook events for which webhook is registered (see [Webhook Events](webhook_events.md))

## Get Webhook Registration by ID

Retrieves a webhook registration to which a study is subscribed.

**Request:**

```http
GET /centrepoint/v3/Studies/{studyId}/Webhooks/{webhookId}
```

**Response:**

|Field|Type|Description|
|-----|----|-----------|
|**id**|Number|Webhook Registration ID|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**url**|String (URL)|Webhook URL|
|**createdDate**|String (ISO8601 Date)|Date webhook registration was created|
|**isDisabled**|Boolean|Is webhook disabled|
|**webhookEvents**|Array([Webhook Event](webhook_events.md))|List of webhook events for which webhook is registered (see [Webhook Events](webhook_events.md))

## Webhooks History

Returns a history log of Webhook requests for a given study.

**Request:**

```http
GET /centrepoint/v3/Studies/{studyId}/Webhooks/{webhookId}/history
```

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

```json
{
    "items": [
      {
          "id": 34,
          "webhookId": 236,
          "webhookEventId": 4,
          "webhookEvent": "raw_processing_complete",
          "createdDate": "2019-06-03T20:41:01",
          "lastSentDate": "2019-06-03T20:41:01",
          "request": {
            "headers": "{\"Content-Type\":[\"application/json\"],\"User-Agent\":[\"ActiGraph-Hookshot/1.0\"],\"X-ActiGraph-Webhook-id\":[\"14\"],\"X-ActiGraph-Event\":[\"upload\"],\"X-ActiGraph-Delivery\":[\"0f9G3fde-8Baf-0c83-1591-517307kpp19c\"],\"X-Client-Cert-Used\":[\"false\"],\"Host\":[\"hostaddress.host.com\"],\"Content-Length\":[\"272\"],\"Expect\":[\"100-continue\"]}",
            "body": "{\"status\":\"completed\",\"firstEpochUTC\":\"2018-03-08T00:20:00.0000000\",\"firstEpochSubjectTZ\":\"2018-03-08T05:50:00.0000000\",\"lastEpochUTC\":\"2018-03-08T00:34:00.0000000\",\"lastEpochSubjectTZ\":\"2018-03-08T06:04:00.0000000\",\"uploadId\":\"362288\",\"studyId\":\"8\",\"subjectId\":\"2358\"}"
          },
          "response": {
            "responseCode": 200,
            "headers": "{\"Connection\":[\"keep-alive\"],\"Content-Length\":[\"0\"],\"Date\":[\"Thu, 08 Mar 2018 00:37:55 GMT\"],\"Server\":[\"Apache-Coyote/1.1\"]}",
            "body": ""
          }
      },
      {
          "id": 35,
          "webhookId": 236,
          "webhookEventId": 4,
          "webhookEvent": "raw_processing_complete",
          "createdDate": "2019-06-03T20:41:01",
          "lastSentDate": "2019-06-04T21:27:00",
          "errorMessage": "An error occurred while attempting to send a webhook message: Failed to resolve domain",
          "request": {
            "headers": "{\"Content-Type\":[\"application/json\"],\"User-Agent\":[\"ActiGraph-Hookshot/1.0\"],\"X-ActiGraph-Webhook-id\":[\"14\"],\"X-ActiGraph-Event\":[\"upload\"],\"X-ActiGraph-Delivery\":[\"0f9G3fde-8Baf-0c83-1591-517307kpp19c\"],\"X-Client-Cert-Used\":[\"false\"],\"Host\":[\"hostaddress.host.com\"],\"Content-Length\":[\"272\"],\"Expect\":[\"100-continue\"]}",
            "body": "{\"status\":\"completed\",\"firstEpochUTC\":\"2018-03-08T00:20:00.0000000\",\"firstEpochSubjectTZ\":\"2018-03-08T05:50:00.0000000\",\"lastEpochUTC\":\"2018-03-08T00:34:00.0000000\",\"lastEpochSubjectTZ\":\"2018-03-08T06:04:00.0000000\",\"uploadId\":\"362288\",\"studyId\":\"8\",\"subjectId\":\"2358\"}"
          }
      },
    ],
    "links": {},
    "totalCount": 1,
    "limit": 100,
    "offset": 0
}
```
