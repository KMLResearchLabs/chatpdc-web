async function enviar() {
  const pergunta = document.getElementById("pergunta").value;
async function enviar() {
  const pergunta = document.getElementById("pergunta").value;
  const modo = document.getElementById("modo").value;
  const chat = document.getElementById("chat");

  chat.innerHTML += `<div class="msg-user">${pergunta}</div>`;

  const res = await fetch("https://chatpdc-web.onrender.com", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ pergunta, modo })
  });

  const data = await res.json();

  chat.innerHTML += `<div class="msg-bot">${data.resposta}</div>`;

  document.getElementById("pergunta").value = "";
}
