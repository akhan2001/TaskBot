import os
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/tasks.readonly']

def authenticate_google():
    CREDENTIALS_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'credentials.json')

    if not os.path.exists(CREDENTIALS_FILE):
        raise FileNotFoundError(f"Credentials file not found at: {CREDENTIALS_FILE}")

    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
    creds = flow.run_local_server(port=0)
    return creds
