# Subject Activity Monitor Assignment Workflow

The CentrePoint API supports creating and ending an activity monitor assignment for a subject.

**NOTE: The assignment workflow requires the *CentrePoint* API scope. (see [Scopes](scopes.md))**

Your study must be configured to *Allow Partial Monitor Assignment Workflow*. Contact ActiGraph for more information.

1. With *Allow Partial Monitor Assignment Workflow* enabled on your study, you can create a partial assignment through the *Create Study Subject Activity Monitor Assignment* API request (see [Assignments](assignments.md)).
1. You must complete the assignment by docking the activity monitor with ActiSync or with a CentrePoint Data Hub.
1. The activity monitor will now be collecting activity data.
1. You may stop collecting by making a request to the *Change Study Subject Activity Monitor Assignment Status* endpoint  (see [Assignments](assignments.md)). During normal usage this will place the activity monitor into the *Collection Stopped* state. The activity monitor will stop activity collection. It is also possible to force end an assignment by setting the assignment status to *Forcefully Ended*, however this should only be performed when an activity monitor cannot go through the normal workflow (i.e. activity monitor is lost or broken).
1. You can now end the assignment by docking the activity monitor with ActiSync or with a CentrePoint Data Hub to perform the final data upload to collect any remaining data on the activity monitor.

Your study may be configured to automatically stop collection after a set time period. This will show as **scheduledCollectionStopDate** when looking at assignment information returned from the API. Contact [ActiGraph](http://www.actigraphcorp.com/support/contact-support/) for more information on this feature.
