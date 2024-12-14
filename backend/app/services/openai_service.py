import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_suggestions(task_title, task_notes):
    prompt = f"Provide suggestions for:\nTask: {task_title}\nNotes: {task_notes}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].text.strip()
