# 🤖 AI Playbook Agent

> *An autonomous AI agent that classifies coding problems, routes them through specialized playbooks, and delivers structured solutions — with built-in evals, red teaming, and RLHF feedback loop.*

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-playbook--agent--ai.netlify.app-6ee7f7?style=for-the-badge)](https://playbook-agent-ai.netlify.app)
[![GitHub](https://img.shields.io/badge/GitHub-chittipolukalyani-a78bfa?style=for-the-badge&logo=github)](https://github.com/chittipolukalyani/playbook-agent)
[![Accuracy](https://img.shields.io/badge/Eval_Accuracy-93.8%25-34d399?style=for-the-badge)]()
[![Red Team](https://img.shields.io/badge/Red_Team-10%2F10-f472b6?style=for-the-badge)]()

---

## 🧠 The Problem

Most AI tools are generic — you paste a problem, get a generic answer. There's no reasoning about *what type* of problem it is or *how* to approach it strategically.

Real engineers don't approach every problem the same way. A debugging session looks different from a security audit. A refactoring task needs different thinking than writing unit tests.

**This project solves that.**

---

## 💡 The Solution

A multi-layer AI agent inspired by how **Cursor** and **Devin** work under the hood:
User Input
↓
Intent Classifier (keyword-based router)
↓
Playbook Selector (7 specialized strategies)
↓
Structured AI Prompt (5-step reasoning chain)
↓
Solution + Confidence Score + Code Diff
↓
RLHF Feedback Loop (👍/👎 per playbook)

---

## 📊 Results

| Metric | Result |
|---|---|
| Eval Accuracy | **93.8%** on 210 test cases |
| Red Team Score | **10/10** adversarial inputs handled |
| Playbooks | **7** specialized strategies |
| Improvement | **74.3% → 93.8%** through keyword tuning |
| Deployment | **Live** on Netlify + Render |

---

## 🗂️ Playbook System

The agent classifies every problem into one of 7 playbooks before solving it:

| Playbook | Triggered By | Approach |
|---|---|---|
| 🐛 Code Debugging | error, crash, bug, fix | Root cause → isolate → patch |
| 📖 Code Explanation | explain, what does, understand | Break down → annotate → summarize |
| ⚡ Performance Optimization | slow, faster, optimize | Profile → bottleneck → refactor |
| 🔒 Security Check | vulnerable, injection, secure | Threat model → identify → harden |
| 🧪 Write Unit Tests | test, coverage, assert | Edge cases → assertions → suite |
| 🔧 Refactor Code | messy, clean, restructure | SOLID → DRY → readable |
| 👁️ Code Review | review, feedback, best practice | Standards → gaps → improvements |

---

## 🔬 Eval Framework

Built a custom eval harness — not just vibes testing:

- **210 hand-curated test cases** with expected playbook labels
- **Automated accuracy scoring** per playbook category
- **Error analysis** — documented exactly where and why it fails
- **Iterative improvement** — tuned keywords across 4 rounds
Round 1: 74.3% → Round 2: 82.4% → Round 3: 92.9% → Round 4: 93.8%

This is the same methodology used by ML teams to evaluate classification models.

---

## 🔴 Red Team Testing

Adversarial inputs designed to break the agent:

| Input Type | Example | Result |
|---|---|---|
| Gibberish | `asdfjkl qwerty random` | ✅ Handled |
| Empty input | *(nothing)* | ✅ Handled |
| All keywords | `debug optimize test review refactor` | ✅ Handled |
| Vague | `I need help` | ✅ Handled |
| Emotional | `HELP ME MY CODE IS BROKEN` | ✅ Handled |
| Philosophical | `What is the meaning of life in Python` | ✅ Handled |
| SQL ambiguity | `SELECT * FROM users` | ✅ Handled |
| No problem stated | `My code is perfect` | ✅ Handled |

**Score: 10/10** — Agent never crashed. Always returned structured response.

---

## 🔁 RLHF Feedback Loop

After every solution, users rate 👍 or 👎. The system tracks:

- Overall user satisfaction score
- Per-playbook satisfaction breakdown
- Which playbooks need improvement

This mirrors the Reinforcement Learning from Human Feedback technique used by OpenAI to improve ChatGPT — implemented here at a micro scale.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, Vanilla JS |
| Backend | Python 3.12, FastAPI |
| AI Model | Groq API — LLaMA 3.3 70B |
| Deployment | Netlify (frontend) + Render (backend) |
| Version Control | Git + GitHub |
| IDE | Cursor (AI-native editor) |

---

## 🚀 Run Locally

```bash
# Clone
git clone https://github.com/chittipolukalyani/playbook-agent.git
cd playbook-agent

# Install
pip install fastapi uvicorn groq python-dotenv

# Configure
echo "GROQ_API_KEY=your-key-here" > backend/.env

# Start backend
cd backend
uvicorn main:app --reload

# Open frontend
open frontend/index.html
```

---

## 📁 Project Structure
playbook-agent/
├── backend/
│   ├── main.py              # FastAPI server + agent logic
│   └── .env                 # API keys (gitignored)
├── frontend/
│   └── index.html           # Full UI — 5 tabs, voice input, code diff
├── playbooks/
│   └── playbooks.json       # 7 playbooks with keyword routing
├── evals/
│   ├── test_cases.json      # 210 labeled test cases
│   └── run_evals.py         # Automated eval runner
└── README.md

---

## 🎯 Key Features

- ⚡ **AI Agent** — step-by-step reasoning, not just Q&A
- 🎤 **Voice Input** — speak your problem
- 💯 **Confidence Meter** — AI self-assessed score with animated bar
- 🔀 **Code Diff Viewer** — before/after side-by-side comparison
- 📊 **Eval Dashboard** — live accuracy visualization
- 🔴 **Red Team Mode** — adversarial robustness testing
- 🔬 **RLHF Insights** — user feedback analytics
- 📋 **Session History** — last 5 analyzed problems

---

## 💡 Inspired By

- **Cursor's agentic loop** — plan → tool call → observe → repeat
- **Devin's session model** — autonomous task execution
- **OpenAI's RLHF** — human feedback drives model improvement
- **Anthropic's red teaming** — adversarial safety evaluation

---

## 🔮 Future Work

- [ ] Add semantic similarity for better playbook matching
- [ ] Input guardrails — detect and reject non-coding inputs
- [ ] Persistent feedback storage with database
- [ ] Multi-turn conversations — follow-up questions
- [ ] Fine-tuned classifier to replace keyword routing

---

*Built and deployed as a personal project. Validated with automated evals and adversarial testing.*