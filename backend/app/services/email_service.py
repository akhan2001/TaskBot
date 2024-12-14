import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_task_email(task_suggestions):
    sender_email = os.getenv("SENDER")
    receiver_email = os.getenv("RECEIVER")
    password = os.getenv("EMAIL_PASSWORD")

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Daily Task Suggestions"

    body = "<h3>Here are your task suggestions:</h3>"
    for task in task_suggestions:
        body += f"<b>Task:</b> {task['title']}<br><b>Suggestion:</b> {task['suggestion']}<br><hr>"
    
    message.attach(MIMEText(body, 'html'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
