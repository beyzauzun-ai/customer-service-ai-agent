from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {"message": "Customer Service Agent is running 🚀"}


@app.post("/chat")
def chat(req: ChatRequest):
    user_input = req.message.lower().strip()

    if "refund" in user_input or "iade" in user_input:
        return {
            "reply": "Sure! Please provide your order ID for the refund process."
        }

    elif "order" in user_input or "sipariş" in user_input:
        return {
            "reply": "You can track your order using your order ID."
        }

    elif "damaged" in user_input or "hasarlı" in user_input:
        return {
            "reply": "I'm sorry to hear that. Please share your order ID and a short description of the damage."
        }

    elif "hello" in user_input or "hi" in user_input or "merhaba" in user_input:
        return {
            "reply": "Hello! How can I assist you today?"
        }

    elif "product" in user_input or "ürün" in user_input:
        return {
            "reply": "Of course. Please tell me which product you need help with."
        }

    else:
        return {
            "reply": "I'm here to help! Could you please clarify your request?"
        }
