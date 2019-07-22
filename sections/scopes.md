# CentrePoint API Resource Scopes

## Scopes

When requesting an access token, you will need to provide the requested scope(s) to which the token should have access.

If desired you can request a token with access to more than one scope by adding each scope separated by a space (+ when Form URL encoded) to the scope parameter of the token request.

### Example

```http
POST /connect/token HTTP/1.1
Host: https://ag-auth-server-staging.azurewebsites.net
Content-Type: application/x-www-form-urlencoded

client_id=xxxxxxxxxx&client_secret=xxxxxxxxxx&scope=CentrePoint+DataRetrieval&grant_type=client_credentials
```

See [Authorization](authorization.md) for more info on requesting access tokens.

### CentrePoint Scope

The CentrePoint scope allows for:

* Retrieval of information about activity monitors in a CentrePoint study. (see [Activity Monitors](activity_monitors.md))
* Creating, ending, and retrieving information about subject activity monitor assignments. (see [Assignments](assignments.md))
* Retrieval of information about sites in a CentrePoint study. (see [Sites](sites.md))
* Retrieval of information about CentrePoint studies to which you have access. (see [Studies](studies.md))
* Retrieval of information about milestones in a CentrePoint study. (see [Study Milestones](study_milestones.md))
* Adding, editing, and retrieving information about subjects in a CentrePoint study. (see [Subjects](subjects.md))
* Retrieval of listing of webhook events. (see [Webhook Events](webhook_events.md))
* Retrieval of a list of the webhook subscriptions for a particular study as well as the history or webhook requests. (see [Webhooks](webhooks.md))

### DataRetrieval Scope

The data retrieval scope allows for:

* Generate raw activity data requests to retrieve raw activity data. (see [Raw Data Activity Requests](raw_data_request.md))
* Generate epoch data requests to retrieve epoch data. (see [Epoch Requests](epoch_data_requests.md))
