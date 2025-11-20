from fastapi import FastAPI
from agents.research_planner import research_planner
from agents.retriever import retriever
from agents.molecular_simulator import molecular_simulator
from agents.evaluator import evaluator
from agents.reporter import reporter
import asyncio

app = FastAPI(title="Agentic Scientific Research System")

@app.get("/")
def home():
    return {"message": "Welcome to Autonomous Research Agent API"}

@app.post("/chat")
async def chat_with_agent(topic: str):
    hypothesis = research_planner(topic)

    papers = retriever(hypothesis)

    sim_result = await molecular_simulator("Molecule X", "Protein Y")

    evaluation = evaluator(sim_result)

    report = reporter(hypothesis, evaluation)

    return {
        "hypothesis": hypothesis,
        "papers": papers,
        "simulation_result": sim_result,
        "evaluation": evaluation,
        "report": report
    }
