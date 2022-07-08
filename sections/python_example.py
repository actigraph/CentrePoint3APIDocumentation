import requests
import time


CLIENT_ID = '<YOUR CLIENT ID PROVIDED BY ACTIGRAPH>'
CLIENT_SECRET = '<YOUR CLIENT SECRET PROVIDED BY ACTIGRAPH>'

AUTH_URL = 'https://auth.actigraphcorp.com/connect/token'
API_URL = 'https://api.actigraphcorp.com'


def request_accesstoken():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    params = {
        'client_id':        CLIENT_ID,
        'client_secret':    CLIENT_SECRET,
        'scope':            'CentrePoint Analytics',
        'grant_type':       'client_credentials'
    }
    response = requests.post(AUTH_URL, data=params, headers=headers).json()
    try:
        access_token = response['access_token']
    except KeyError:
        print('Access Token not aquired. Check your credentials and try again.')
        quit()
    nr_requests = 1

    return access_token, nr_requests


# This function will handle all requests and can be passed the URL for the desired call.
def make_request(call, access_token, nr_requests):
    nr_requests += 1 
    if nr_requests == 10: #  if we have made 9 requests, we need to wait for a second, in order to not exceed the maximum of 10 requests per second.
        time.sleep(1.1)
        nr_requests = 0

    session = requests.session()
    session.headers = {'Authorization': f'Bearer {access_token}'}

    response = session.get(call).json() 
    return response, nr_requests


if __name__ == '__main__':
    access_token, nr_requests = request_accesstoken()
    print('Access Token aquired.')

    # Example 1: returns details of all studies you have access to.
    call = f'{API_URL}/centrepoint/v3/studies'
    response, nr_requests = make_request(call, access_token, nr_requests=1)
    print(response)

    studyID = response['items'][0]['id'] #  Get the ID of the first study
    print(studyID)

    # Example 2: returns a list of all participants in the first study we have access to.
    call = f'{API_URL}/centrepoint/v3/studies/{studyID}/Subjects'
    response, nr_requests = make_request(call, access_token, nr_requests)
    print(response)

    for subject in response['items']: #  Print the ID of each participant
        print(subject['id'])

