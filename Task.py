#import func_getevents
#import googlecarender

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/tasks']

def getTask():
    """Shows basic usage of the Tasks API.
    Prints the title and ID of the first 10 task lists.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('tasks', 'v1', credentials=creds)

    # Call the Tasks API
    results = service.tasklists().list(maxResults=10).execute()
    items = results.get('items', [])

    # if not items:
    #     print('No task lists found.')
    # else:
    #     # print('Task lists:')
    #     for item in items:
    #         print(u'{0} ({1})'.format(item['title'], item['id']))
    
    tasks = service.tasks().list(tasklist='@default').execute()
    if "items" in tasks: 
        for task in tasks['items']:
            if "notes" in task and "due" in task:
                pos = task["position"][-2:]
                word = task["due"][5:10]
                print('*',pos,word,task['title'],"\n",task["notes"])
            elif not "notes" in task:
                print("*", task["title"])
    else:
        print("Not any task")
    
def setTask(title,notes,month,day):
    """Shows basic usage of the Tasks API.
    Prints the title and ID of the first 10 task lists.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('tasks', 'v1', credentials=creds)

    task = {
    'title': title,
    'notes': notes, 
    # 'due': '2019-09-09T21:00:00.000Z'
    "due": "2019-" + month + "-" + day + "T12:00:00.000Z"
    }
    result = service.tasks().insert(tasklist='@default', body=task).execute()
    print ("Created a new task,", result['title'])

def deleteTask(pos):
    """Shows basic usage of the Tasks API.
    Prints the title and ID of the first 10 task lists.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('tasks', 'v1', credentials=creds)

    tasks = service.tasks().list(tasklist='@default').execute()
    for task in tasks['items']:
        posTarget = task["position"][-2:]
        if  posTarget == pos:
            print("Deleted task ->",task["title"])
            service.tasks().delete(tasklist='@default', task=task["id"]).execute()
           
            