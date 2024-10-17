# TaskBot

TaskBot is an automated task assistant designed to read tasks from Google Tasks, generate suggestions for each task using the OpenAI API, and send a daily email with those suggestions. The project also supports manually defining tasks instead of retrieving them from Google Tasks.

## Features

- Retrieve tasks from Google Tasks
- Use OpenAI API to generate relevant suggestions for each task
- Send daily task suggestions via email

## Manually Defining Tasks

If you prefer not to retrieve tasks from Google Tasks, you can manually define your tasks directly in the script. Simply create a list of tasks, each with a title and description, and replace the section that fetches tasks from Google. 

For example, you could define tasks like:

- **Task**: "Create TaskBot"
  - **Description**: "TaskBot reads tasks from Google Tasks, generates suggestions for each task using OpenAI API, and sends a daily email with those suggestions."
  
- **Task**: "Reply to Professor's email"
  - **Description**: "none"
  
- **Task**: "Do 5 questions on leetcode"
  - **Description**: "Review dynamic programming algorithms"

After defining your tasks, the program will generate suggestions and email them just as it would if the tasks came from Google Tasks.

## Setting Up the Environment Variables

Before running the project, you need to set up the environment variables to store sensitive information, such as your OpenAI API key and email password. This information should be placed in a `.env` file in the root directory of your project.

### Steps to Set Up `.env` File

1. Create a `.env` file in the root directory of your project (in the same location as `task.py`).
2. Add the following keys to the `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
EMAIL_PASSWORD=your_email_password_here
LANGUAGE=English
SENDER=sender_email@gmail.com
RECEIVER=receiver_email@gmail.com
