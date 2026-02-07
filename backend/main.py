from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from PDCBot import PDC_Bot
from prompts import chatpdc_prompts

app = FastAPI()

# Libera acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois pode restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    pergunta: str
    modo: str

@app.post("/chat")
def chat(req: ChatRequest):
    prompt = chatpdc_prompts.get(req.modo, chatpdc_prompts["Normal"])
    resposta = PDC_Bot(req.pergunta, prompt)
    return {"resposta": resposta}
