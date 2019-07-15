# Subject Activity Monitor Assignment Workflow

The CentrePoint API supports creating and ending an activity monitor assignment for a subject.

**NOTE: The assignment workflow requires the *CentrePoint* API scope. (see [Scopes](scopes.md))**

Your study must be configured to *Allow Partial Monitor Assignment Workflow*. Contact ActiGraph for more information.

1. With *Allow Partial Monitor Assignment Workflow* enabled on your study, you can create a partial assignment through the *Create Study Subject Device Assignment* API request (see [Assignments](assignments.md)).
1. You must complete the assignment by docking the device with ActiSync or with a CentrePoint Data Hub.
1. The activity monitor will now be collecting activity data.
1. You may stop collecting by making a request to the *Change Study Subject Device Assignment Status* endpoint  (see [Assignments](assignments.md)).
1. The device will stop activity collection.
1. You can end the assignment by docking the activity monitor with ActiSync or with a CentrePoint Data Hub to perform the final data upload.
