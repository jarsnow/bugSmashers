import os
from dotenv import load_dotenv
from groq import Groq

# load API key
load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


# ask user a question
prompt = input("ask me a question: ")
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)
