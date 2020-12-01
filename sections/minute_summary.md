# Minute Summary

**NOTE: These requests require the *Analytics* API scope. (see [Scopes](scopes.md))**

## Retrieve Minute Summary Data For Subject

Returns a list of Minute Summaries within the requested study.

**Request:**

```http
GET /analytics/v3/Studies/{studyId}/Subjects/{subjectId}/MinuteSummaries
```

**Query Options**

|Field|Type|Description|
|-----|----|-----------|
|**subjectId**|Number|CentrePoint Subject ID (see [Subjects](subjects.md))|
|**fromDate**|String (ISO8601 Date)|Starting Date for the Minute Summary Query (Inclusive)|
|**toDate**|String (ISO8601 Date)|Ending Date for the Minute Summary Query (Inclusive)|

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|**subjectId**|Number|CentrePoint Subject ID (see [Subjects](subjects.md))|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**activityMonitorSerial**|String|Activity Monitor Used During the Minute|
|**minuteSummarySettingsId**|String (GUID)|The ID of the Minute Summary Setting Used to Create The Minute Summary|
|**TimestampUtc**|String (ISO8601 Date)|The Timestamp for the Minute Summary|
|**isWear**|Boolean|Indicates Whether or Not This Minute Was During a Wear Period|
|**isSleep**|Boolean|Indicates Whether or Not This Minute Was During a Sleep Period|
|**x**|Number|X Axis Count Summary|
|**y**|Number|Y Axis Count Summary|
|**z**|Number|Z Axis Count Summary|
|**vectorMagnitude**|Number|Vector Magnitude Summary|
|**steps**|Number|The Number of Steps in the Minute (Only present if steps were calculated)|
|**longPressCounts**|Number|The Number of Long Press Event Markers in the Minute (Only present if Event Markers were collected)|
|**pressCounts**|Number|The Number of Press Event Markers in the Minute (Only present if Event Markers were collected)|
|**mets**|Number|The METs calculation for the Minute (Only present if METs/Calories were collected)|
|**calories**|Number|The Number of Calories burned in the Minute (Only present if METs/Calories were collected)|
|**crouterCutPointsMinuteAggregations**|Object Array (See *CrouterCutPointsMinuteAggregation* below)|The Total Crouter Cutpoint Classifications in the Minute|
|**freedsonCutPointsMinuteAggregations**|Object Array (See *FreedsonCutPointsMinuteAggregation* below)|The Total Freedson Cutpoint Classifications in the Minute|
|**evensonCutPointsMinuteAggregations**|Object Array (See *EvensonCutPointsMinuteAggregation* below)|The Total Evenson Cutpoint Classifications in the Minute|
|**staudenmayerCutPointsMinuteAggregations**|Object Array (See *StaudenmayerCutPointsMinuteAggregation* below)|The Total Staudenmayer Cutpoint Classifications in the Minute|

*CrouterCutPointsMinuteAggregation*

|Name|Type|Description|
|:---|:---|:----------|
|**vmSedentary**|Number|A minute aggregate in seconds where the Crouter VM Activity Intensity Cut Point is “Sedentary”|
|**vmLight**|Number|A minute aggregate in seconds where the Crouter VM Activity Intensity Cut Point is “Light”|
|**vmModerate**|Number|A minute aggregate in seconds where the Crouter VM Activity Intensity Cut Point is “Moderate”|
|**vmVigorous**|Number|A minute aggregate in seconds where the Crouter VM Activity Intensity Cut Point is “Vigorous”|
|**vmMvpa**|Number|A minute aggregate in seconds where the Crouter VM Activity Intensity Cut Point between “Moderate” and “Vigorous”|
|**vaSedentary**|Number|A minute aggregate in seconds where the Crouter VA Activity Intensity Cut Point is “Sedentary”|
|**vaLight**|Number|A minute aggregate in seconds where the Crouter VA Activity Intensity Cut Point is “Light”|
|**vaModerate**|Number|A minute aggregate in seconds where the Crouter VA Activity Intensity Cut Point is “Moderate”|
|**vaVigorous**|Number|A minute aggregate in seconds where the Crouter VA Activity Intensity Cut Point is “Vigorous”|
|**vaMvpa**|Number|A minute aggregate in seconds where the Crouter VA Activity Intensity Cut Point between “Moderate” and “Vigorous”|


*StaudenmayerCutPointsMinuteAggregation*

|Name|Type|Description|
|:---|:---|:----------|
|**light**|Number|A minute aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is considered “Light”|
|**moderate**|Number|A minute aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is considered “Moderate”|
|**vigorous**|Number|A minute aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is considered “Vigorous”|
|**mvpa**|Number|A minute aggregate in seconds including the summation for the Staudenmayer Activity Intensity Cut Point between “Moderate” and “Vigorous”|
|**sedentary**|Number|A minute aggregate in seconds where the Staudenmayer Sedentary Intensity Cut Point is “Sedentary”|
|**nonSedentary**|Number|A minute aggregate in seconds where the Staudenmayer Sedentary Intensity Cut Point is “Non-Sedentary”|
|**locomotion**|Number|A minute aggregate in seconds where the Staudenmayer Locomotion Intensity Cut Point is “Locomotion”|
|**nonLocomotion**|Number|A minute aggregate in seconds where the Staudenmayer Locomotion Intensity Cut Point is “Non-Locomotion”|

*FreedsonCutPointsMinuteAggregation*

|Name|Type|Description|
|:---|:---|:----------|
|**sedentary**|Number|A minute aggregate in seconds where the Freedson Adult Cut Points Activity Intensity is “Sedentary”|
|**light**|Number|A minute aggregate in seconds where the Freedson Adult Cut Points Activity Intensity is “Light”|
|**moderate**|Number|A minute aggregate in seconds where the Freedson Adult Cut Points Activity Intensity is “Moderate”|
|**vigorous**|Number|A minute aggregate in seconds where the Freedson Adult Cut Points Activity Intensity is “Vigorous”|
|**veryVigorous**|Number|A minute aggregate in seconds where the Freedson Adult Cut Points Activity Intensity is “Very Vigorous”|

*EvensonCutPointsMinuteAggregation*

|Name|Type|Description|
|:---|:---|:----------|
|**sedentary**|Number|A minute aggregate in seconds where the Evenson Cut Points Activity Intensity is “Sedentary”|
|**light**|Number|A minute aggregate in seconds where the Evenson Cut Points Activity Intensity is “Light”|
|**moderate**|Number|A minute aggregate in seconds where the Evenson Cut Points Activity Intensity is “Moderate”|
|**vigorous**|Number|A minute aggregate in seconds where the Evenson Cut Points Activity Intensity is “Vigorous”|
|**mvpa**|Number|A minute aggregate in seconds where the Evenson Activity Intensity Cut Point between “Moderate” and “Vigorous”|

**Response Example:**

```json
{
    "items": [
        {
            "subjectId": 22524,
            "timestampUtc": "2017-11-01T11:45:00+00:00",
            "minuteSummarySettingsId": "cf233e99-1d9a-4def-b059-08d855519629",
            "activityMonitorSerial": "CPW1B01190145",
            "studyId": 2780,
            "isWear": true,
            "isSleep": false,
            "x": 3342,
            "y": 2285,
            "z": 1375,
            "vectorMagnitude": 4275.606857511574,
            "mets": 4.033920550685386,
            "calories": 7.044567372217769
        },
        {
            "subjectId": 22524,
            "timestampUtc": "2017-11-01T11:46:00+00:00",
            "minuteSummarySettingsId": "cf233e99-1d9a-4def-b059-08d855519629",
            "activityMonitorSerial": "CPW1B01190145",
            "studyId": 2780,
            "isWear": true,
            "isSleep": false,
            "x": 3448,
            "y": 3368,
            "z": 1832,
            "vectorMagnitude": 5156.389434478354,
            "mets": 3.5813816724334275,
            "calories": 6.254283930504439
        },
        ...
        {
            "subjectId": 22524,
            "timestampUtc": "2017-11-01T13:24:00+00:00",
            "minuteSummarySettingsId": "cf233e99-1d9a-4def-b059-08d855519629",
            "activityMonitorSerial": "CPW1B01190145",
            "studyId": 2780,
            "isWear": true,
            "isSleep": false,
            "x": 5636,
            "y": 5689,
            "z": 0,
            "vectorMagnitude": 8008.071990185902,
            "mets": 1.142009567790956,
            "calories": 1.9943286534619031
        }
    ],
    "links": {},
    "totalCount": 2198,
    "limit": 100,
    "offset": 0
}
```


## List Study Minute Summary Settings

Returns a list of Minute Summary Settings within the requested study.

**Request:**

```http
GET /analytics/v3/Studies/{studyId}/MinuteSummarySettings
```

**Query Options**

|Field|Type|Description|
|-----|----|-----------|
|**ids**|String Array of GUIDs|GUIDs of the Minute Summary Settings|

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|**id**|String (GUID)|Minute Summary Setting ID|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**wearPeriodSettingId**|String (GUID)|The ID of the Wear Period Algorithm Setting Used In the Minute Summary|
|**sleepPeriodSettingId**|String (GUID)|The ID of the Sleep Period Algorithm Setting Used In the Minute Summary|
|**epochSummarySettingId**|String (GUID)|The ID of the Epoch Algorithm Setting Used In the Minute Summary|
|**cutpointSettingIds**|String Array (GUID)|The IDs of the Cutpoint Algorithm Settings Used In the Minute Summary|
|**stepsSettingId**|String (GUID)|The ID of the Steps Algorithm Setting Used In the Minute Summary (This property is only present if there is a steps algorithm associated with the Minute Summary Setting)|
|**metsCaloriesSettingId**|String (GUID)|The ID of the METs/Calories Algorithm Setting Used In the Minute Summary (This property is only present if there is a METs/Calories algorithm associated with the Minute Summary Setting)|

**Response Example:**

```json
{
    "items": [
        {
            "id": "cf233e99-1d9a-4def-b059-08d855519629",
            "studyId": 2780,
            "wearPeriodSettingId": "c939ca38-db06-eb11-96f5-000d3a102a21",
            "sleepPeriodSettingId": "c839ca38-db06-eb11-96f5-000d3a102a21",
            "epochSummarySettingId": "c739ca38-db06-eb11-96f5-000d3a102a21",
            "cutPointSettingIds": [],
            "metsCaloriesSettingId": "eecf3840-db06-eb11-96f5-000d3a102a21"
        }
    ],
    "links": {},
    "totalCount": 1,
    "limit": 100,
    "offset": 0
}
```


## Retrieve Minute Summary Setting

Returns a single Minute Summary Setting by ID within the requested study.

**Request:**

```http
GET /analytics/v3/Studies/{studyId}/MinuteSummarySettings/{minuteSummarySettingId}
```

**Response:**

|Field|Type|Description|
|-----|----|-----------|
|**id**|String (GUID)|Minute Summary Setting ID|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**wearPeriodSettingId**|String (GUID)|The ID of the Wear Period Algorithm Setting Used In the Minute Summary|
|**sleepPeriodSettingId**|String (GUID)|The ID of the Sleep Period Algorithm Setting Used In the Minute Summary|
|**epochSummarySettingId**|String (GUID)|The ID of the Epoch Algorithm Setting Used In the Minute Summary|
|**cutpointSettingIds**|String Array (GUID)|The IDs of the Cutpoint Algorithm Settings Used In the Minute Summary|
|**stepsSettingId**|String (GUID)|The ID of the Steps Algorithm Setting Used In the Minute Summary (This property is only present if there is a steps algorithm associated with the Minute Summary Setting)|
|**metsCaloriesSettingId**|String (GUID)|The ID of the METs/Calories Algorithm Setting Used In the Minute Summary (This property is only present if there is a METs/Calories algorithm associated with the Minute Summary Setting)|

**Response Example:**

```json
{
    "id": "cf233e99-1d9a-4def-b059-08d855519629",
    "studyId": 2780,
    "wearPeriodSettingId": "c939ca38-db06-eb11-96f5-000d3a102a21",
    "sleepPeriodSettingId": "c839ca38-db06-eb11-96f5-000d3a102a21",
    "epochSummarySettingId": "c739ca38-db06-eb11-96f5-000d3a102a21",
    "cutPointSettingIds": [],
    "metsCaloriesSettingId": "eecf3840-db06-eb11-96f5-000d3a102a21"
}
```
