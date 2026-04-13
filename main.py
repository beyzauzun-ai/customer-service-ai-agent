from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request modeli
class ChatRequest(BaseModel):
    message: str

# Test endpoint (çalışıyor mu diye)
@app.get("/")
def root():
    return {"message": "Customer Service Agent is running 🚀"}

# Chat endpoint (Streamlit burayı çağırıyor)
@app.post("/chat")
def chat(req: ChatRequest):
    user_message = req.message

    # Basit cevap (şimdilik test için)
    reply = f"You said: {user_message}"

    return {"reply": reply}

