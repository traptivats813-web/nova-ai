const input = document.querySelector(".input-area input");
const button = document.querySelector(".input-area button");
const chatBox = document.querySelector(".chat-box");

button.addEventListener("click", sendMessage);

input.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

function sendMessage() {

    const message = input.value.trim();

    if (message === "") return;

    chatBox.innerHTML += `
        <div class="user-message">
            ${message}
        </div>
    `;

    input.value = "";

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    })
    .then(response => response.json())
    .then(data => {

        chatBox.innerHTML += `
            <div class="ai-message">
                ${data.response}
            </div>
        `;
        input.value = "";
        input.focus();

        chatBox.scrollTop = chatBox.scrollHeight;

    });
}
const newChatBtn = document.getElementById("new-chat");

newChatBtn.addEventListener("click", function () {

    fetch("/new_chat", {
        method: "POST"
    })
    .then(response => response.json())
    .then(data => {

        chatBox.innerHTML = `
            <div class="ai-message">
                👋 Hello! I'm <strong>Nova AI</strong>. How can I help you today?
            </div>
        `;

    });

});