import re
import random
from groq import Groq
import os
from dotenv import load_dotenv

def quebrar_em_linhas(texto, palavras_por_linha):
    texto = re.sub(r"\s+", " ", texto.strip())
    palavras = texto.split(" ")

    linhas = []
    for i in range(0, len(palavras), palavras_por_linha):
        linhas.append(" ".join(palavras[i:i + palavras_por_linha]))

    return "\n".join(linhas)


def PDC_Bot(pergunta: str, prompt: str, modo: str) -> str:
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

    # Interceptador do KoC
    if modo == "KoC":
        frases = [
            "To comendo sofa",
            "Come sofa",
            "Coem ofsa",
            "Safo moec",
            "Cmoe faos",
            "Bora?",
            "Tem que ir pra Russia",
            "Como minera Bitcoin no celular?"
        ]

        chance = 5  # %

        if random.uniform(0, 100) < chance:
            return f"\n{random.choice(frases)}"

    client = Groq(api_key=api_key)

    try:
        resposta = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": pergunta}
            ]
        )

        if resposta.choices and resposta.choices[0].message:
            conteudo = resposta.choices[0].message.content.strip()
            conteudo = quebrar_em_linhas(conteudo, palavras_por_linha=17)
        else:
            conteudo = "O vazio respondeu, nada..."

        return f"\n{conteudo}"

    except Exception as e:
        return f"\nAlguma porpetagem aconteceu, manda print da tela para kmlresearchlabs@gmail.com: {e}"