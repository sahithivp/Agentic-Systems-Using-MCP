from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def research_planner(topic: str):
    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert drug-discovery research planner. "
                "Your job is to generate precise, biologically-plausible hypotheses. "
                "Focus on molecular mechanisms, protein targets, pathways, and potential interactions. "
                "Output MUST be:\n"
                "1. A single hypothesis (one sentence)\n"
                "2. Scientifically grounded\n"
                "3. Direct, with no extra commentary"
            )
        },
        {
            "role": "user",
            "content": (
                f"Generate a drug-discovery hypothesis based on the topic:\n"
                f"\"{topic}\".\n"
                "Format:\n"
                "Hypothesis: <one sentence only>"
            )
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.3,   
        max_tokens=150
    )

    return response.choices[0].message.content.strip()