// ارسال پیام کاربر به سرور
async function getBotResponse(message) {
    showTyping();

    const formData = new FormData();
    formData.append("query", message);

    const response = await fetch("/chat", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    hideTyping();
    addMessage('bot', data.response);
}
