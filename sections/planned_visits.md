# Planned Visits

**NOTE: These requests require the *CentrePoint* API scope. (see [Scopes](scopes.md))**

## List Planned Visits

Returns the visit version, status and the list of planned visits in that visit version for a study.

**Request:**

```http
GET /centrepoint/v3/Studies/{studyId}/ActualVisitFiles/PlannedVisits
```

**Response:**

|Field|Type|Description|
|-----|----|-----------|
|**version**|Number|Study Visit Version|
|**status**|String|Status of the Visit Version. Locked/CheckedOut|
|**studyPlannedVisits**|List|List of planned visits in the study version|

For he fields in each item of studyPlannedVisits, refer below table.

|Field|Type|Nullable|Description|
|-----|----|--------|-----------|
|**studyPlannedVisitId**|Number|No|Study Planned Visit Id|
|**verFrom**|Number|No|The first version where this planned visit is available|
|**verTo**|Number|No|The last version until which this planned visit is available|
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
            "verFrom": 1,
            "verTo": 2147483647,
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
            "verFrom": 1,
            "verTo": 2147483647,
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
            "verFrom": 1,
            "verTo": 2147483647,
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
            "verFrom": 1,
            "verTo": 2147483647,
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
            "verFrom": 1,
            "verTo": 2147483647,
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
            "verFrom": 1,
            "verTo": 2147483647,
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
            "verFrom": 2,
            "verTo": 2147483647,
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
            "verFrom": 6,
            "verTo": 2147483647,
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
|**visitversion**|Number|When specified, returns planned visits for that version|latest locked version for the study|
|**includewearonly**|Boolean|When true, returns only the wear visits|false|

**Example Filtered Request:**

```http
GET /centrepoint/v3/Studies/{studyId}/ActualVisitFiles/PlannedVisits?visitversion=6&includewearonly=true
```

**Response:**

```json
{
    "version": 6,
    "status": "Locked",
    "studyPlannedVisits": [
        {
            "studyPlannedVisitId": 64,
            "verFrom": 1,
            "verTo": 2147483647,
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
            "verFrom": 1,
            "verTo": 2147483647,
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
            "verFrom": 1,
            "verTo": 2147483647,
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
            "verFrom": 1,
            "verTo": 2147483647,
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
            "verFrom": 1,
            "verTo": 2147483647,
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
            "verFrom": 1,
            "verTo": 2147483647,
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
            "verFrom": 2,
            "verTo": 2147483647,
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
