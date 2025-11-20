from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def research_planner(topic: str):
    prompt = f"""
    You are a research planner in drug discovery.
    Formulate a hypothesis about {topic}, e.g. "Molecule X may inhibit Protein Y".
    Return hypothesis as a short sentence.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
