import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_answer(context, question):
    print("Calling LLM...")
    prompt = f"""
    You are a helpful assistant.
    Use ONLY the context below to answer the question.
    If the answer is not in the context, say:
    "I don't know based on the provided document."

    Context:
    {context}

    Question:
    {question}
    
    Answer:
    
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content