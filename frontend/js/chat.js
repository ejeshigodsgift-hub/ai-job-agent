async function sendMessage() {

    const input = document.getElementById("messageInput")

    const message = input.value

    const response = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message,
            user_id: 1
        })
    })

    const data = await response.json()

    const messages = document.getElementById("messages")

    messages.innerHTML += `<p><b>You:</b> ${message}</p>`

    messages.innerHTML += `<p><b>AI:</b> ${data.reply}</p>`

    input.value = ""
}