# Visits

**NOTE: These requests require the *CentrePoint* API scope. (see [Scopes](scopes.md))**

## List Planned Visits

Returns the visit version, status and the list of planned visits in that visit version for a study.

**Request:**

```http
GET /centrepoint/v3/Studies/{studyId}/Visits/PlannedVisits
```

**Response:**

|Field|Type|Description|
|-----|----|-----------|
|**version**|Number|Study Visit Version|
|**status**|String|Status of the Visit Version. Locked/CheckedOut|
|**studyPlannedVisits**|List|List of planned visits in the study version|

For the fields in each item of studyPlannedVisits, refer to the below table.
The items are ordered by Study Planned Visit Id and the sort order is ascending.

|Field|Type|Nullable|Description|
|-----|----|--------|-----------|
|**studyPlannedVisitId**|Number|No|Study Planned Visit Id|
|**studyId**|Number|No|Study Id|
|**visitName**|String|No|Visit Name|
|**visitDay**|Number|No|Visit Day|
|**visitWearPeriodName**|String|Yes|Wear Period Name for the visit|
|**earliestOffsetVisitStart**|Number|Yes|Earlist Offset to start the visit|
|**latestOffsetVisitStart**|Number|Yes|Latest Offset to start the visit|
|**plannedWearPeriodDuration**|Number|Yes|No. of days planned for wearing the device|
|**actualVisitWindowOffset**|Number|Yes|Offset for the day from which the subject needs to start wearing the device|
|**minimumVisitWearPeriodCompliance**|Number|Yes|Minimum no. of days for which the subject needs to wear the device|

```json
{
    "version": 6,
    "status": "Locked",
    "studyPlannedVisits": [
        {
            "studyPlannedVisitId": 64,
            "studyId": 1608,
            "visitName": "Visit1",
            "visitDay": 1,
            "visitWearPeriodName": "WearPeriod1",
            "earliestOffsetVisitStart": 1,
            "latestOffsetVisitStart": 1,
            "plannedWearPeriodDuration": 7,
            "actualVisitWindowOffset": 0,
            "minimumVisitWearPeriodCompliance": 3
        },
        {
            "studyPlannedVisitId": 65,
            "studyId": 1608,
            "visitName": "Visit2",
            "visitDay": 11,
            "visitWearPeriodName": "WearPeriod2",
            "earliestOffsetVisitStart": 1,
            "latestOffsetVisitStart": 1,
            "plannedWearPeriodDuration": 14,
            "actualVisitWindowOffset": 0,
            "minimumVisitWearPeriodCompliance": 3
        },
        {
            "studyPlannedVisitId": 66,
            "studyId": 1608,
            "visitName": "Visit3",
            "visitDay": 21,
            "visitWearPeriodName": "WearPeriod3",
            "earliestOffsetVisitStart": 1,
            "latestOffsetVisitStart": 1,
            "plannedWearPeriodDuration": 7,
            "actualVisitWindowOffset": 0,
            "minimumVisitWearPeriodCompliance": 3
        },
        {
            "studyPlannedVisitId": 67,
            "studyId": 1608,
            "visitName": "Visit4",
            "visitDay": 35,
            "visitWearPeriodName": "WearPeriod4",
            "earliestOffsetVisitStart": 1,
            "latestOffsetVisitStart": 1,
            "plannedWearPeriodDuration": 7,
            "actualVisitWindowOffset": -6,
            "minimumVisitWearPeriodCompliance": 3
        },
        {
            "studyPlannedVisitId": 68,
            "studyId": 1608,
            "visitName": "Visit5",
            "visitDay": 39,
            "visitWearPeriodName": "WearPeriod5",
            "earliestOffsetVisitStart": 1,
            "latestOffsetVisitStart": 1,
            "plannedWearPeriodDuration": 7,
            "actualVisitWindowOffset": -6,
            "minimumVisitWearPeriodCompliance": 3
        },
        {
            "studyPlannedVisitId": 69,
            "studyId": 1608,
            "visitName": "Visit6",
            "visitDay": 49,
            "visitWearPeriodName": "WearPeriod6",
            "earliestOffsetVisitStart": 1,
            "latestOffsetVisitStart": 1,
            "plannedWearPeriodDuration": 7,
            "actualVisitWindowOffset": 0,
            "minimumVisitWearPeriodCompliance": 3
        },
        {
            "studyPlannedVisitId": 70,
            "studyId": 1608,
            "visitName": "Visit7",
            "visitDay": 58,
            "visitWearPeriodName": "WearPeriod7",
            "earliestOffsetVisitStart": 1,
            "latestOffsetVisitStart": 1,
            "plannedWearPeriodDuration": 7,
            "actualVisitWindowOffset": -6,
            "minimumVisitWearPeriodCompliance": 3
        },
        {
            "studyPlannedVisitId": 250,
            "studyId": 1608,
            "visitName": "Visit8",
            "visitDay": 60
        }
    ]
}
```

**Query Parameters:**

Query parameters include opional filters that can be applied to narrow the search for planned visits.

|Field|Type|Description|Default Value|
|-----|----|-----------|-------------|
|**visitversion**|Number|When specified, returns planned visits for that version|Latest locked version for the study|
|**includewearonly**|Boolean|When true, returns only the wear visits|false|

**Example Filtered Request:**

```http
GET /centrepoint/v3/Studies/{studyId}/Visits/PlannedVisits?visitversion=6&includewearonly=true
```

**Response:**

```json
{
    "version": 6,
    "status": "Locked",
    "studyPlannedVisits": [
        {
            "studyPlannedVisitId": 64,
            "studyId": 1608,
            "visitName": "Visit1",
            "visitDay": 1,
            "visitWearPeriodName": "WearPeriod1",
            "earliestOffsetVisitStart": 1,
            "latestOffsetVisitStart": 1,
            "plannedWearPeriodDuration": 7,
            "actualVisitWindowOffset": 0,
            "minimumVisitWearPeriodCompliance": 3
        },
        {
            "studyPlannedVisitId": 65,
            "studyId": 1608,
            "visitName": "Visit2",
            "visitDay": 11,
            "visitWearPeriodName": "WearPeriod2",
            "earliestOffsetVisitStart": 1,
            "latestOffsetVisitStart": 1,
            "plannedWearPeriodDuration": 14,
            "actualVisitWindowOffset": 0,
            "minimumVisitWearPeriodCompliance": 3
        },
        {
            "studyPlannedVisitId": 66,
            "studyId": 1608,
            "visitName": "Visit3",
            "visitDay": 21,
            "visitWearPeriodName": "WearPeriod3",
            "earliestOffsetVisitStart": 1,
            "latestOffsetVisitStart": 1,
            "plannedWearPeriodDuration": 7,
            "actualVisitWindowOffset": 0,
            "minimumVisitWearPeriodCompliance": 3
        },
        {
            "studyPlannedVisitId": 67,
            "studyId": 1608,
            "visitName": "Visit4",
            "visitDay": 35,
            "visitWearPeriodName": "WearPeriod4",
            "earliestOffsetVisitStart": 1,
            "latestOffsetVisitStart": 1,
            "plannedWearPeriodDuration": 7,
            "actualVisitWindowOffset": -6,
            "minimumVisitWearPeriodCompliance": 3
        },
        {
            "studyPlannedVisitId": 68,
            "studyId": 1608,
            "visitName": "Visit5",
            "visitDay": 39,
            "visitWearPeriodName": "WearPeriod5",
            "earliestOffsetVisitStart": 1,
            "latestOffsetVisitStart": 1,
            "plannedWearPeriodDuration": 7,
            "actualVisitWindowOffset": -6,
            "minimumVisitWearPeriodCompliance": 3
        },
        {
            "studyPlannedVisitId": 69,
            "studyId": 1608,
            "visitName": "Visit6",
            "visitDay": 49,
            "visitWearPeriodName": "WearPeriod6",
            "earliestOffsetVisitStart": 1,
            "latestOffsetVisitStart": 1,
            "plannedWearPeriodDuration": 7,
            "actualVisitWindowOffset": 0,
            "minimumVisitWearPeriodCompliance": 3
        },
        {
            "studyPlannedVisitId": 70,
            "studyId": 1608,
            "visitName": "Visit7",
            "visitDay": 58,
            "visitWearPeriodName": "WearPeriod7",
            "earliestOffsetVisitStart": 1,
            "latestOffsetVisitStart": 1,
            "plannedWearPeriodDuration": 7,
            "actualVisitWindowOffset": -6,
            "minimumVisitWearPeriodCompliance": 3
        }
    ]
}
```

## List Actual Visits

Returns a list of actual visits in the study.

### Request

```http
GET /centrepoint/v3/Studies/{studyId}/Visits/ActualVisits
```

### Response

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.
The items are ordered by Subject Id and then by Visit Date and the sort order is ascending.

|Field|Type|Description|
|-----|----|-----------|
|**actualVisitId**|Number|Actual Visit Id|
|**subjectId**|Number|Subject Id|
|**visitId**|Number|Study Planned Visit Id|
|**visitName**|String|Visit Name|
|**visitDate**|Date|Visit Date|
|**wearPeriod**|Object|Wear Period for the visit. If wear period is not available, it will be null|

For the fields in wearPeriod, refer to the below table.

|Field|Type|Description|
|-----|----|-----------|
|**wearPeriodId**|Number|Wear Period Id|
|**wearPeriodName**|String|Wear Period Name|
|**wearPeriodStartDate**|Date|Wear Period Start Date|
|**wearPeriodEndDate**|Date|Wear Period End Date|

```json
{
    "items": [
        {
            "actualVisitId": 7077,
            "subjectId": 13984,
            "visitId": 64,
            "visitName": "Visit1",
            "visitDate": "2024-06-14",
            "wearPeriod": {
                "wearPeriodId": 164357,
                "wearPeriodName": "WearPeriod1",
                "wearPeriodStartDate": "2024-06-14",
                "wearPeriodEndDate": "2024-06-20"
            }
        },
        {
            "actualVisitId": 7078,
            "subjectId": 13984,
            "visitId": 65,
            "visitName": "Visit2",
            "visitDate": "2024-06-24"
        }
    ],
    "links": {},
    "totalCount": 7,
    "limit": 100,
    "offset": 0
}
```

**Query Parameters:**

Query parameters include filters that can be applied to narrow the search for actual visits.

|Field|Type|Description|Default Value|
|-----|----|-----------|-------------|
|**SubjectId**|Number|When not null, visits are filtered for the subject|null|
|**StartDate**|Date|When not null, the visits will be filtered by start date|null|
|**EndDate**|Date|When not null, the visits will be filtered by end date|null|

**Example Filtered Request:**

```http
GET /centrepoint/v3/Studies/{studyId}/Visits/ActualVisits?SubjectId=13984&StartDate=2024-06-13&EndDate=2024-06-24
```

**Response:**

```json
{
    "items": [
        {
            "actualVisitId": 7077,
            "subjectId": 13984,
            "visitId": 64,
            "visitName": "Visit1",
            "visitDate": "2024-06-14",
            "wearPeriod": {
                "wearPeriodId": 164357,
                "wearPeriodName": "WearPeriod1",
                "wearPeriodStartDate": "2024-06-14",
                "wearPeriodEndDate": "2024-06-20"
            }
        },
        {
            "actualVisitId": 7078,
            "subjectId": 13984,
            "visitId": 65,
            "visitName": "Visit2",
            "visitDate": "2024-06-24",
            "wearPeriod": {
                "wearPeriodId": 164358,
                "wearPeriodName": "WearPeriod2",
                "wearPeriodStartDate": "2024-06-24",
                "wearPeriodEndDate": "2024-07-03"
            }
        }
    ],
    "links": {},
    "totalCount": 2,
    "limit": 100,
    "offset": 0
}
```
