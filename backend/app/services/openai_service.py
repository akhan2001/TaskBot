import openai
import os

from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_suggestions(task_title, task_notes, language="English"):
    prompt = (
        f"Please provide some suggestions for the following task in {language}:\n"
        f"Task: {task_title}\nDescription: {task_notes}\n"
        f"Please provide suggestions to help complete this task better. "
        f"In the first line of your response, state the estimated time required to complete this task."
    )
    print("Generated Prompt:", prompt)

    try:
        print("Attempting to call OpenAI API...")
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": f"You are an assistant specializing in providing suggestions for tasks in {language}."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )
        print("OpenAI API Response:", response)
        return response.choices[0].message["content"].strip()

    except openai.error.OpenAIError as e:
        print(f"OpenAI API Error: {str(e)}")
        raise RuntimeError(f"OpenAI API error: {str(e)}")

    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
        raise RuntimeError(f"Unexpected error: {str(e)}")
