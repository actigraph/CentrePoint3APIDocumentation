# Visit Files

**NOTE: These requests require the *CentrePoint* API scope. (see [Scopes](scopes.md))**

## Upload Visit File

Provides an entry point for a .csv file with subject visit records for a given study.

A client upload of a .csv file of subject visits begins an import process into the ActiGraph CentrePoint system. When referring to the act of transferring a file into the CentrePoint system, we sometimes use the terms 'upload' and 'import' interchangeably. An upload file is therefore synonymous with an import file in this regard.

**Request:**

```http
POST /centrepoint/v3/Studies/{studyId}/ActualVisitFiles
Body is of type 'form-data'
```

**Request Body Parameters:**

|Field|Type|Description|
|-----|----|-----------|
|**file**|File|The subject visit file to upload/import (see [Visit File Format and Guidelines](#visit-file-format-and-guidelines))|

**Postman Example:**

![visit file postman post](images/visitfile_postman_post.png)

**Response:**

```json
{
    "actualVisitFileImportId": 1,
    "enqueuedDate": "2025-05-09T13:56:12.5386701Z",
    "fileName": "actual_visits_1.csv",
    "studyId": 523
}
```

**Response Body Fields:**

|Field|Type|Description|
|-----|----|-----------|
|**actualVisitFileImportId**|Number|ID given to the file import|
|**enqueuedDate**|String (ISO8601 Date)|UTC Date/Time of when the import process was enqueued|
|**fileName**|String|The original name of the file when uploaded|
|**studyId**|Number|CentrePoint Study ID (see [Studies](studies.md))|

## List Visit File Imports

Returns a list of visit file imports that have taken place or are currently in process within a study.

**Request:**

```http
GET /centrepoint/v3/Studies/{studyId}/ActualVisitFiles/Imports
```

**Response:**

This response is paginated. See [Pagination](pagination.md) for a description of pagination related fields returned.

|Field|Type|Description|
|-----|----|-----------|
|**actualVisitFileImportId**|Number|Visit file import ID|
|**enqueuedDate**|String (ISO8601 Date)|Enqueued Date of the import|
|**importStartedDate**|String (ISO8601 Date)|Started Date of the import|
|**importCompletionDate**|String (ISO8601 Date)|Completion Date of the import|
|**fileName**|String|The name of the original upload file.|
|**studyId**|Number|CentrePoint Study ID.|
|**downloadUrl**|String|The signed URL that can be used to download the imported visit file.|
|**failureMessage**|String|If a failure exists, indicates what kind of error(s) may have occurred to result in said failure.|
|**detailedErrors**|Array|If requested, provides a list of errors by record (not included in the JSON below, see the Query Parameters section for a JSON example response that includes this in the result). See [Visit File Format and Guidelines](#visit-file-format-and-guidelines) for validation errors one can expect to see here because of missing or badly formatted data and/or headers.|

```json
{
    "items": [
        {
            "actualVisitFileImportId": 3,
            "enqueuedDate": "2025-05-09T14:34:33.07Z",
            "importStartedDate": "2025-05-09T15:20:33.083Z",
            "importCompletionDate": "2025-05-09T15:20:38.943Z",
            "fileName": "actual_visits_1.csv",
            "studyId": 523,
            "downloadUrl": "https://agcpstorage.blob.core.windows.net/actual-visit-files/study-0000000523/actual_visits_1-76d560cf-4b7f-4580-b788-1dac8ef3e972.csv?sv=2023-11-03&se=2025-05-09T19%3A45%3A32Z&sr=b&sp=r&rscd=attachment%3Bfilename%3Dactual_visits_1.csv&sig=JLxAhlIxXdgHddXxxxA#rtYjbyM%3D",
            "failureMessage": "Unable to read file, a catastrophic error was detected - One or more critical file format validation error(s) occurred, see read errors in Data property for more information."
        },
        {
            "actualVisitFileImportId": 4,
            "enqueuedDate": "2025-05-09T15:21:40.297Z",
            "importStartedDate": "2025-05-09T15:21:42.217Z",
            "importCompletionDate": "2025-05-09T15:21:43.487Z",
            "fileName": "actual_visits_1 - PASS.csv",
            "studyId": 523,
            "downloadUrl": "https://agcpstorage.blob.core.windows.net/actual-visit-files/study-0000000523/actual_visits_1%20-%20PASS-cdd71511-78c9-4071-b3ce-3da88e0a6435.csv?sv=2023-11-03&se=2025-05-09T19%3A45%3A32Z&sr=b&sp=r&rscd=attachment%3Bfilename%3Dactual_visits_1+-+PASS.csv&sig=JLxAhlIxXdgHddXxxxA#rtYjbyM%3D"
        }
    ],
    "links": {
        "prev": "https://[localhost:53033]/Studies/523/ActualVisitFiles/Imports?limit=2&offset=0&ImportCompletionDate=5%2F09%2F2025"
    },
    "totalCount": 2,
    "limit": 2,
    "offset": 2
}
```

**Query Parameters:**

Query parameters include filters that can be applied to narrow the search for imports, and a flag for additional details.

|Field|Type|Description|Default Value|
|-----|----|-----------|-------------|
|**IsFailedOnly**|Boolean|When true, returns failed imports only|false|
|**DetailedErrors**|Boolean|When true, returns a list of all errors (seperated by '\|') on each visit file record and the record's location in the file (row number) if errors exist|false|
|**ImportCompletionDate**|String (ISO8601 Date)|Completion Date of the import (Date only)|null|
|**ImportCompletionDateTime**|String (ISO8601 Date)|Completion Date and Time of the import|null|

**Example Filtered Request:**

```http
GET /centrepoint/v3/Studies/523/ActualVisitFiles/Imports?IsFailedOnly=true&DetailedErrors=true&ImportCompletionDate=5/09/2025&ImportCompletionDateTime=2025-05-09T16:17:18.31Z
```

**Response:**

```json
{
    "items": [
        {
            "actualVisitFileImportId": 8,
            "enqueuedDate": "2025-05-09T16:17:15.827Z",
            "importStartedDate": "2025-05-09T16:17:17.223Z",
            "importCompletionDate": "2025-05-09T16:17:18.31Z",
            "fileName": "actual_visits_multiple_errors_per_row.csv",
            "studyId": 523,
            "downloadUrl": "https://agcpstorage.blob.core.windows.net/actual-visit-files/study-0000000523/actual_visits_multiple_errors_per_row-3c9c6b55-0033-41fa-8b60-6c003392057f.csv?sv=2023-11-03&se=2025-05-09T20%3A18%3A33Z&sr=b&sp=r&rscd=attachment%3Bfilename%3Dactual_visits_multiple_errors_per_row.csv&sig=Fs6GgGggXxxXXSKxuetZJA7I%2xxXxxxXxXlh8%3D",
            "failureMessage": "One or more validation errors occurred, see Data property or row errors for more information. Subjects Default-1st and Default-2nd (Site-Subject) have been excluded from the results.",
            "detailedErrors": [
                {
                    "rowNumber": 3,
                    "errorMessages": "PlannedVisitEntry: The subject visit date provided in the record '5/22/2025' is in the future. | The visit date '22-May-25' in this record is beyond the subject status change to a 'Completed' date of '5/21/2023'. A visit date cannot be after a Completed status date."
                },
                {
                    "rowNumber": 11,
                    "errorMessages": "StudySubjectStatus: The subject status date provided in this record '11th of January, 2024' cannot be parsed into a date. | Subject '2nd' in Site 'Default' has a Completed status date '11th of January, 2024' that has changed from a previous record's Completed status date of '9/3/2024'. Completed status dates cannot change. | PlannedVisitEntry: The visit date provided in this record '21st of May, 2024' cannot be parsed into a date."
                }
            ]
        }
    ],
    "links": {},
    "totalCount": 1,
    "limit": 100,
    "offset": 0
}
```

## Get Visit File Import by ID

Returns a visit file import download URL and its metadata within a study. Can optionally contain a query parameter that signals whether detailed errors (errors by row) shall be returned.

**Request:**

```http
GET /centrepoint/v3/Studies/523/ActualVisitFiles/Imports/3?DetailedErrors=true
```

**Response:**

```json
{
            "actualVisitFileImportId": 8,
            "enqueuedDate": "2025-05-09T16:17:15.827Z",
            "importStartedDate": "2025-05-09T16:17:17.223Z",
            "importCompletionDate": "2025-05-09T16:17:18.31Z",
            "fileName": "actual_visits_multiple_errors_per_row.csv",
            "studyId": 523,
            "downloadUrl": "https://agcpstorage.blob.core.windows.net/actual-visit-files/study-0000000523/actual_visits_multiple_errors_per_row-3c9c6b55-0033-41fa-8b60-6c003392057f.csv?sv=2023-11-03&se=2025-05-09T20%3A18%3A33Z&sr=b&sp=r&rscd=attachment%3Bfilename%3Dactual_visits_multiple_errors_per_row.csv&sig=Fs6GgGggXxxXXSKxuetZJA7I%2xxXxxxXxXlh8%3D",
            "failureMessage": "One or more validation errors occurred, see Data property or row errors for more information. Subjects Default-1st and Default-2nd (Site-Subject) have been excluded from the results.",
            "detailedErrors": [
                {
                    "rowNumber": 3,
                    "errorMessages": "PlannedVisitEntry: The subject visit date provided in the record '5/22/2025' is in the future. | The visit date '22-May-25' in this record is beyond the subject status change to a 'Completed' date of '5/21/2023'. A visit date cannot be after a Completed status date."
                },
                {
                    "rowNumber": 11,
                    "errorMessages": "StudySubjectStatus: The subject status date provided in this record '11th of January, 2024' cannot be parsed into a date. | Subject '2nd' in Site 'Default' has a Completed status date '11th of January, 2024' that has changed from a previous record's Completed status date of '9/3/2024'. Completed status dates cannot change. | PlannedVisitEntry: The visit date provided in this record '21st of May, 2024' cannot be parsed into a date."
                }
            ]
        }
```

## Visit File Format and Guidelines

**Note:**  *All visit files stored in CentrePoint storage have a retention period of 90 days. After this time has lapsed for a file, the file and its associated metadata will be permanently removed from all ActiGraph resources.*

Visit files imported into ActiGraph's CentrePoint system must be in the format described below:

* All visit files must contain a header with each of the following columns spelled exactly as written:
  * **Study ID** - the name of the study in question in CentrePoint (not the internal study ID).
  * **Site** - the site within the study affiliated with the subject visit record.
  * **Subject** - the study's subject that partook in the visit.
  * **Subject Status** - the status of the subject in the study for that visit.
  * **Subject Status Date** - the date the subject status was given.
  * **Visit Name** - the name of the visit in which this record applies.
  * **Visit Date (DOV)** - the date of the visit in this record.
* Any other columns in the file will be ignored.
* The fields under the Study ID, Site, and Subject columns in the visit file are the **CentrePoint** identifiers for study, site, and subject (IE name of the study, subject, and site stored in the **CentrePoint system**).
* There is a max file size of **10MB** for files uploaded to the public API. It is expected the content of these visit files should never surpass this.
* All dates - subject status date, visit date - are expected to be in the form **dd-MMM-yyyy**, but can be in any standard national date format.
* A max of 10 (ten) duplicate errors will be stored and returned from our GET endpoints.  The remaining duplicates will be truncated.
* Only **.csv** files will be accepted by the API.  An exception will be returned otherwise.
* The study used in the file upload/import must be an active study (not hard locked).
* Visits must be defined in study configurations (this configuration value must be set to true). Contact ActiGraph support for changes in this configuration.

**Validation:**

All visit files will undergo a process of validation before entries are inserted into the database.  These validation errors will be reported on each import, with details such as the row number of the invalid record along with all errors found. All records that are considered 'wear' visits must have a corresponding visit name and subject status in ActiGraph storage prior to the import.

The following list describes some of the possible validation errors that can be returned:

* **StudyDoesNotExist -** "The study ID '{0}' given to the folder containing this visit file does not exist."
* **FileStudyNameDoesNotMatch -** "The study ID '{0}' given to the folder containing this visit file has a study name '{1}' that does not match the study name '{2}' of this record."
* **VisitsNotDefined -** "Visits are not defined for the study in this record."
* **SubjectDoesNotExist -** "The subject '{0}' in this record does not exist for study '{1}' and site '{2}', or the subject has no subject status."
* **SubjectStatusDoesNotExist -** "For subject '{0}', the subject status of '{1}' in this record does not exist in the database. Available subject statuses: {2}."
* **UnableToParseStatusDate -** "The subject status date provided in this record '{0}' cannot be parsed into a date."
* **StatusDateInFuture -** "The subject status date provided in the record '{0}' is in the future."
* **VisitDateInFuture -** "The subject visit date provided in the record '{0}' is in the future."
* **SubjectInLockedState -** "The subject '{0}' in this record is currently in a locked state and cannot accept anymore data until unlocked."
* **VisitDateIsNotUnique -** "The visit date '{0}' for subject '{1}' is not unique. A subject can have no more than one visit a day."
* **UnableToParseVisitDate -** "The visit date provided in this record '{0}' cannot be parsed into a date."
* **NullStudyName -** "An empty or null study name was identified in the record. Because we cannot identify the study this record applies to, an accurate visit history of any subject in the study cannot be determined."
* **StudyNameChanged -** "The study name in the visit file changed. Each visit file should have an association with only one study. An accurate visit history of any subject in the study cannot be determined."
* **MissingSubjectIdentifier -** "Subject is null or empty. It is not possible to determine an accurate visit history of this subject or for what subject this record applies to - Unable to process file."
* **NoBaselineVisits -** "Subject '{0}' does not have a baseline visit. All subjects must have a baseline visit."
* **OutOfOrderDays -** "The visit day '{0}' or its corresponding visit date '{1}' in this record is in an unexpected order compared to these same properties in other records. Visit days and their dates should be ordered sequentially."
* **CompletedStatusDateChanged -** "Subject '{0}' in Site '{1}' has a Completed status date '{2}' that has changed from a previous record's Completed status date of '{3}'. Completed status dates cannot change."
* **VisitDateBeyondStatusCompleteDate -** "The visit date '{0}' in this record is beyond the subject status change to a 'Completed' date of '{1}'. A visit date cannot be after a Completed status date."
* **StudyIsHardlocked -** "Study {0} is hard locked. Importing or modifying visit files in a hard locked study is not allowed."
