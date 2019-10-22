# Epoch Data File Formats

* CSV - Comma Separated Values


-----

## CSV

Standard comma separated values format.

**Header:**

* StudyId
* SubjectId
* DeviceSerial
* Timestamp
* X
* Y
* Z
* HeartRate
* Capsense
* Lux
* Steps

**Columns:**

|Column|Description|Notes|
|------|-----------|-----------|
|**Study Id**|Study Id of subject||
|**Subject Id**|Subject Id||
|**Device Serial**|Activity Monitor Serial Number||
|**Timestamp**|UNIX (UTC) timestamp in seconds||
|**X**|Axis X Counts||
|**Y**|Axis Y Counts||
|**Z**|Axis Z Counts||
|**HeartRate**|Heart Rate Sensor Reading|***Field Not Supported***|
|**Capsense**|Capacitive Touch Sensor Reading|***Field Not Supported***|
|**Lux**|Lux|***Field Not Supported***|
|**Steps**|Steps|***Field Not Supported***|
