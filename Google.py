
import os.path
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import googleapiclient.errors

# This code was taken from the quickstart.py
# example for Google Sheets. You can find it here:
# https://developers.google.com/sheets/api/quickstart/python
def Create_Service(client_secret_file, api_name, api_version, scopes):
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build(api_name, api_version, credentials=creds)

    print(api_name, 'Created service successfully!\n')
    return service
