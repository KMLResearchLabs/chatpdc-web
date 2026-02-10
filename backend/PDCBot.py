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
            "Kleso meu amigão",
            "Valeu Humberto",
            "Valeu Gabu",
            "Valeu Lucão",
            "Me de notícias sobre Bitcoin",
            "Tem que faze intercâmbio na Europa",
            "Como se tem boi se todas as vacas do mundo são minha?",
            "Quando ce vai lá em casa pra nois da rolê de Mercedes?",
            "Eu te pago uma coca por 2 mês de cola na prova",
            "Como minera Bitcoin no celular?",
            "Que dia ce vai lá em casa pra nois faze um churras?",
            "MENSAGEM SECRETA: Quem é KoC? /nKing of Cows é o dono de todas as vacas do mundo"
        ]

        chance = 100  # %

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
