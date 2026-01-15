/* Chat Interface Logic */

const chatContainer = document.getElementById('chatContainer');
const inputText = document.getElementById('inputText');
const submitBtn = document.querySelector('.btn-send');

// Auto-resize textarea
inputText.addEventListener('input', function () {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';
    if (this.value === '') {
        this.style.height = '24px';
    }
});

// Handle Enter key
inputText.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        submitTask();
    }
});

async function submitTask() {
    const input = inputText.value.trim();
    if (!input) return;

    // Clear input
    inputText.value = '';
    inputText.style.height = '24px';

    // Add User Message
    appendMessage(input, 'user');

    // Disable input while processing
    inputText.disabled = true;
    submitBtn.disabled = true;

    // Add Loading Bubble
    const loadingId = appendLoadingMessage();

    try {
        const res = await fetch("http://localhost:8000/api/run-agent", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ input }),
        });

        const data = await res.json();

        // Remove loading bubble
        removeMessage(loadingId);

        // Render AI Response
        const result = data.output || data.memory || {};
        appendAgentResponse(result);

    } catch (error) {
        console.error("Error:", error);
        removeMessage(loadingId);
        appendMessage("Sorry, I encountered an error connecting to the server.", 'ai');
    } finally {
        inputText.disabled = false;
        submitBtn.disabled = false;
        inputText.focus();
    }
}

function appendMessage(text, sender) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `message message-${sender}`;

    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    bubble.textContent = text;

    msgDiv.appendChild(bubble);
    chatContainer.appendChild(msgDiv);
    scrollToBottom();
}

function appendLoadingMessage() {
    const id = 'loading-' + Date.now();
    const msgDiv = document.createElement('div');
    msgDiv.className = 'message message-ai';
    msgDiv.id = id;

    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    bubble.innerHTML = '<span class="typing-dots">Thinking...</span>';

    msgDiv.appendChild(bubble);
    chatContainer.appendChild(msgDiv);
    scrollToBottom();
    return id;
}

function removeMessage(id) {
    const el = document.getElementById(id);
    if (el) el.remove();
}

function appendAgentResponse(response) {
    const msgDiv = document.createElement('div');
    msgDiv.className = 'message message-ai';

    const bubble = document.createElement('div');
    bubble.className = 'bubble';

    if (Object.keys(response).length === 0) {
        bubble.textContent = "I processed your request but have nothing specific to report.";
        msgDiv.appendChild(bubble);
        chatContainer.appendChild(msgDiv);
        scrollToBottom();
        return;
    }

    // Check for simple text response first (common in direct chat)
    if (typeof response === 'string') {
        bubble.textContent = response;
        msgDiv.appendChild(bubble);
        chatContainer.appendChild(msgDiv);
        scrollToBottom();
        return;
    }

    // Format structured agent response
    const contentWrapper = document.createElement('div');

    for (const [agent, result] of Object.entries(response)) {
        const agentName = agent.replace('_output', '').replace('_', ' ');
        const title = document.createElement('strong');
        title.style.display = 'block';
        title.style.marginBottom = '4px';
        title.style.color = '#a5b4fc';
        title.style.textTransform = 'capitalize';
        title.textContent = agentName;
        contentWrapper.appendChild(title);

        if (typeof result === "object") {
            const pre = document.createElement('pre');
            pre.textContent = JSON.stringify(result, null, 2);
            contentWrapper.appendChild(pre);
        } else {
            const p = document.createElement('p');
            p.style.marginBottom = '12px';
            p.textContent = result;
            contentWrapper.appendChild(p);
        }
    }

    bubble.appendChild(contentWrapper);
    msgDiv.appendChild(bubble);
    chatContainer.appendChild(msgDiv);
    scrollToBottom();
}

function scrollToBottom() {
    // scroll the wrapper, not window
    const wrapper = document.querySelector('.chat-wrapper');
    wrapper.scrollTop = wrapper.scrollHeight;
}
