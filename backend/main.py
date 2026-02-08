from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from PDCBot import PDC_Bot
from prompts import chatpdc_prompts
from memory import get_session, cleanup_sessions

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://kmlresearchlabs.github.io"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    pergunta: str
    modo: str
    session_id: str


@app.post("/chat")
def chat(req: ChatRequest):
    cleanup_sessions()

    session = get_session(req.session_id)

    # salva pergunta na memória
    session["messages"].append({
        "role": "user",
        "content": req.pergunta
    })

    session["messages"] = session["messages"][-12:]

    prompt = chatpdc_prompts.get(req.modo, chatpdc_prompts["Normal"])

    # chama o bot COM CONTEXTO
    resposta = PDC_Bot(
        mensagem=req.pergunta,
        prompt=prompt,
        modo=req.modo,
        memory=session["messages"]
    )

    # salva resposta
    session["messages"].append({
        "role": "assistant",
        "content": resposta
    })

    return {"resposta": resposta}
