from googleapiclient.discovery import build
from app.services.google_auth import authenticate_google

def fetch_tasks():
    creds = authenticate_google()  # Google OAuth 授权
    service = build('tasks', 'v1', credentials=creds)
    
    tasks = []
    tasklists = service.tasklists().list().execute().get('items', [])
    
    for tasklist in tasklists:
        task_items = service.tasks().list(tasklist=tasklist['id']).execute().get('items', [])
        for task in task_items:
            tasks.append({
                'title': task.get('title', 'No Title'),
                'notes': task.get('notes', 'No Notes')
            })
    return tasks
