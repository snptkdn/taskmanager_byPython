from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def main(starttime,endtime,title):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle_calendar'):
        with open('token.pickle_calendar', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle_calendar', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # 登録イベントに記念日と日付を設定
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    event = {
        'summary': title,
        'start': {
            'dateTime': starttime,
            'timeZone': 'Asia/Tokyo',
        },
        'end': {
            'dateTime': endtime,
            'timeZone': 'Asia/Tokyo',
        },
    }

    # 記念日を登録するGoogleカレンダーIDをcalendarIdに指定し、イベントを登録する
    event = service.events().insert(calendarId="primary", body=event).execute()
    if event:
        print("set task",event['start'].get('dateTime'), event['summary'])
    else:
        print('Failed to add an anniversary.')

if __name__ == '__main__':
    main()