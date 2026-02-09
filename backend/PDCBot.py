import random
from groq import Groq
import os
from dotenv import load_dotenv


def PDC_Bot(pergunta: str, prompt: str, modo: str, memory=None) -> str:
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

        chance = 95  # %

        if random.uniform(0, 100) < chance:
            return f"\n{random.choice(frases)}"

    client = Groq(api_key=api_key)

    try:
        messages = [
            {"role": "system", "content": prompt}
        ]

        if memory:
            messages.extend(memory)

        messages.append({
            "role": "user",
            "content": pergunta
        })

        resposta = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )

        if resposta.choices and resposta.choices[0].message:
            conteudo = resposta.choices[0].message.content.strip()
        else:
            conteudo = "O vazio respondeu, nada..."

        return f"\n{conteudo}"

    except Exception as e:
        return (
            "\nAlguma porpetagem aconteceu, manda print da tela "
            f"para kmlresearchlabs@gmail.com: {e}"
        )
