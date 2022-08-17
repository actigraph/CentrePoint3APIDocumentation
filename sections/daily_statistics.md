# Daily Statistics

**NOTE: These requests require the *Analytics* API scope. (see [Scopes](scopes.md))**

## List Study Daily Statistics

Returns a list of Daily Statistics within the requested study.

**Request:**

```http
GET /analytics/v3/Studies/{studyId}/Subjects/{subjectId}/DailyStatistics
```

**Query Options**

|Field|Type|Description|
|-----|----|-----------|
|**dailyStatisticsSettingId**|GUID|ID of the Settings Used To Create the Daily Statistics|
|**fromDate**|String (ISO8601 Date)|Starting Date for the Daily Statistics Query (Inclusive)|
|**toDate**|String (ISO8601 Date)|Ending Date for the Daily Statistics Query (Inclusive)|

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|**id**|Number|Daily Statistic ID|
|**subjectId**|Number|CentrePoint Subject ID (see [Subjects](subjects.md))|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**siteId**|Number|CentrePoint Site ID (see [Sites](sites.md))|
|**dailyStatisticsSettingId**|GUID of the Settings Used To create the Daily Statistic|
|**date**|String (ISO8601 Date)|Date/Time of the Daily Statistic|
|**activityMonitorSerials**|String Array|A List of All Activity Monitors Used for that Day|
|**firstEpochDateTimeUtc**|String (ISO8601 Date)|Date/Time in UTC of the First Epoch Used in the Daily Statistic|
|**lastEpochDateTimeUtc**|String (ISO8601 Date)|Date/Time in UTC of the Last Epoch Used in the Daily Statistic|
|**firstEpochDateTimeLocal**|String (ISO8601 Date)|Date/Time in Subject's Timezone of the First Epoch Used in the Daily Statistic|
|**lastEpochDateTimeLocal**|String (ISO8601 Date)|Date/Time in Subject's Timezone of the Last Epoch Used in the Daily Statistic|
|**epochAggregation**|Object (See *EpochAggregation* below)|The Aggregation of the Epochs Used in the Daily Statistic|
|**eventMarkerAggregation**|Object (See *EventMarkerAggregation* below)|The Aggregation of the Event Markers Used in the Daily Statistic (This property is only present when Event Markers are present in the study)|
|**crouterAggregations**|Object (See *CrouterAggregations* below)|The Aggregation of the Crouter Cutpoints Used in the Daily Statistic (This property is only present when Crouter Cutpoints are present in the study)|
|**freedsonAggregations**|Object Array (See *FreedsonAggregations* below)|The Aggregation of the Freedson Cutpoints Used in the Daily Statistic (This property is only present when Freedson Cutpoints are present in the study)|
|**staudenmayerAggregations**|Object Array (See *StaudenmayerAggregations* below)|The Aggregation of the Staudenmayer Cutpoints Used in the Daily Statistic (This property is only present when Staudenmayer Cutpoints are present in the study)|
|**evensonAggregations**|Object Array (See *EvensonAggregations* below)|The Aggregation of the Evenson Cutpoints Used in the Daily Statistic (This property is only present when Evenson Cutpoints are present in the study)|
|**genericCutpointAggregations**|Object Array (See *GenericCutpointAggregations* below)|The Aggregation of the Generic Cutpoints Used in the Daily Statistic (This property is only present when Generic Cutpoints are present in the study)|
|**mavmAggregation**|Object (See *MavmAggregation* below)|The Aggregation of the MAVM Steps Used in the Daily Statistic (This property is only present when MAVM Steps are present in the study)|
|**uwfAggregation**|Object (See *UwfAggregation* below)|The Aggregation of the UWF Steps Used in the Daily Statistic (This property is only present when UWF Steps are present in the study)|
|**hildebrandMetCalorieAggregation**|Object (See *HildebrandMetCalorieAggregation* below)|The Aggregation of the Hildebrand METs/Calories Used in the Daily Statistic (This property is only present when Hildebrand METs/Calories are present in the study)|
|**crouterYouthMetCalorieAggregation**|Object (See *CrouterYouthMetCalorieAggregation* below)|The Aggregation of the Crouter Youth METs/Calories Used in the Daily Statistic (This property is only present when CrouterYouth METs/Calories are present in the study)|


*Epoch Aggregation*

|Name|Type|Description|
|:---|:---|:----------|
|**wearMinutes**|Number|A daily aggregate, in minutes, of the non-partial epochs for subject that represent when subject was wearing monitor based on wear detection algorithm|
|**nonWearMinutes**|Number|A daily aggregate, in minutes, of the non-partial epochs for subject that represent when subject was not wearing monitor based on wear detection algorithm|
|**sleepMinutes**|Number|A daily aggregate of the non-partial epochs for subject that represent when the subject was asleep based on sleep detection algorithm|
|**awakeMinutes**|Number|A daily aggregate of the non-partial epochs for subject that represent when the subject was awake|
|**wearAwakeMinutes**|Number|A daily aggregate of the non-partial epochs for subject that represent when subject was wearing monitor and awake|
|**wearSleepMinutes**|Number|A daily aggregate of the non-partial epochs for subject that represent when subject was wearing monitor and asleep|
|**totalNonFilteredMinutes**|Number|A daily aggregate of the non-partial epochs for given subject not filtered for wear or sleep|
|**totalNonFilteredAxisXCounts**|Number|A daily aggregate of the X axis counts from the non-partial epochs for subject|
|**totalNonFilteredAxisYCounts**|Number|A daily aggregate of the Y axis counts from the non-partial epochs for subject|
|**totalNonFilteredAxisZCounts**|Number|A daily aggregate of the Z axis counts from the non-partial epochs for subject|
|**wearFilteredAxisXCounts**|Number|A daily aggregate of the X axis counts from the non-partial epochs for subject that represent when subject was wearing monitor|
|**wearFilteredAxisYCounts**|Number|A daily aggregate of the Y axis counts from the non-partial epochs for subject that represent when subject was wearing monitor|
|**wearFilteredAxisZCounts**|Number|A daily aggregate of the Z axis counts from the non-partial epochs for subject that represent when subject was wearing monitor|
|**wearAwakeFilteredAxisXCounts**|Number|A daily aggregate of the X axis counts from the non-partial epochs for subject that represent when subject was wearing monitor and awake|
|**wearAwakeFilteredAxisYCounts**|Number|A daily aggregate of the Y axis counts from the non-partial epochs for subject that represent when subject was wearing monitor and awake|
|**wearAwakeFilteredAxisZCounts**|Number|A daily aggregate of the Z axis counts from the non-partial epochs for subject that represent when subject was wearing monitor and awake|
|**wearSleepFilteredAxisXCounts**|Number|A daily aggregate of the X axis counts from the non-partial epochs for subject that represent when subject was wearing monitor and asleep|
|**wearSleepFilteredAxisYCounts**|Number|A daily aggregate of the Y axis counts from the non-partial epochs for subject that represent when subject was wearing monitor and asleep|
|**wearSleepFilteredAxisZCounts**|Number|A daily aggregate of the Z axis counts from the non-partial epochs for subject that represent when subject was wearing monitor and asleep|
|**totalNonFilteredVectorMagnitude**|Number|A daily aggregate of the Vector Magnitude values (of x, y, and x axis counts) from the non-partial epochs for subject|
|**wearFilteredVectorMagnitude**|Number|A daily aggregate of the Vector Magnitude values (of x, y, and x axis counts) from the non-partial epochs for subject which represent when subject was wearing the monitor|
|**wearAwakeFilteredVectorMagnitude**|Number|A daily aggregate of the Vector Magnitude values (of x, y, and x axis counts) from the non-partial epochs for subject which represent when subject was wearing the monitor and awake|
|**wearSleepFilteredVectorMagnitude**|Number|A  daily aggregate of the Vector Magnitude values (of x, y, and x axis counts) from the non-partial epochs for subject which represent when subject was wearing the monitor and awake|
|**firstEpochDateTimeUtc**|String (ISO8601 Date/Time)|Date Time in UTC timezone of first epoch recorded for this day|
|**lastEpochDateTimeUtc**|String (ISO8601 Date/Time)|Date Time in UTC timezone of last epoch recorded for this day|
|**firstEpochDateTimeLocal**|String (ISO8601 Date/Time)|Date Time in subject's timezone of first epoch recorded for this day|
|**lastEpochDateTimeLocal**|String (ISO8601 Date/Time)|Date Time in subject's timezone of last epoch recorded for this day|

*EventMarkerAggregation*

|Name|Type|Description|
|:---|:---|:----------|
|**longPressCount**|Number|A daily aggregate of Long Press Events|
|**pressCount**|Number|A daily aggregate of Press Events|
|**releaseCount**|Number|A daily aggregate of Release Events|

*FreedsonAggregations*

|Name|Type|Description|
|:---|:---|:----------|
|**nonFilteredVASedentary**|Number|A daily aggregate in seconds where the Freedson Adult Cut Points VA Activity Intensity is “Sedentary”|
|**nonFilteredVALight**|Number|A daily aggregate in seconds where the Freedson Adult Cut Points VA Activity Intensity is “Light”|
|**nonFilteredVAModerate**|Number|A daily aggregate in seconds where the Freedson Adult Cut Points VA Activity Intensity is “Moderate”|
|**nonFilteredVAVigorous**|Number|A daily aggregate in seconds where the Freedson Adult Cut Points VA Activity Intensity is “Vigorous”|
|**nonFilteredVAVeryVigorous**|Number|A daily aggregate in seconds where the Freedson Adult Cut Points VA Activity Intensity is “Very Vigorous”|
|**wearFilteredVASedentary**|Number|A daily aggregate in seconds where the Freedson Adult Cut Points VA Activity Intensity is “Sedentary” where the subject was wearing the monitor|
|**wearFilteredVALight**|Number|A daily aggregate in seconds where the Freedson Adult Cut Points VA Activity Intensity is “Light” where the subject was wearing the monitor|
|**wearFilteredVAModerate**|Number|A daily aggregate in seconds where the Freedson Adult Cut Points VA Activity Intensity is “Moderate” where the subject was wearing the monitor|
|**wearFilteredVAVigorous**|Number|A daily aggregate in seconds where the Freedson Adult Cut Points VA Activity Intensity is “Vigorous” where the subject was wearing the monitor|
|**wearFilteredVAVeryVigorous**|Number|A daily aggregate in seconds where the Freedson Adult Cut Points VA Activity Intensity is “Very Vigorous” where the subject was wearing the monitor|
|**wearAwakeFilteredVASedentary**|Number|A daily aggregate in seconds where the Freedson Adult Cut Points VA Activity Intensity is “Sedentary” where the subject was wearing the monitor and awake|
|**wearAwakeFilteredVALight**|Number|A daily aggregate in seconds where the Freedson Adult Cut Points VA Activity Intensity is “Light” where the subject was wearing the monitor and awake|
|**wearAwakeFilteredVAModerate**|Number|A daily aggregate in seconds where the Freedson Adult Cut Points VA Activity Intensity is “Moderate” where the subject was wearing the monitor and awake|
|**wearAwakeFilteredVAVigorous**|Number|A daily aggregate in seconds where the Freedson Adult Cut Points VA Activity Intensity is “Vigorous” where the subject was wearing the monitor and awake|
|**wearAwakeFilteredVAVeryVigorous**|Number|A daily aggregate in seconds where the Freedson Adult Cut Points VA Activity Intensity is “Very Vigorous” where the subject was wearing the monitor and awake|
|**wearSleepFilteredVASedentary**|Number|A daily aggregate in seconds where the Freedson Adult Cut Points VA Activity Intensity is “Sedentary” where the subject was wearing the monitor and asleep|
|**wearSleepFilteredVALight**|Number|A daily aggregate in seconds where the Freedson Adult Cut Points VA Activity Intensity is “Light” where the subject was wearing the monitor and asleep|
|**wearSleepFilteredVAModerate**|Number|A daily aggregate in seconds where the Freedson Adult Cut Points VA Activity Intensity is “Moderate” where the subject was wearing the monitor and asleep|
|**wearSleepFilteredVAVigorous**|Number|A daily aggregate in seconds where the Freedson Adult Cut Points VA Activity Intensity is “Vigorous” where the subject was wearing the monitor and asleep|
|**wearSleepFilteredVAVeryVigorous**|Number|A daily aggregate in seconds where the Freedson Adult Cut Points VA Activity Intensity is “Very Vigorous” where the subject was wearing the monitor and asleep|

*EvensonAggregations*

|Name|Type|Description|
|:---|:---|:----------|
|**nonFilteredSedentary**|Number|A daily aggregate in seconds where the Evenson Cut Points VA Activity Intensity is “Sedentary”|
|**nonFilteredLight**|Number|A daily aggregate in seconds where the Evenson Cut Points VA Activity Intensity is “Light”|
|**nonFilteredModerate**|Number|A daily aggregate in seconds where the Evenson Cut Points VA Activity Intensity is “Moderate”|
|**nonFilteredVigorous**|Number|A daily aggregate in seconds where the Evenson Cut Points VA Activity Intensity is “Vigorous”|
|**nonFilteredMVPA**|Number|A daily aggregate in seconds where the Evenson Activity Intensity Cut Point between “Moderate” and “Vigorous”|
|**wearFilteredSedentary**|Number|A daily aggregate in seconds where the Evenson Cut Points VA Activity Intensity is “Sedentary” where the subject was wearing the monitor|
|**wearFilteredLight**|Number|A daily aggregate in seconds where the Evenson Cut Points VA Activity Intensity is “Light” where the subject was wearing the monitor|
|**wearFilteredModerate**|Number|A daily aggregate in seconds where the Evenson Cut Points VA Activity Intensity is “Moderate” where the subject was wearing the monitor|
|**wearFilteredVigorous**|Number|A daily aggregate in seconds where the Evenson Cut Points VA Activity Intensity is “Vigorous” where the subject was wearing the monitor|
|**wearFilteredMVPA**|Number|A daily aggregate in seconds where the Evenson Activity Intensity Cut Point between “Moderate” and “Vigorous” where the subject was wearing the monitor|
|**wearAwakeSedentary**|Number|A daily aggregate in seconds where the Evenson Cut Points VA Activity Intensity is “Sedentary” where the subject was wearing the monitor and awake|
|**wearAwakeLight**|Number|A daily aggregate in seconds where the Evenson Cut Points VA Activity Intensity is “Light” where the subject was wearing the monitor and awake|
|**wearAwakeModerate**|Number|A daily aggregate in seconds where the Evenson Cut Points VA Activity Intensity is “Moderate” where the subject was wearing the monitor and awake|
|**wearAwakeVigorous**|Number|A daily aggregate in seconds where the Evenson Cut Points VA Activity Intensity is “Vigorous” where the subject was wearing the monitor and awake|
|**wearAwakeMVPA**|Number|A daily aggregate in seconds where the Evenson Activity Intensity Cut Point between “Moderate” and “Vigorous” where the subject was wearing the monitor and awake|

*GenericCutpointAggregations*

|Name|Type|Description|
|:---|:---|:----------|
|**algorithmName**|String|Name of the algorithm setting used to generate the generic cutpoints|
|**totalBuckets**|Dictionary<String, Number>|A daily aggregate in seconds of each defined cutpoint bucket|
|**wearBuckets**|Dictionary<String, Number>|A daily aggregate in seconds of each defined cutpoint bucket where the subject was wearing the monitor|
|**awakeBuckets**|Dictionary<String, Number>|A daily aggregate in seconds of each defined cutpoint bucket where the subject was awake|
|**wearAwakeBuckets**|Dictionary<String, Number>|A daily aggregate in seconds of each defined cutpoint bucket where the subject was wearing the monitor and awake|
|**totalAggregateBuckets**|Dictionary<String, Number>|A daily aggregate in seconds of each defined daily aggregate cutpoint bucket|
|**wearAggregateBuckets**|Dictionary<String, Number>|A daily aggregate in seconds of each defined daily aggregate cutpoint bucket where the subject was wearing the monitor|
|**awakeAggregateBuckets**|Dictionary<String, Number>|A daily aggregate in seconds of each defined daily aggregate cutpoint bucket where the subject was awake|
|**wearAwakeAggregateBuckets**|Dictionary<String, Number>|A daily aggregate in seconds of each defined daily aggregate cutpoint bucket where the subject was wearing the monitor and awake|

*MAVMAggregation*

|Name|Type|Description|
|:---|:---|:----------|
|**nonFilteredSteps**|Number|Total steps for day|
|**wearFilteredSteps**|Number|Total steps where activity monitor was considered worn|
|**wearAwakeFilteredSteps**|Number|Total steps where activity monitor was worn and subject was considered awake|
|**wearSleepFilteredSteps**|Number|Total steps where activity monitor was worn and subject was considered asleep|

*CrouterAggregations*

|Name|Type|Description|
|:---|:---|:----------|
|**nonFilteredVMSedentary**|Number|A daily aggregate in seconds where the Crouter VM Activity Intensity Cut Point is “Sedentary”|
|**nonFilteredVMLight**|Number|A daily aggregate in seconds where the Crouter VM Activity Intensity Cut Point is “Light”|
|**nonFilteredVMModerate**|Number|A daily aggregate in seconds where the Crouter VM Activity Intensity Cut Point is “Moderate”|
|**nonFilteredVMVigorous**|Number|A daily aggregate in seconds where the Crouter VM Activity Intensity Cut Point is “Vigorous”|
|**nonFilteredVMMVPA**|Number|A daily aggregate in seconds where the Crouter VM Activity Intensity Cut Point between “Moderate” and “Vigorous”|
|**wearFilteredVMSedentary**|Number|A daily aggregate in seconds where the Crouter VM Activity Intensity Cut Point is “Sedentary” which represent where the subject was wearing the monitor|
|**wearFilteredVMLight**|Number|A daily aggregate in seconds where the Crouter VM Activity Intensity Cut Point is “Light” which represent where the subject was wearing the monitor|
|**wearFilteredVMModerate**|Number|A daily aggregate in seconds where the Crouter VM Activity Intensity Cut Point is “Moderate” which represent where the subject was wearing the monitor|
|**wearFilteredVMVigorous**|Number|A daily aggregate in seconds where the Crouter VM Activity Intensity Cut Point is “Vigorous” which represent where the subject was wearing the monitor|
|**wearFilteredVMMVPA**|Number|A daily aggregate in seconds where the Crouter VM Activity Intensity Cut Point is between “Moderate” and “Vigorous” which represent where the subject was wearing the monitor|
|**wearAwakeFilteredVMSedentary**|Number|A daily aggregate in seconds where the Crouter VM Activity Intensity Cut Point is “Sedentary” which represent where the subject was wearing the monitor and awake|
|**wearAwakeFilteredVMLight**|Number|A daily aggregate in seconds where the Crouter VM Activity Intensity Cut Point is “Light” which represent where the subject was wearing the monitor and awake|
|**wearAwakeFilteredVMModerate**|Number|A daily aggregate in seconds where the Crouter VM Activity Intensity Cut Point is “Moderate” which represent where the subject was wearing the monitor and awake|
|**wearAwakeFilteredVMVigorous**|Number|A daily aggregate in seconds where the Crouter VM Activity Intensity Cut Point is “Vigorous” which represent where the subject was wearing the monitor and awake|
|**wearAwakeFilteredVMMVPA**|Number|A daily aggregate in seconds where the Crouter VM Activity Intensity Cut Point is between “Moderate” and “Vigorous” which represent where the subject was wearing the monitor and awake|
|**wearSleepFilteredVMSedentary**|Number|A daily aggregate in seconds where the Crouter VM Activity Intensity Cut Point is “Sedentary” which represent where the subject was wearing the monitor and asleep|
|**wearSleepFilteredVMLight**|Number|A daily aggregate in seconds where the Crouter VM Activity Intensity Cut Point is “Light” which represent where the subject was wearing the monitor and asleep|
|**wearSleepFilteredVMModerate**|Number|A daily aggregate in seconds where the Crouter VM Activity Intensity Cut Point is “Moderate” which represent where the subject was wearing the monitor and asleep|
|**wearSleepFilteredVMVigorous**|Number|A daily aggregate in seconds where the Crouter VM Activity Intensity Cut Point is “Vigorous” which represent where the subject was wearing the monitor and asleep|
|**wearSleepFilteredVMMVPA**|Number|A daily aggregate in seconds where the Crouter VM Activity Intensity Cut Point is between “Moderate” and “Vigorous” which represent where the subject was wearing the monitor and asleep|
|**nonFilteredVASedentary**|Number|A daily aggregate in seconds where the Crouter VA Activity Intensity Cut Point is “Sedentary”|
|**nonFilteredVALight**|Number|A daily aggregate in seconds where the Crouter VA Activity Intensity Cut Point is “Light”|
|**nonFilteredVAModerate**|Number|A daily aggregate in seconds where the Crouter VA Activity Intensity Cut Point is “Moderate”|
|**nonFilteredVAVigorous**|Number|A daily aggregate in seconds where the Crouter VA Activity Intensity Cut Point is “Vigorous”|
|**nonFilteredVAMVPA**|Number|A daily aggregate in seconds where the Crouter VA Activity Intensity Cut Point between “Moderate” and “Vigorous”|
|**wearFilteredVASedentary**|Number|A daily aggregate in seconds where the Crouter VA Activity Intensity Cut Point is “Sedentary” which represent where the subject was wearing the monitor|
|**wearFilteredVALight**|Number|A daily aggregate in seconds where the Crouter VA Activity Intensity Cut Point is “Light” which represent where the subject was wearing the monitor|
|**wearFilteredVAModerate**|Number|A daily aggregate in seconds where the Crouter VA Activity Intensity Cut Point is “Moderate” which represent where the subject was wearing the monitor|
|**wearFilteredVAVigorous**|Number|A daily aggregate in seconds where the Crouter VA Activity Intensity Cut Point is “Vigorous” which represent where the subject was wearing the monitor|
|**wearFilteredVAMVPA**|Number|A daily aggregate in seconds where the Crouter VA Activity Intensity Cut Point is between “Moderate” and “Vigorous” which represent where the subject was wearing the monitor|
|**wearAwakeFilteredVASedentary**|Number|A daily aggregate in seconds where the Crouter VA Activity Intensity Cut Point is “Sedentary” which represent where the subject was wearing the monitor and awake|
|**wearAwakeFilteredVALight**|Number|A daily aggregate in seconds where the Crouter VA Activity Intensity Cut Point is “Light” which represent where the subject was wearing the monitor and awake|
|**wearAwakeFilteredVAModerate**|Number|A daily aggregate in seconds where the Crouter VA Activity Intensity Cut Point is “Moderate” which represent where the subject was wearing the monitor and awake|
|**wearAwakeFilteredVAVigorous**|Number|A daily aggregate in seconds where the Crouter VA Activity Intensity Cut Point is “Vigorous” which represent where the subject was wearing the monitor and awake|
|**wearAwakeFilteredVAMVPA**|Number|A daily aggregate in seconds where the Crouter VA Activity Intensity Cut Point is between “Moderate” and “Vigorous” which represent where the subject was wearing the monitor and awake|
|**wearSleepFilteredVASedentary**|Number|A daily aggregate in seconds where the Crouter VA Activity Intensity Cut Point is “Sedentary” which represent where the subject was wearing the monitor and asleep|
|**wearSleepFilteredVALight**|Number|A daily aggregate in seconds where the Crouter VA Activity Intensity Cut Point is “Light” which represent where the subject was wearing the monitor and asleep|
|**wearSleepFilteredVAModerate**|Number|A daily aggregate in seconds where the Crouter VA Activity Intensity Cut Point is “Moderate” which represent where the subject was wearing the monitor and asleep|
|**wearSleepFilteredVAVigorous**|Number|A daily aggregate in seconds where the Crouter VA Activity Intensity Cut Point is “Vigorous” which represent where the subject was wearing the monitor and asleep|
|**wearSleepFilteredVAMVPA**|Number|A daily aggregate in seconds where the Crouter VA Activity Intensity Cut Point is between “Moderate” and “Vigorous” which represent where the subject was wearing the monitor and asleep|

*StaudenmayerAggregations*

|Name|Type|Description|
|:---|:---|:----------|
|**nonFilteredLight**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is considered “Light”|
|**nonFilteredModerate**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is considered “Moderate”|
|**nonFilteredVigorous**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is considered “Vigorous”|
|**nonFilteredMVPA**|Number|A daily aggregate in seconds including the summation for the Staudenmayer Activity Intensity Cut Point between “Moderate” and “Vigorous”|
|**nonFilteredSedentary**|Number|A daily aggregate in seconds where the Staudenmayer Sedentary Intensity Cut Point is “Sedentary”|
|**nonFilteredNonSedentary**|Number|A daily aggregate in seconds where the Staudenmayer Sedentary Intensity Cut Point is “Non-Sedentary”|
|**nonFilteredLocomotion**|Number|A daily aggregate in seconds where the Staudenmayer Locomotion Intensity Cut Point is “Locomotion”|
|**nonFilteredNonLocomotion**|Number|A daily aggregate in seconds where the Staudenmayer Locomotion Intensity Cut Point is “Non-Locomotion”|
|**WearFilteredLight**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Light” representing when the subject was wearing the monitor|
|**wearFilteredModerate**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Moderate” representing when the subject was wearing the monitor|
|**wearFilteredVigorous**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Vigorous” representing when the subject was wearing the monitor|
|**wearFilteredMVPA**|Number|A daily aggregate in seconds where the summation for the Staudenmayer Activity Intensity Cut Point between “Moderate” and “Vigorous” representing when the subject was wearing the monitor|
|**wearFilteredSedentary**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Sedentary” representing when the subject was wearing the monitor|
|**wearFilteredNonSedentary**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Non-Sedentary” representing when the subject was wearing the monitor|
|**wearFilteredLocomotion**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Locomotion” representing when the subject was wearing the monitor|
|**wearFilteredNonLocomotion**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Non-Locomotion” representing when the subject was wearing the monitor|
|**wearAwakeFilteredLight**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Light” representing when subject was wearing the monitor and awake|
|**wearAwakeFilteredModerate**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Moderate” representing when subject was wearing the monitor and awake|
|**wearAwakeFilteredVigorous**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Vigorous” representing when subject was wearing the monitor and awake|
|**wearAwakeFilteredMVPA**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is between “Moderate” and “Vigorous” representing when subject was wearing the monitor and awake|
|**wearAwakeFilteredSedentary**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Sedentary” representing when subject was wearing the monitor and awake|
|**wearAwakeFilteredNonSedentary**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Non-Sedentary” representing when subject was wearing the monitor and awake|
|**wearAwakeFilteredLocomotion**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Locomotion” representing when subject was wearing the monitor and awake|
|**wearAwakeFilteredNonLocomotion**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Non-Locomotion” representing when subject was wearing the monitor and awake|
|**wearSleepFilteredLight**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Light” representing when subject was wearing the monitor and asleep|
|**wearSleepFilteredModerate**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Moderate” representing when subject was wearing the monitor and asleep|
|**wearSleepFilteredVigorous**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Vigorous” representing when subject was wearing the monitor and asleep|
|**wearSleepFilteredMVPA**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is between “Moderate” and “Vigorous” representing when subject was wearing the monitor and asleep|
|**wearSleepFilteredSedentary**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Sedentary” representing when subject was wearing the monitor and asleep|
|**wearSleepFilteredNonSedentary**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Non-Sedentary” representing when subject was wearing the monitor and asleep|
|**wearSleepFilteredLocomotion**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Locomotion” representing when subject was wearing the monitor and asleep|
|**wearSleepFilteredNonLocomotion**|Number|A daily aggregate in seconds where the Staudenmayer Activity Intensity Cut Point is “Non-Locomotion” representing when subject was wearing the monitor and asleep|

*UwfAggregation*

|Name|Type|Description|
|:---|:---|:----------|
|**nonFilteredSteps**|Number|Total steps for day|
|**wearFilteredSteps**|Number|Total steps where activity monitor was considered worn|
|**wearAwakeFilteredSteps**|Number|Total steps where activity monitor was worn and subject was considered awake|
|**wearSleepFilteredSteps**|Number|Total steps where activity monitor was worn and subject was considered asleep|

*HildebrandMetCalorieAggregation*

|Name|Type|Description|
|:---|:---|:----------|
|**nonFilteredMets**|Number|Total METS for the day|
|**wearMets**|Number|Total METS where activity monitor was considered worn|
|**wearAwakeMets**|Number|Total METS where activity monitor was worn and subject was considered awake|
|**nonFilteredMetsAverage**|Number|Average METS for the day|
|**wearMetsAverage**|Number|Average METS where activity monitor was considered worn|
|**wearAwakeMetsAverage**|Number|Average METS where activity monitor was worn and subject was considered awake|
|**nonFilteredCalories**|Number|Total Calories for the day|
|**wearCalories**|Number|Total Calories where activity monitor was considered worn|
|**wearAwakeCalories**|Number|Total Calories where activity monitor was worn and subject was considered awake|

*CrouterYouthMetCalorieAggregation*

|Name|Type|Description|
|:---|:---|:----------|
|**nonFilteredMets**|Number|Total METS for the day|
|**wearMets**|Number|Total METS where activity monitor was considered worn|
|**wearAwakeMets**|Number|Total METS where activity monitor was worn and subject was considered awake|
|**nonFilteredMetsAverage**|Number|Average METS for the day|
|**wearMetsAverage**|Number|Average METS where activity monitor was considered worn|
|**wearAwakeMetsAverage**|Number|Average METS where activity monitor was worn and subject was considered awake|
|**nonFilteredCalories**|Number|Total Calories for the day|
|**wearCalories**|Number|Total Calories where activity monitor was considered worn|
|**wearAwakeCalories**|Number|Total Calories where activity monitor was worn and subject was considered awake|

**Response Example:**

```json
{
    "items": [
        {
            "id": 1,
            "studyId": 2775,
            "dailyStatisticsSettingId": "ad1fda37-239d-48ad-581b-08d8556c9944",
            "subjectId": 22518,
            "date": "2020-10-05T00:00:00+00:00",
            "siteId": 5431,
            "activityMonitorSerials": [
                "TAS1F49170092"
            ],
            "epochAggregation": {
                "wearMinutes": 7.0,
                "nonWearMinutes": 1.0,
                "sleepMinutes": 0.0,
                "awakeMinutes": 8.0,
                "wearAwakeMinutes": 7.0,
                "wearSleepMinutes": 0.0,
                "totalNonFilteredMinutes": 8.0,
                "totalNonFilteredAxisXCounts": 17693,
                "totalNonFilteredAxisYCounts": 18595,
                "totalNonFilteredAxisZCounts": 14835,
                "wearFilteredAxisXCounts": 16788,
                "wearFilteredAxisYCounts": 17805,
                "wearFilteredAxisZCounts": 14249,
                "wearAwakeFilteredAxisXCounts": 16788,
                "wearAwakeFilteredAxisYCounts": 17805,
                "wearAwakeFilteredAxisZCounts": 14249,
                "wearSleepFilteredAxisXCounts": 0,
                "wearSleepFilteredAxisYCounts": 0,
                "wearSleepFilteredAxisZCounts": 0,
                "totalNonFilteredVectorMagnitude": 29646.138011552197,
                "wearFilteredVectorMagnitude": 28317.644146362174,
                "wearAwakeFilteredVectorMagnitude": 28317.644146362174,
                "wearSleepFilteredVectorMagnitude": 0.0,
                "nonFilteredVectorMagnitudeCounts": 30108.160465352863,
                "wearFilteredVectorMagnitudeCounts": 28771.552445026784,
                "wearAwakeFilteredVectorMagnitudeCounts": 28771.552445026784,
                "firstEpochDateTimeUtc": "2020-10-05T06:16:00+00:00",
                "lastEpochDateTimeUtc": "2020-10-05T06:23:00+00:00",
                "firstEpochDateTimeLocal": "2020-10-05T06:16:00+00:00",
                "lastEpochDateTimeLocal": "2020-10-05T06:23:00+00:00"
            },
            "crouterAggregations": [
                {
                    "nonFilteredVMSedentary": 340,
                    "nonFilteredVMLight": 60,
                    "nonFilteredVMModerate": 60,
                    "nonFilteredVMVigorous": 20,
                    "nonFilteredVMMVPA": 80,
                    "wearFilteredVMSedentary": 295,
                    "wearFilteredVMLight": 50,
                    "wearFilteredVMModerate": 55,
                    "wearFilteredVMVigorous": 20,
                    "wearFilteredVMMVPA": 75,
                    "wearAwakeFilteredVMSedentary": 295,
                    "wearAwakeFilteredVMLight": 50,
                    "wearAwakeFilteredVMModerate": 55,
                    "wearAwakeFilteredVMVigorous": 20,
                    "wearAwakeFilteredVMMVPA": 75,
                    "wearSleepFilteredVMSedentary": 0,
                    "wearSleepFilteredVMLight": 0,
                    "wearSleepFilteredVMModerate": 0,
                    "wearSleepFilteredVMVigorous": 0,
                    "wearSleepFilteredVMMVPA": 0,
                    "nonFilteredVASedentary": 335,
                    "nonFilteredVALight": 50,
                    "nonFilteredVAModerate": 75,
                    "nonFilteredVAVigorous": 20,
                    "nonFilteredVAMVPA": 95,
                    "wearFilteredVASedentary": 295,
                    "wearFilteredVALight": 35,
                    "wearFilteredVAModerate": 70,
                    "wearFilteredVAVigorous": 20,
                    "wearFilteredVAMVPA": 90,
                    "wearAwakeFilteredVASedentary": 295,
                    "wearAwakeFilteredVALight": 35,
                    "wearAwakeFilteredVAModerate": 70,
                    "wearAwakeFilteredVAVigorous": 20,
                    "wearAwakeFilteredVAMVPA": 90,
                    "wearSleepFilteredVASedentary": 0,
                    "wearSleepFilteredVALight": 0,
                    "wearSleepFilteredVAModerate": 0,
                    "wearSleepFilteredVAVigorous": 0,
                    "wearSleepFilteredVAMVPA": 0
                }
            ],
            "mavmAggregation": {
                "nonFilteredSteps": 0,
                "wearFilteredSteps": 0,
                "wearAwakeFilteredSteps": 0,
                "wearSleepFilteredSteps": 0
            },
            "genericCutpointAggregations": [
                {
                    "AlgorithmName": "Puyau Children VA",
                    "TotalBuckets": {
                        "Sedentary": 15960,
                        "Light": 8820,
                        "Moderate": 0,
                        "Vigorous": 0
                    },
                    "WearBuckets": {
                        "Sedentary": 13200,
                        "Light": 8820,
                        "Moderate": 0,
                        "Vigorous": 0
                    },
                    "AwakeBuckets": {
                        "Sedentary": 13200,
                        "Light": 8820,
                        "Moderate": 0,
                        "Vigorous": 0
                    },
                    "WearAwakeBuckets": {
                        "Sedentary": 13200,
                        "Light": 8820,
                        "Moderate": 0,
                        "Vigorous": 0
                    },
                    "TotalAggregateBuckets": {
                        "Mvpa": 0,
                        "Lvpa": 8820
                    },
                    "WearAggregateBuckets": {
                        "Mvpa": 0,
                        "Lvpa": 8820
                    },
                    "AwakeAggregateBuckets": {
                        "Mvpa": 0,
                        "Lvpa": 8820
                    },
                    "WearAwakeAggregateBuckets": {
                        "Mvpa": 0,
                        "Lvpa": 8820
                    }
                },
                {
                    "AlgorithmName": "Kim VM Hip",
                    "TotalBuckets": {
                        "Sedentary": 13379.5,
                        "Non-Sedentary": 11399.5
                    },
                    "WearBuckets": {
                        "Sedentary": 10619.5,
                        "Non-Sedentary": 11399.5
                    },
                    "AwakeBuckets": {
                        "Sedentary": 10619.5,
                        "Non-Sedentary": 11399.5
                    },
                    "WearAwakeBuckets": {
                        "Sedentary": 10619.5,
                        "Non-Sedentary": 11399.5
                    },
                    "TotalAggregateBuckets": {},
                    "WearAggregateBuckets": {},
                    "AwakeAggregateBuckets": {},
                    "WearAwakeAggregateBuckets": {}
                },
                {
                    "AlgorithmName": "Kim VA Wrist",
                    "TotalBuckets": {
                        "Sedentary": 13379.5,
                        "Non-Sedentary": 11399.5
                    },
                    "WearBuckets": {
                        "Sedentary": 10619.5,
                        "Non-Sedentary": 11399.5
                    },
                    "AwakeBuckets": {
                        "Sedentary": 10619.5,
                        "Non-Sedentary": 11399.5
                    },
                    "WearAwakeBuckets": {
                        "Sedentary": 10619.5,
                        "Non-Sedentary": 11399.5
                    },
                    "TotalAggregateBuckets": {},
                    "WearAggregateBuckets": {},
                    "AwakeAggregateBuckets": {},
                    "WearAwakeAggregateBuckets": {}
                },
                {
                    "AlgorithmName": "Kim VM Wrist",
                    "TotalBuckets": {
                        "Sedentary": 13379.5,
                        "Non-Sedentary": 11399.5
                    },
                    "WearBuckets": {
                        "Sedentary": 10619.5,
                        "Non-Sedentary": 11399.5
                    },
                    "AwakeBuckets": {
                        "Sedentary": 10619.5,
                        "Non-Sedentary": 11399.5
                    },
                    "WearAwakeBuckets": {
                        "Sedentary": 10619.5,
                        "Non-Sedentary": 11399.5
                    },
                    "TotalAggregateBuckets": {},
                    "WearAggregateBuckets": {},
                    "AwakeAggregateBuckets": {},
                    "WearAwakeAggregateBuckets": {}
                },
                {
                    "AlgorithmName": "Koster Non-Dominant Wrist",
                    "TotalBuckets": {
                        "Sedentary": 13380,
                        "Non-Sedentary": 11400
                    },
                    "WearBuckets": {
                        "Sedentary": 10620,
                        "Non-Sedentary": 11400
                    },
                    "AwakeBuckets": {
                        "Sedentary": 10620,
                        "Non-Sedentary": 11400
                    },
                    "WearAwakeBuckets": {
                        "Sedentary": 10620,
                        "Non-Sedentary": 11400
                    },
                    "TotalAggregateBuckets": {},
                    "WearAggregateBuckets": {},
                    "AwakeAggregateBuckets": {},
                    "WearAwakeAggregateBuckets": {}
                },
                {
                    "AlgorithmName": "Koster Dominant Wrist",
                    "TotalBuckets": {
                        "Sedentary": 13380,
                        "Non-Sedentary": 11400
                    },
                    "WearBuckets": {
                        "Sedentary": 10620,
                        "Non-Sedentary": 11400
                    },
                    "AwakeBuckets": {
                        "Sedentary": 10620,
                        "Non-Sedentary": 11400
                    },
                    "WearAwakeBuckets": {
                        "Sedentary": 10620,
                        "Non-Sedentary": 11400
                    },
                    "TotalAggregateBuckets": {},
                    "WearAggregateBuckets": {},
                    "AwakeAggregateBuckets": {},
                    "WearAwakeAggregateBuckets": {}
                }
            ],
            "firstEpochDateTimeUtc": "2020-10-05T06:16:00+00:00",
            "lastEpochDateTimeUtc": "2020-10-05T06:23:00+00:00",
            "firstEpochDateTimeLocal": "2020-10-05T06:16:00+00:00",
            "lastEpochDateTimeLocal": "2020-10-05T06:23:00+00:00"
        },
        {
            "id": 2,
            "studyId": 2775,
            "dailyStatisticsSettingId": "ad1fda37-239d-48ad-581b-08d8556c9944",
            "subjectId": 22519,
            "date": "2020-10-05T00:00:00+00:00",
            "siteId": 5431,
            "activityMonitorSerials": [
                "TAS1F49170092"
            ],
            "epochAggregation": {
                "wearMinutes": 14.0,
                "nonWearMinutes": 328.0,
                "sleepMinutes": 327.0,
                "awakeMinutes": 15.0,
                "wearAwakeMinutes": 14.0,
                "wearSleepMinutes": 0.0,
                "totalNonFilteredMinutes": 342.0,
                "totalNonFilteredAxisXCounts": 51405,
                "totalNonFilteredAxisYCounts": 48310,
                "totalNonFilteredAxisZCounts": 27739,
                "wearFilteredAxisXCounts": 51387,
                "wearFilteredAxisYCounts": 48297,
                "wearFilteredAxisZCounts": 27436,
                "wearAwakeFilteredAxisXCounts": 51387,
                "wearAwakeFilteredAxisYCounts": 48297,
                "wearAwakeFilteredAxisZCounts": 27436,
                "wearSleepFilteredAxisXCounts": 0,
                "wearSleepFilteredAxisYCounts": 0,
                "wearSleepFilteredAxisZCounts": 0,
                "totalNonFilteredVectorMagnitude": 75800.9382923457,
                "wearFilteredVectorMagnitude": 75670.06061845068,
                "wearAwakeFilteredVectorMagnitude": 75670.06061845068,
                "wearSleepFilteredVectorMagnitude": 0.0,
                "nonFilteredVectorMagnitudeCounts": 77607.69301814424,
                "wearFilteredVectorMagnitudeCounts": 77282.48941483306,
                "wearAwakeFilteredVectorMagnitudeCounts": 77282.48941483306,
                "firstEpochDateTimeUtc": "2020-10-05T06:39:00+00:00",
                "lastEpochDateTimeUtc": "2020-10-05T12:28:00+00:00",
                "firstEpochDateTimeLocal": "2020-10-05T06:39:00+00:00",
                "lastEpochDateTimeLocal": "2020-10-05T12:28:00+00:00"
            },
            "crouterAggregations": [
                {
                    "nonFilteredVMSedentary": 20290,
                    "nonFilteredVMLight": 55,
                    "nonFilteredVMModerate": 75,
                    "nonFilteredVMVigorous": 100,
                    "nonFilteredVMMVPA": 175,
                    "wearFilteredVMSedentary": 615,
                    "wearFilteredVMLight": 50,
                    "wearFilteredVMModerate": 75,
                    "wearFilteredVMVigorous": 100,
                    "wearFilteredVMMVPA": 175,
                    "wearAwakeFilteredVMSedentary": 615,
                    "wearAwakeFilteredVMLight": 50,
                    "wearAwakeFilteredVMModerate": 75,
                    "wearAwakeFilteredVMVigorous": 100,
                    "wearAwakeFilteredVMMVPA": 175,
                    "wearSleepFilteredVMSedentary": 0,
                    "wearSleepFilteredVMLight": 0,
                    "wearSleepFilteredVMModerate": 0,
                    "wearSleepFilteredVMVigorous": 0,
                    "wearSleepFilteredVMMVPA": 0,
                    "nonFilteredVASedentary": 20300,
                    "nonFilteredVALight": 45,
                    "nonFilteredVAModerate": 60,
                    "nonFilteredVAVigorous": 115,
                    "nonFilteredVAMVPA": 175,
                    "wearFilteredVASedentary": 620,
                    "wearFilteredVALight": 45,
                    "wearFilteredVAModerate": 60,
                    "wearFilteredVAVigorous": 115,
                    "wearFilteredVAMVPA": 175,
                    "wearAwakeFilteredVASedentary": 620,
                    "wearAwakeFilteredVALight": 45,
                    "wearAwakeFilteredVAModerate": 60,
                    "wearAwakeFilteredVAVigorous": 115,
                    "wearAwakeFilteredVAMVPA": 175,
                    "wearSleepFilteredVASedentary": 0,
                    "wearSleepFilteredVALight": 0,
                    "wearSleepFilteredVAModerate": 0,
                    "wearSleepFilteredVAVigorous": 0,
                    "wearSleepFilteredVAMVPA": 0
                }
            ],
            "mavmAggregation": {
                "nonFilteredSteps": 70,
                "wearFilteredSteps": 70,
                "wearAwakeFilteredSteps": 70,
                "wearSleepFilteredSteps": 0
            },
            "genericCutpointAggregations": [
                {
                    "AlgorithmName": "Puyau Children VA",
                    "TotalBuckets": {
                        "Sedentary": 64140,
                        "Light": 22260,
                        "Moderate": 0,
                        "Vigorous": 0
                    },
                    "WearBuckets": {
                        "Sedentary": 26700,
                        "Light": 22200,
                        "Moderate": 0,
                        "Vigorous": 0
                    },
                    "AwakeBuckets": {
                        "Sedentary": 22620,
                        "Light": 21780,
                        "Moderate": 0,
                        "Vigorous": 0
                    },
                    "WearAwakeBuckets": {
                        "Sedentary": 22620,
                        "Light": 21780,
                        "Moderate": 0,
                        "Vigorous": 0
                    },
                    "TotalAggregateBuckets": {
                        "Mvpa": 0,
                        "Lvpa": 22260
                    },
                    "WearAggregateBuckets": {
                        "Mvpa": 0,
                        "Lvpa": 22200
                    },
                    "AwakeAggregateBuckets": {
                        "Mvpa": 0,
                        "Lvpa": 21780
                    },
                    "WearAwakeAggregateBuckets": {
                        "Mvpa": 0,
                        "Lvpa": 21780
                    }
                },
                {
                    "AlgorithmName": "Kim VM Hip",
                    "TotalBuckets": {
                        "Sedentary": 13379.5,
                        "Non-Sedentary": 11399.5
                    },
                    "WearBuckets": {
                        "Sedentary": 10619.5,
                        "Non-Sedentary": 11399.5
                    },
                    "AwakeBuckets": {
                        "Sedentary": 10619.5,
                        "Non-Sedentary": 11399.5
                    },
                    "WearAwakeBuckets": {
                        "Sedentary": 10619.5,
                        "Non-Sedentary": 11399.5
                    },
                    "TotalAggregateBuckets": {},
                    "WearAggregateBuckets": {},
                    "AwakeAggregateBuckets": {},
                    "WearAwakeAggregateBuckets": {}
                },
                {
                    "AlgorithmName": "Kim VA Wrist",
                    "TotalBuckets": {
                        "Sedentary": 13379.5,
                        "Non-Sedentary": 11399.5
                    },
                    "WearBuckets": {
                        "Sedentary": 10619.5,
                        "Non-Sedentary": 11399.5
                    },
                    "AwakeBuckets": {
                        "Sedentary": 10619.5,
                        "Non-Sedentary": 11399.5
                    },
                    "WearAwakeBuckets": {
                        "Sedentary": 10619.5,
                        "Non-Sedentary": 11399.5
                    },
                    "TotalAggregateBuckets": {},
                    "WearAggregateBuckets": {},
                    "AwakeAggregateBuckets": {},
                    "WearAwakeAggregateBuckets": {}
                },
                {
                    "AlgorithmName": "Kim VM Wrist",
                    "TotalBuckets": {
                        "Sedentary": 13379.5,
                        "Non-Sedentary": 11399.5
                    },
                    "WearBuckets": {
                        "Sedentary": 10619.5,
                        "Non-Sedentary": 11399.5
                    },
                    "AwakeBuckets": {
                        "Sedentary": 10619.5,
                        "Non-Sedentary": 11399.5
                    },
                    "WearAwakeBuckets": {
                        "Sedentary": 10619.5,
                        "Non-Sedentary": 11399.5
                    },
                    "TotalAggregateBuckets": {},
                    "WearAggregateBuckets": {},
                    "AwakeAggregateBuckets": {},
                    "WearAwakeAggregateBuckets": {}
                },
                {
                    "AlgorithmName": "Koster Non-Dominant Wrist",
                    "TotalBuckets": {
                        "Sedentary": 13380,
                        "Non-Sedentary": 11400
                    },
                    "WearBuckets": {
                        "Sedentary": 10620,
                        "Non-Sedentary": 11400
                    },
                    "AwakeBuckets": {
                        "Sedentary": 10620,
                        "Non-Sedentary": 11400
                    },
                    "WearAwakeBuckets": {
                        "Sedentary": 10620,
                        "Non-Sedentary": 11400
                    },
                    "TotalAggregateBuckets": {},
                    "WearAggregateBuckets": {},
                    "AwakeAggregateBuckets": {},
                    "WearAwakeAggregateBuckets": {}
                },
                {
                    "AlgorithmName": "Koster Dominant Wrist",
                    "TotalBuckets": {
                        "Sedentary": 13380,
                        "Non-Sedentary": 11400
                    },
                    "WearBuckets": {
                        "Sedentary": 10620,
                        "Non-Sedentary": 11400
                    },
                    "AwakeBuckets": {
                        "Sedentary": 10620,
                        "Non-Sedentary": 11400
                    },
                    "WearAwakeBuckets": {
                        "Sedentary": 10620,
                        "Non-Sedentary": 11400
                    },
                    "TotalAggregateBuckets": {},
                    "WearAggregateBuckets": {},
                    "AwakeAggregateBuckets": {},
                    "WearAwakeAggregateBuckets": {}
                }
            ],
            "firstEpochDateTimeUtc": "2020-10-05T06:39:00+00:00",
            "lastEpochDateTimeUtc": "2020-10-05T12:28:00+00:00",
            "firstEpochDateTimeLocal": "2020-10-05T06:39:00+00:00",
            "lastEpochDateTimeLocal": "2020-10-05T12:28:00+00:00"
        }
    ],
    "links": {},
    "totalCount": 2,
    "limit": 100,
    "offset": 0
}
```


## List Study Daily Statistics Settings

Returns a list of Daily Statistics Settings within the requested study.

**Request:**

```http
GET /analytics/v3/Studies/{studyId}/DailyStatisticsSettings
```

**Query Options**

|Field|Type|Description|
|-----|----|-----------|
|**ids**|String Array of GUIDs|GUIDs of the Daily StatisticsSettings|

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|**id**|String (GUID)|Daily Statistic Setting ID|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**wearPeriodSettingId**|String (GUID)|The ID of the Wear Period Algorithm Setting Used In the Daily Statistics|
|**sleepPeriodSettingId**|String (GUID)|The ID of the Sleep Period Algorithm Setting Used In the Daily Statistics|
|**epochSummarySettingId**|String (GUID)|The ID of the Epoch Algorithm Setting Used In the Daily Statistics|
|**cutpointSettingIds**|String Array (GUID)|The IDs of the Cutpoint Algorithm Settings Used In the Daily Statistics|
|**stepsSettingId**|String (GUID)|The ID of the Steps Algorithm Setting Used In the Daily Statistics (This property is only present if there is a steps algorithm associated with the Daily Statistics Setting)|
|**metsCaloriesSettingId**|String (GUID)|The ID of the METs/Calories Algorithm Setting Used In the Daily Statistics (This property is only present if there is a METs/Calories algorithm associated with the Daily Statistics Setting)|

**Response Example:**

```json
{
    "items": [
        {
            "id": "ad1fda37-239d-48ad-581b-08d8556c9944",
            "studyId": 2775,
            "wearPeriodSettingId": "a13f3252-d106-eb11-96f5-000d3a102a21",
            "sleepPeriodSettingId": "116b5c9b-d106-eb11-96f5-000d3a102a21",
            "epochSummarySettingId": "3555504b-d106-eb11-96f5-000d3a102a21",
            "cutpointSettingIds": [
                "df777f61-d106-eb11-96f5-000d3a102a21"
            ],
            "stepsSettingId": "a03f3252-d106-eb11-96f5-000d3a102a21"
        }
    ],
    "links": {},
    "totalCount": 1,
    "limit": 100,
    "offset": 0
}
```

## Retrieve Daily Statistics Setting

Returns a single Daily Statistics Setting by ID within the requested study.

**Request:**

```http
GET /analytics/v3/Studies/{studyId}/DailyStatisticsSettings/{dailyStatisticsSettingId}
```

**Response:**

|Field|Type|Description|
|-----|----|-----------|
|**id**|String (GUID)|Daily Statistic Setting ID|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|
|**wearPeriodSettingId**|String (GUID)|The ID of the Wear Period Algorithm Setting Used In the Daily Statistics|
|**sleepPeriodSettingId**|String (GUID)|The ID of the Sleep Period Algorithm Setting Used In the Daily Statistics|
|**epochSummarySettingId**|String (GUID)|The ID of the Epoch Algorithm Setting Used In the Daily Statistics|
|**cutpointSettingIds**|String Array (GUID)|The IDs of the Cutpoint Algorithm Settings Used In the Daily Statistics|
|**stepsSettingId**|String (GUID)|The ID of the Steps Algorithm Setting Used In the Daily Statistics (This property is only present if there is a steps algorithm associated with the Daily Statistics Setting)|
|**metsCaloriesSettingId**|String (GUID)|The ID of the METs/Calories Algorithm Setting Used In the Daily Statistics (This property is only present if there is a METs/Calories algorithm associated with the Daily Statistics Setting)|

**Response Example:**

```json
{
    "id": "ad1fda37-239d-48ad-581b-08d8556c9944",
    "studyId": 2775,
    "wearPeriodSettingId": "a13f3252-d106-eb11-96f5-000d3a102a21",
    "sleepPeriodSettingId": "116b5c9b-d106-eb11-96f5-000d3a102a21",
    "epochSummarySettingId": "3555504b-d106-eb11-96f5-000d3a102a21",
    "cutpointSettingIds": [
        "df777f61-d106-eb11-96f5-000d3a102a21"
    ],
    "stepsSettingId": "a03f3252-d106-eb11-96f5-000d3a102a21"
}
```
