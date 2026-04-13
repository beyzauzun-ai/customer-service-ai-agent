# 🤖 AI Customer Service Agent with Evaluation Pipeline

An end-to-end AI customer service project that combines:
- an intelligent support agent
- an automated evaluation pipeline
- a live web interface for public demo

## 🚀 Live Demo

- Streamlit App: https://customer-service-ai-agent.streamlit.app
- Live API: https://customer-service-ai-agent-264345805986.europe-west1.run.app

## 💡 Project Overview

This project simulates real-world customer service scenarios such as:
- refunds
- order tracking
- damaged product complaints
- product-related questions

The project started as an evaluation-focused AI agent workflow and was later extended with a FastAPI backend and a Streamlit UI for live deployment.
## 📸 Demo

Built an AI-powered customer service agent capable of handling real-world scenarios such as order tracking, refunds, and product inquiries with automated evaluation.

<img src="AgentUI.png" width="800"/>


## 🧪 Evaluation Pipeline
The evaluation pipeline was designed to automatically test the agent’s behavior across customer service scenarios.

It measures:
- tool usage accuracy
- response quality
- scenario success rate

## 📊 Evaluation Pipeline
```bash
customer_service_agent/
├── main.py
├── eval/
├── tests/
├── .env
├── README.md

```

### Evaluation Results

- ✅ All test scenarios passed
- ✅ tool_trajectory_avg_score: 1.0
- ✅ response_match_score: ~0.55–0.66

This helped validate whether the agent not only responds, but responds in a reliable and testable way.

## 🖥️ Live Application Layer

To make the project interactive and publicly accessible, I added:
- a FastAPI backend for handling chat requests
- a Streamlit frontend for user interaction
- public deployment for real-time demo access

## 🧠 What I Learned

Through this project, I gained hands-on experience in:
- building an AI agent workflow
- working with evaluation pipelines
- creating REST APIs with FastAPI
- connecting frontend and backend systems
- integrating LLM-based responses
- deploying a public AI application
- improving UX with quick action buttons

## 🔧 Tech Stack

- Python
- Google ADK
- Pytest
- FastAPI
- Streamlit
- Google Gemini API
- Git & GitHub

## 🏗️ Architecture

User → Streamlit UI → FastAPI Backend → AI Logic / Evaluation-informed Agent Design → Response

## ✨ Features

- ✅ AI-powered conversational agent
- ✅ Automated evaluation system
- ✅ Scenario-based testing
- ✅ Scalable architecture using Google ADK
- ✅ Test-driven evaluation with pytest
- ✅ FastAPI backend for real-time interaction
- ✅ Streamlit UI for user-friendly interface
- ✅ Public deployment (live demo)

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/beyzauzun-ai/customer-service-ai-agent.git
cd customer-service-ai-agent
```

### ⛓️‍💥 Install dependencies:
pip install -r requirements.txt

### Run FastAPI backend

 ```bash
python3 -m uvicorn main:app --host 0.0.0.0 --port 8080
```
### Run Streamlit UI

 ```bash
streamlit run app_ui.py
```

 ### Open in browser
 
 ```bash
http://localhost:8501
```

### 🎯 Purpose

This project was developed to build and evaluate an AI-powered customer service agent that can handle real-world support scenarios.

The goal was to:
- design an intelligent conversational agent
- validate its performance using an evaluation pipeline
- deploy it as a real, user-facing application


## 🧠 Learning Outcomes

- AI agent design
- Evaluation pipelines
- Real-world AI applications
- Backend–frontend integration
- Deploying AI systems to production

  
### 👩‍💻 Author

Beyza Uzun

AI & Data Enthusiast
