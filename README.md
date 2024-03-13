# CentrePoint (V3) API Documentation

## Overview

The CentrePoint API was developed to provide other software systems a web interface to the study admin web portal. The API provides access to the same core study and de-identified subject data that can be accessed within [CentrePoint](http://studyadmin.actigraphcorp.com).

API Base URL: [https://api.actigraphcorp.com](https://api.actigraphcorp.com)

Authorization Base URL: [https://auth.actigraphcorp.com](https://auth.actigraphcorp.com)

## Enabling API Access

Please contact [ActiGraph](http://www.actigraphcorp.com/support/contact-support/) for more information.

### Authorization

The CentrePoint API uses [OAuth 2.0](https://oauth.net/2/) for its authorization flow.

 Refer to the [Authorization](./sections/authorization.md) section for specifics and examples.

## API Resources

#### CentrePoint (General)

* Retrieval of information about CentrePoint studies to which you have access. (see [Studies](./sections/studies.md))
* Retrieval of information about sites in a CentrePoint study. (see [Sites](./sections/sites.md))
* Adding, editing, and retrieving information about subjects in a CentrePoint study. (see [Subjects](./sections/subjects.md))
* Retrieval of information about activity monitors in a CentrePoint study. (see [Activity Monitors](./sections/activity_monitors.md))
* Creating, ending, and retrieving information about subject activity monitor assignments. (see [Subject Activity Monitor Assignment Workflow](./sections/assignment_workflow.md) and [Assignments](./sections/assignments.md))
* Retrieving information about uploads for a CentrePoint subject. (see [Uploads](./sections/uploads.md))
* Retrieval of information about milestones in a CentrePoint study. (see [Study Milestones](./sections/study_milestones.md))
* Retrieval of listing of webhook events. (see [Webhook Events](./sections/webhook_events.md))
* Retrieval of a list of the webhook subscriptions for a particular study as well as the history or webhook requests. (see [Webhooks](./sections/webhooks.md))

#### Large Data File Access

* Access to pre-made day files of large study data like raw accelerometer data. (see [Data Access Files](./sections/data_access_files.md))

#### Export DataSet Files

* Access to DataSet Export files for a particular Study Id, Study Program combination. (see [DataSet Export Files](./sections/data_set_files.md))
* Access to DataSet Export subjects for a particular Study Id. (see [DataSet Export Subjects](./sections/data_set_export_subjects.md))

#### Analytics/Algorithmic Data-Retrieval

* Retrieval of Analytics Algorithm Settings. (see [Algorithm Settings](./sections/algorithm_settings.md))
* Retrieval of Epochs/Minute Summary Data. (see [Minute Summary](./sections/minute_summary.md))
* Retrieval of Daily Summary Data. (see [Daily Statistics](./sections/daily_statistics.md))
* Retrieval of (Dustin Tracy) Sleep Periods. (see [Dustin Tracy Sleep Periods](./sections/dustin_tracy_sleep_periods.md))
* Retrieval of CPW01 Insight Watch button press/release Events (or 'Event Markers'). (see [Event Markers](./sections/event_markers.md))

#### RAW Sub-second Activity Data Retrieval

* Generate raw (sub-second) activity data requests to retrieve raw activity data for a given subject. (see [Raw Data Activity Requests](./sections/raw_data_request.md)) **Note:** It is now recommended to use the [Data Access Files](./sections/data_access_files.md) for retrieving raw accelerometer data.

### JSON

This is a [JSON](http://tools.ietf.org/html/rfc4627) API. When sending Http requests you must supply the Content-Type field within the header as  “application/json” on PUT and POST operations. If an error occurs, you may receive a text/plain response, e.g. a 400 bad request response indicates you will need to take action.

### HTTPS

Any non-[HTTPS](http://tools.ietf.org/html/rfc2818) request will result in a Forbidden response.

### Date Formatting

* All dates will adhere to [ISO 8601](http://www.w3.org/TR/NOTE-datetime). So when sending Http requests you must supply the Date field in ISO 8601.
* Dates in **UTC** will consist of a the trailing 'Z' character (example: 2016-06-14T20:46:00Z).
* Dates where the trailing 'Z' is withheld will signify that the date should be interpreted in the **subject's timezone**.

### Request Limiting

This API is request limited. We only allow a certain number of requests from each unique IP address. If an API consumer exceeds 500 requests within a minute, then the API will block any further requests with a 429 response code. This rate limit is a sliding window and the 429 response message will include a Retry-After header that will indicate the amount of seconds to wait before retrying the request.

## CentrePoint Integration Guide

To view ALL options/alternatives to integrate with the CentrePoint System, refer to the [CentrePoint Integration Guide](https://github.com/actigraph/CentrePointIntegrationGuide).
