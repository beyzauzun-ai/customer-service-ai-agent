from fastapi import FastAPI
from pydantic import BaseModel
import os

from google import genai

app = FastAPI()

api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None


class RequestModel(BaseModel):
    message: str


@app.get("/")
def root():
    return {
        "message": "Customer Service Agent is running 🚀",
        "ai_enabled": client is not None,
    }


@app.post("/chat")
def chat(request: RequestModel):
    user_input = request.message.lower()

    # Rule-based responses first
    if "refund" in user_input:
        return {"reply": "Sure! Please provide your order ID for the refund process."}

    elif "order" in user_input:
        return {"reply": "You can track your order using your order ID."}

    elif "hello" in user_input or "hi" in user_input:
        return {"reply": "Hello! How can I assist you today?"}

    elif "damaged" in user_input or "broken" in user_input:
        return {
            "reply": "I’m sorry your product arrived damaged. Please share your order ID so I can help with a refund or replacement."
        }

    # AI fallback
    if client is not None:
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"""
You are a helpful customer service assistant.
Answer clearly and politely.

If the user writes in Turkish, respond in Turkish.
If the user writes in English, respond in English.

Customer message:
{request.message}
""",
            )
            return {"reply": response.text}
        except Exception as e:
            return {"reply": f"AI Error: {str(e)}"}

    return {"reply": "I’m here to help! Could you please clarify your request?"}

