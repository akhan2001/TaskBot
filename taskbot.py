import os
import smtplib
import datetime

from openai import OpenAI
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/tasks.readonly']
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SENDER_EMAIL = os.getenv("SENDER")
RECEIVER_EMAIL = os.getenv("RECEIVER")
LANGUAGE = os.getenv("LANGUAGE")
password = os.getenv("EMAIL_PASSWORD")
client = OpenAI(api_key=OPENAI_API_KEY)


def authenticate_google():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return creds

def get_tasks():
    creds = authenticate_google()
    service = build('tasks', 'v1', credentials=creds)

    tasks = []
    results = service.tasklists().list().execute()
    tasklists = results.get('items', [])

    for tasklist in tasklists:
        result = service.tasks().list(tasklist=tasklist['id']).execute()
        task_items = result.get('items', [])

        for task in task_items:
            title = task.get('title', 'no task')            # task.get('key', 'default value')
            notes = task.get('notes', 'no description')
            tasks.append({
                'title': title,
                'notes': notes
            })

    return tasks

def generate_suggestions(task_title, task_notes):
    prompt = f"Please provide some suggestions for the following task in {LANGUAGE}:\nTask: {task_title}\nDescription: {task_notes}\nPlease provide suggestions to help complete this task better. In the first line of your response, state the estimated time required to complete this task."

    response = client.chat.completions.create(
        model="gpt-4o", 
        messages=[
            {"role": "system", "content": f"You are an assistant specializing in providing suggestions for tasks in {LANGUAGE}."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200,          
        temperature=0.7        
    )
    return response.choices[0].message.content.strip()

def send_email(task_suggestions):
    sender_email = SENDER_EMAIL
    receiver_email = RECEIVER_EMAIL

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = f"Daily Suggestions From <TASKBOT> - {datetime.date.today()}"

    body_content = "<h3>Here are your tasks and suggestions for today ~~~ :</h3><br>"
    for task in task_suggestions:
        body_content += f"<b>TASK</b>: {task['title']}<br>"
        body_content += f"<b>SUGGESTION</b>:<br>"

        suggestion_lines = task['suggestion'].split('\n')
        for line in suggestion_lines:
            body_content += f"{line.strip()}<br>"
        body_content += "<hr>"

    message.attach(MIMEText(body_content, 'html'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == "__main__":
    print("-----------Getting TASKS-----------------")
    # tasks = get_tasks()

    # Define Tasks Manually Here
    tasks = [
        {
            'title': 'Morning Routine',
            'notes': 'Complete your morning routine including exercise, breakfast, and planning for the day.'
        },
        {
            'title': 'Pray',
            'notes': 'Set aside time for prayer and reflection.'
        },
        {
            'title': 'Quran',
            'notes': 'Read and reflect on a portion of the Quran.'
        },
        {
            'title': 'DevOps Study',
            'notes': 'Spend time studying DevOps practices and tools.'
        }
    ]

    print("-----------Taskbot is making suggestions for YOU----------------")
    task_suggestions = []
    for task in tasks:
        title = task['title']
        notes = task['notes']
        suggestion = generate_suggestions(title, notes)
        task_suggestions.append({
            'title': title,
            'notes': notes,
            'suggestion': suggestion
        })

    print("-----------Let's see the suggestions-------------------")
    for task in task_suggestions:
        print(f"Task Title: {task['title']}")
        print(f"Notes: {task['notes']}")
        print(f"Suggestions from TaskBot: {task['suggestion']}")
        print("\n" + "-"*50 + "\n")

    print("----------------Sending Email---------------------")
    send_email(task_suggestions)