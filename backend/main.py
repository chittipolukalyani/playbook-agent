from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLAYBOOKS_PATH = os.path.join(BASE_DIR, "playbooks", "playbooks.json")

with open(PLAYBOOKS_PATH, encoding="utf-8") as f:
    playbooks = json.load(f)

class Query(BaseModel):
    problem: str

def match_playbook(problem: str):
    problem_lower = problem.lower()
    for playbook in playbooks:
        for keyword in playbook["keywords"]:
            if keyword in problem_lower:
                return playbook
    return playbooks[0]

@app.post("/analyze")
async def analyze(query: Query):
    matched = match_playbook(query.problem)

    prompt = f"""You are an expert AI assistant using the '{matched["name"]}' playbook.

Problem: {query.problem}

Follow these steps exactly:
Step 1: Understand the problem
Step 2: Identify the core issue
Step 3: Apply the {matched["name"]} approach
Step 4: Give the solution with explanation
Step 5: Give a confidence score out of 100

Be clear, specific and helpful."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "playbook": matched["name"],
        "playbook_id": matched["id"],
        "solution": response.choices[0].message.content,
        "problem": query.problem
    }

@app.get("/playbooks")
async def get_playbooks():
    return playbooks

@app.get("/health")
async def health():
    return {"status": "running"}

@app.get("/evals")
async def run_evals():
    import json as json_module
    
    evals_path = os.path.join(BASE_DIR, "evals", "test_cases.json")
    with open(evals_path, encoding="utf-8") as f:
        test_cases = json_module.load(f)
    
    total = len(test_cases)
    passed = 0
    failed = []
    playbook_stats = {}

    for test in test_cases:
        matched = match_playbook(test["problem"])
        result_id = matched["id"]
        expected = test["expected_playbook"]
        
        if expected not in playbook_stats:
            playbook_stats[expected] = {"total": 0, "passed": 0}
        playbook_stats[expected]["total"] += 1
        
        if result_id == expected:
            passed += 1
            playbook_stats[expected]["passed"] += 1
        else:
            failed.append({
                "problem": test["problem"],
                "expected": expected,
                "got": result_id
            })

    accuracy = round((passed / total) * 100, 1)
    
    return {
        "total": total,
        "passed": passed,
        "failed_count": total - passed,
        "accuracy": accuracy,
        "failed_cases": failed[:10],
        "playbook_stats": playbook_stats
    }
feedback_store = []

class Feedback(BaseModel):
    playbook: str
    rating: str
    problem: str

@app.post("/feedback")
async def store_feedback(feedback: Feedback):
    feedback_store.append({
        "playbook": feedback.playbook,
        "rating": feedback.rating,
        "problem": feedback.problem
    })
    return {"status": "saved"}

@app.get("/insights")
async def get_insights():
    if not feedback_store:
        return {"total": 0, "satisfaction": 0, "by_playbook": {}}
    
    total = len(feedback_store)
    thumbs_up = sum(1 for f in feedback_store if f["rating"] == "up")
    satisfaction = round((thumbs_up / total) * 100, 1)
    
    by_playbook = {}
    for f in feedback_store:
        pb = f["playbook"]
        if pb not in by_playbook:
            by_playbook[pb] = {"up": 0, "down": 0}
        by_playbook[pb][f["rating"]] += 1
    
    return {
        "total": total,
        "thumbs_up": thumbs_up,
        "thumbs_down": total - thumbs_up,
        "satisfaction": satisfaction,
        "by_playbook": by_playbook
    }