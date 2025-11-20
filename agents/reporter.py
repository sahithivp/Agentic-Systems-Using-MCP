from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def reporter(hypothesis: str, evaluation: str):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a senior scientific reporting assistant specializing in "
                "drug discovery and computational biology. "
                "Your responsibility is to summarize agent outputs clearly, concisely, "
                "and without adding fabricated data. "
                "Follow strict scientific tone, avoid speculation beyond given inputs, "
                "and always provide structured, actionable insights."
            )
        },
        {
            "role": "user",
            "content": (
                "Create a structured technical summary based on the following inputs.\n\n"
                f"Hypothesis:\n{hypothesis}\n\n"
                f"Evaluation Results:\n{evaluation}\n\n"
                "Output Format:\n"
                "1. **Summary** – 3–5 sentence concise scientific summary.\n"
                "2. **Key Findings** – bullet points derived ONLY from inputs.\n"
                "3. **Recommended Next Experiments** – 2–4 concrete steps, "
                "including computational or wet-lab follow-ups.\n"
                "Avoid extra commentary. Do NOT invent new data or results."
            )
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.25,  
        max_tokens=300
    )

    return response.choices[0].message.content.strip()