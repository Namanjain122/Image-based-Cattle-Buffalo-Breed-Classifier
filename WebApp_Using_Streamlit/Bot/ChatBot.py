from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API"))
def ask_doctor(prompt):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{
            "role": "system", 
             "content": """
                You are MR. Doctor,
                an expert veterinary doctor
                specialized in cows and buffaloes.

                Provide:
                - disease guidance
                - feeding advice
                - cattle care
                - vaccination suggestions
                - breed-related information

                Keep answers practical and concise.
                """
        }, {
            "role": "user",
            "content": prompt
        }]
    )
    return response.choices[0].message.content