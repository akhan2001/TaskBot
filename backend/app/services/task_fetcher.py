from googleapiclient.discovery import build
from app.services.google_auth import authenticate_google

def fetch_tasks():
    creds = authenticate_google()
    service = build('tasks', 'v1', credentials=creds)
    tasklists = service.tasklists().list().execute().get('items', [])
    
    tasks = []
    for tasklist in tasklists:
        result = service.tasks().list(tasklist=tasklist['id']).execute()
        task_items = result.get('items', [])
        for task in task_items:
            tasks.append({
                'title': task.get('title', 'No Title'),
                'notes': task.get('notes', 'No Description')
            })
    return tasks
