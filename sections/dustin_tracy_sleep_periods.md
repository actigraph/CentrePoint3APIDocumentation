# Dustin Tracy Sleep Periods

**NOTE: These requests require the *Analytics* API scope. (see [Scopes](scopes.md))**

## List Study Dustin Tracy Sleep Periods

Returns a list of Dustin Tracy Sleep Periods within the requested study.

**Request:**

```http
GET /analytics/v3/Studies/{studyId}/Subjects/{subjectId}/DustinTracySleepPeriods
```

**Query Options**

|Field|Type|Description|
|-----|----|-----------|
|**algorithmSettingId**|String (GUID)|GUID of the Settings Used To Create the Dustin Tracy Sleep Periods|
|**subjectId**|Number|CentrePoint Subject ID (see [Subjects](subjects.md))|
|**fromDate**|String (ISO8601 Date)|Starting Date for the Dustin Tracy Sleep Periods Query (Inclusive)|
|**toDate**|String (ISO8601 Date)|Ending Date for the Dustin Tracy Sleep Periods Query (Inclusive)|

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|**id**|Number|Dustin Tracy Sleep Period ID|
|**subjectId**|Number|CentrePoint Subject ID (see [Subjects](subjects.md))|
|**activityMonitorSerial**|Number|The Monitor Used to Collect the Data for the Sleep Period|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**algorithmSettingId**|GUID of the Settings Used To Create the Dustin Tracy Sleep Period|
|**inBedTime**|String (ISO8601 Date)|Start of the Sleep Period|
|**outBedTime**|String (ISO8601 Date)|End of the Sleep Period|
|**durationMinutes**|Number|Total number of minutes in the sleep period|
|**timeAsleepMinutes**|Number|The number of minutes marked as awake between Begin Time and End Time|
|**timeAwakeMinutes**|Number|Number of minutes marked asleep in the sleep period|
|**awakeningCount**|Number|Number of awakening periods during the sleep period|
|**averageAwakening**|Number|Average of the Awakening times (Time Awake / Awakening Count)|
|**totalCounts**|Number|Sum of the Vertical axis counts for each epoch in the sleep period|
|**efficiency**|Number|Ratio between sleep and total time.(Sleep Time/Duration)|
|**wakeAfterOnsetMinutes**|Number|The number of minutes marked as awake between Onset and End Time|
|**sleepFragmentationIndex**|Number|Percentage (between 0 - 1) of sleep periods with only one epoch|
|**sleepMovementIndex**|Number|Percentage (between 0 - 1) of epochs with movement |
|**totalSleepFragmentationIndex**|Number|Addition of MovementIndex and FragmentationIndex|

**Response Example:**

```json
{
    "items": [
        {
            "id": 94,
            "studyId": 2196,
            "algorithmSettingId": "c4fee8c1-9fec-ea11-af8c-000d3a102b0e",
            "subjectId": 21670,
            "inBedTime": "2020-05-15T15:15:00+00:00",
            "outBedTime": "2020-05-15T15:28:00+00:00",
            "activityMonitorSerial": "CPW1A00000001",
            "durationMinutes": 13,
            "timeAsleepMinutes": 6.00,
            "timeAwakeMinutes": 7.00,
            "awakeningCount": 1,
            "averageAwakening": 7.0,
            "totalCounts": 3128,
            "efficiency": 0.46153846153846156,
            "wakeAfterOnsetMinutes": 7.0,
            "sleepFragmentationIndex": 0.5,
            "sleepMovementIndex": 0.38461538461538464,
            "totalSleepFragmentationIndex": 0.8846153846153846
        },
        {
            "id": 150,
            "studyId": 2196,
            "algorithmSettingId": "71c68872-edec-ea11-af8c-000d3a102b0e",
            "subjectId": 21670,
            "inBedTime": "2020-05-15T15:15:00+00:00",
            "outBedTime": "2020-05-15T15:28:00+00:00",
            "activityMonitorSerial": "CPW1A00000001",
            "durationMinutes": 13,
            "timeAsleepMinutes": 6.00,
            "timeAwakeMinutes": 7.00,
            "awakeningCount": 1,
            "averageAwakening": 7.0,
            "totalCounts": 3128,
            "efficiency": 0.46153846153846156,
            "wakeAfterOnsetMinutes": 7.0,
            "sleepFragmentationIndex": 0.5,
            "sleepMovementIndex": 0.38461538461538464,
            "totalSleepFragmentationIndex": 0.8846153846153846
        },
        ...
        {
            "id": 1506,
            "studyId": 2196,
            "algorithmSettingId": "4f48945c-4005-eb11-96f5-000d3a102a21",
            "subjectId": 21670,
            "inBedTime": "2020-05-16T01:52:00+00:00",
            "outBedTime": "2020-05-16T12:59:00+00:00",
            "activityMonitorSerial": "CPW1A00000001",
            "durationMinutes": 667,
            "timeAsleepMinutes": 578.00,
            "timeAwakeMinutes": 89.00,
            "awakeningCount": 13,
            "averageAwakening": 6.846153846153846,
            "totalCounts": 46919,
            "efficiency": 0.8665667166416792,
            "wakeAfterOnsetMinutes": 89.0,
            "sleepFragmentationIndex": 0.0,
            "sleepMovementIndex": 0.2698650674662669,
            "totalSleepFragmentationIndex": 0.2698650674662669
        }
    ],
    "links": {},
    "totalCount": 84,
    "limit": 100,
    "offset": 0
}
```


## List Study Dustin Tracy Sleep Period Settings

Returns a list of Dustin Tracy Sleep Period Settings within the requested study.

**Request:**

```http
GET /analytics/v3/Studies/{studyId}/DustinTracySleepPeriodSettings
```

**Query Options**

|Field|Type|Description|
|-----|----|-----------|
|**ids**|String Array of GUIDs|GUIDs of the Dustin Tracy Sleep Period Settings|

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|**id**|String (GUID)|Dustin Tracy Sleep Period Setting ID|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**name**|String|The Custom Name of the Dustin Tracy Sleep Period Setting Setting|
|**algorithmType**|String|The Algorithm Type for the Setting|
|**settings**|Object (See *DustinTracySettingsDetail* below)|The Details of the Settings Used to Generate the Sleep Periods|

*DustinTracySettingsDetail*

|Field|Type|Description|
|-----|----|-----------|
|**blockLengthInMinutes**|Number|The time span in minutes for epochs to be placed in a block|
|**thresholdCountsPerMinute**|Number|Value (counts/min) for which block averages falling below or rising above were assumed to represent a transition from wake to bedrest or from bedrest to wake|
|**bedRestStartTriggerCountsPerMinute**|Number|Minimum number of counts/min required in any two consecutive 1-min epochs to be marked as wake end|
|**bedRestEndTriggerCountsPerMinute**|Number|Minimum number of counts/min allowed in any two consecutive 1-min epochs to be marked as bedrest end|
|**minimumBedRestLengthInMinutes**|Number|Minimum time minutes for valid bed rest/sleep period|
|**maxSleepPeriodLengthInMinutes**|Number|Maximum time minutes for valid bed rest/sleep period|
|**minimumNonZeroEpochs**|Number|Minimum amount of non-zero epochs for a sleep period|

**Response Example:**

```json
{
    "items": [
        {
            "id": "ead14cd0-c903-eb11-96f5-000d3a102a21",
            "studyId": 2196,
            "name": "Dustin Tracy Sleep Periods - Adult Wrist-Worn",
            "algorithmType": "Dustin Tracy Sleep Periods",
            "settings": {
                "blockLengthInMinutes": 45,
                "thresholdCountsPerMinute": 400,
                "bedRestStartTriggerCountsPerMinute": 400,
                "bedRestEndTriggerCountsPerMinute": 1500,
                "minimumBedRestLengthInMinutes": 60,
                "maxSleepPeriodLengthInMinutes": 1440
            }
        },
        {
            "id": "efd14cd0-c903-eb11-96f5-000d3a102a21",
            "studyId": 2196,
            "name": "Dustin Tracy Sleep Periods - Youth/Adolescent Wrist-Worn",
            "algorithmType": "Dustin Tracy Sleep Periods",
            "settings": {
                "blockLengthInMinutes": 60,
                "thresholdCountsPerMinute": 250,
                "bedRestStartTriggerCountsPerMinute": 50,
                "bedRestEndTriggerCountsPerMinute": 3000,
                "minimumBedRestLengthInMinutes": 60,
                "maxSleepPeriodLengthInMinutes": 1440
            }
        }
    ],
    "links": {},
    "totalCount": 2,
    "limit": 100,
    "offset": 0
}
```


## Retrieve Dustin Tracy Sleep Period Setting

Returns a single Dustin Tracy Sleep Period Setting Setting by ID within the requested study.

**Request:**

```http
GET /analytics/v3/Studies/{studyId}/DustinTracySleepPeriodSettings/{dustinTracySleepPeriodSettingId}
```

**Response:**

|Field|Type|Description|
|-----|----|-----------|
|**id**|String (GUID)|Dustin Tracy Sleep Period Setting ID|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**name**|String|The Custom Name of the Dustin Tracy Sleep Period Setting Setting|
|**algorithmType**|String|The Algorithm Type for the Setting|
|**settings**|Object (See *DustinTracySettingsDetail* below)|The Details of the Settings Used to Generate the Sleep Periods|

*DustinTracySettingsDetail*

|Field|Type|Description|
|-----|----|-----------|
|**blockLengthInMinutes**|Number|The time span in minutes for epochs to be placed in a block|
|**thresholdCountsPerMinute**|Number|Value (counts/min) for which block averages falling below or rising above were assumed to represent a transition from wake to bedrest or from bedrest to wake|
|**bedRestStartTriggerCountsPerMinute**|Number|Minimum number of counts/min required in any two consecutive 1-min epochs to be marked as wake end|
|**bedRestEndTriggerCountsPerMinute**|Number|Minimum number of counts/min allowed in any two consecutive 1-min epochs to be marked as bedrest end|
|**minimumBedRestLengthInMinutes**|Number|Minimum time minutes for valid bed rest/sleep period|
|**maxSleepPeriodLengthInMinutes**|Number|Maximum time minutes for valid bed rest/sleep period|
|**minimumNonZeroEpochs**|Number|Minimum amount of non-zero epochs for a sleep period|

**Response Example:**

```json
{
    "id": "ead14cd0-c903-eb11-96f5-000d3a102a21",
    "studyId": 2196,
    "name": "Dustin Tracy Sleep Periods - Adult Wrist-Worn",
    "algorithmType": "Dustin Tracy Sleep Periods",
    "settings": {
        "blockLengthInMinutes": 45,
        "thresholdCountsPerMinute": 400,
        "bedRestStartTriggerCountsPerMinute": 400,
        "bedRestEndTriggerCountsPerMinute": 1500,
        "minimumBedRestLengthInMinutes": 60,
        "maxSleepPeriodLengthInMinutes": 1440
    }
}
```