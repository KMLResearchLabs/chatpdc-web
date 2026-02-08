async function enviar() {
  const pergunta = document.getElementById("pergunta").value;
  const modo = document.getElementById("modo").value;
  const chat = document.getElementById("chat");

  if (!pergunta.trim()) return;

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
      body: JSON.stringify({ pergunta, modo })
    });

    const data = await res.json();

    typing.remove();

    chat.innerHTML += `<div class="msg-bot">${data.resposta}</div>`;
  } catch (err) {
    typing.remove();
    chat.innerHTML += `<div class="msg-bot">Erro ao responder 😢</div>`;
  }

  chat.scrollTop = chat.scrollHeight;
}
