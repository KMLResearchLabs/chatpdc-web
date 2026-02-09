let chatIniciado = false;

function enviarSugestao(texto) {
  document.getElementById("pergunta").value = texto;
  enviar();
}

chat.scrollTo({
  top: chat.scrollHeight,
  behavior: "smooth"
});

const sessionId = crypto.randomUUID();

async function enviar() {
  if (!chatIniciado) {
    document.getElementById("welcome").style.display = "none";
    document.getElementById("chat").style.display = "flex";
    chatIniciado = true;
  }

  
  const pergunta = document.getElementById("pergunta").value;
  const modo = document.getElementById("modo").value;
  const chat = document.getElementById("chat");
  const botao = document.getElementById("btnEnviar");

  if (!pergunta.trim()) return;

  botao.disabled = true;

  chat.innerHTML += `<div class="msg-user">${pergunta}</div>`;

  const typing = document.createElement("div");
  typing.className = "typing";
  typing.innerHTML = "<span></span><span></span><span></span>";
  chat.appendChild(typing);
  chat.scrollTop = chat.scrollHeight;

  document.getElementById("pergunta").value = "";

 try {
  const res = await fetch("https://chatpdc-web.onrender.com/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      pergunta,
      modo,
      session_id: sessionId
    })
  });

  if (!res.ok) {
    const text = await res.text();
    console.error("Erro backend:", text);
    throw new Error("Backend error");
  }

  const data = await res.json();

  typing.remove();
  chat.innerHTML += `<div class="msg-bot">${marked.parse(data.resposta)}</div>`;
} catch (err) {
  console.error(err);
  typing.remove();
  chat.innerHTML += `<div class="msg-bot">Erro ao responder </div>`;
}


  botao.disabled = false;
  chat.scrollTop = chat.scrollHeight;
}
