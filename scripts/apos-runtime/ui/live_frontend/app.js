const ws = new WebSocket("ws://localhost:8000/ws");

ws.onmessage = (msg) => {
    const data = JSON.parse(msg.data);

    if (data.type === "event") {
        console.log("EVENT:", data.data);
    }

    if (data.type === "state") {
        console.log("STATE:", data.data);
    }
};