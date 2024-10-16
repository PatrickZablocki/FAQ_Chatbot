const sendBtn = document.getElementById("sendBtn");
const userInput = document.getElementById("userInput");
const chatbox = document.getElementById("chatbox");

sendBtn.addEventListener("click", () => {
    const message = userInput.value;
    chatbox.innerHTML += `<div>User: ${message}</div>`;
    userInput.value = '';

    //  API-Abfrage an das Backend
    fetch('http://127.0.0.1:5000/api/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
    })
    .then(response => response.json())
    .then(data => {
        chatbox.innerHTML += `<div>Bot: ${data.response}</div>`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
})