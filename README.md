# 🤖 AI Playbook Agent

An AI agent that takes any coding problem, automatically selects the right playbook, reasons step by step, and delivers a precise solution — with built-in evals, red teaming, and RLHF feedback loop.

## 🎯 What it does

- Describe any coding problem in plain English
- Agent automatically classifies it into 1 of 7 playbooks
- AI reasons through 5 structured steps
- Returns solution with confidence score and code diff
- Voice input supported

## 📊 Results

- **93.8% accuracy** on 210 automated test cases
- **10/10** adversarial red team inputs handled gracefully
- **7 playbooks** — Debugging, Explanation, Optimization, Security, Testing, Refactor, Review

## 🏗️ Architecture

User Input → Playbook Router → AI Agent → Structured Solution
↓
Eval Harness (210 tests)
↓
RLHF Feedback Loop

## 🛠️ Tech Stack

- **Frontend** — HTML, CSS, JavaScript
- **Backend** — Python, FastAPI
- **AI Model** — Groq LLaMA 3
- **Evals** — Custom eval harness with 210 test cases
- **Built with** — Cursor AI IDE

## 🚀 How to run

1. Clone the repo
2. Install dependencies
```bash
pip install fastapi uvicorn groq python-dotenv
```
3. Add your Groq API key to `backend/.env`
GROQ_API_KEY=your-key-here

4. Start backend
```bash
cd backend
uvicorn main:app --reload
```
5. Open `frontend/index.html` in browser

## 🔬 Features

| Feature | Description |
|---|---|
| ⚡ AI Agent | Solves coding problems step by step |
| 📊 Eval Dashboard | 93.8% accuracy on 210 test cases |
| 🔴 Red Team | 10/10 adversarial inputs handled |
| 🔬 RLHF Insights | User feedback analytics |
| 🎤 Voice Input | Speak your problem |
| 🔀 Code Diff | Before/after code comparison |
| 💯 Confidence Score | AI self-assessed confidence meter |

## 💡 Inspired by

- Cursor's agentic loop (plan → tool call → observe → repeat)
- Devin's session-based autonomous coding
- OpenAI's RLHF training methodology