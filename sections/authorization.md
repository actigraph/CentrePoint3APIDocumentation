# Authorization

In order to acccess the CentrePoint API, you must have [ActiGraph](http://www.actigraphcorp.com/support/contact-support/) enable API access for your account. ActiGraph will generate and provide you with a "*client ID*" and "*client secret*."  This key pair is what you will use to retrieve an access token. The access token must be sent in the authorization header of each request to the CentrePoint API.

### Keep Your API Credentials Safe

Remember that anyone who has your client ID and client secret can see and change everything you have access to. So you want to guard that as well as you guard your username and password.  If this key pair becomes compromised, [contact us](http://www.actigraphcorp.com/support/contact-support/) immediately and we can deactivate it and provide you a new one.

### Example in Python

Refer to [this script](./python_example.py) to see an example on how to access the access token and make an authorized request in Python. 

## Retrieving an Access Token

To retrieve an access token, you will need to make a POST request to the ActiGraph authorization token endpoint. [https://auth.actigraphcorp.com/connect/token](https://auth.actigraphcorp.com/connect/token)

The content type should be set to *application/x-www-form-urlencoded*
The body should contain your *client ID*, *client secret*, a *scope* set to a valid scope for the resource(s) you wish to access, and a *grant_type* set to *client_credentials*.

|Parameter|Description|
|---------|-----------|
|**client_id**|the client ID provided to you by ActiGraph|
|**client_secret**|the client secret provided to you by ActiGraph|
|**grant_type**|The grant_type parameter must be set to client_credentials.|
|**scope**|a scope set to a valid scope for the resource(s) you wish to access (see [Scopes](scopes.md))|

#### Example Access Token Request

```http
POST /connect/token HTTP/1.1
Content-Type: application/x-www-form-urlencoded

client_id=xxxxxxxxxx&client_secret=xxxxxxxxxx
    &scope=CentrePoint&grant_type=client_credentials
```

#### Example Access Token Response

**access_token** The access token string as issued by the authorization server. This will be used to authorize all requests to the API.
**token_type** “Bearer”.
**expires_in** The duration of time the access token is granted for in seconds.

```json
{
    "access_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjcxNThCNjY4NjBFM...",
    "expires_in": 3600,
    "token_type": "Bearer"
}
```

## Authorized Request

All requests will be authorized by including the HTTP authorization header.  The scheme is set to "Bearer", and the parameter is your access token.

See the following example:

```http
GET /centrepoint/v3/Studies HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```
