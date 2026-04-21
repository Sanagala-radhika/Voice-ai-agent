frontend/mic.js  

let ws;
let mediaRecorder;

async function start() {
  ws = new WebSocket("ws://localhost:8000/voice");

  ws.onopen = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.ondataavailable = async (event) => {
      if (event.data.size > 0 && ws.readyState === 1) {
        const buffer = await event.data.arrayBuffer();
        ws.send(buffer);
      }
    };

    mediaRecorder.start(250); // send audio every 250ms
  };

  ws.onmessage = async (event) => {

    // TEXT RESPONSE
    if (typeof event.data === "string") {
      document.getElementById("aiText").innerText = event.data;
    }

    // AUDIO RESPONSE
    else {
      const blob = new Blob([event.data], { type: "audio/mpeg" });
      const audio = new Audio(URL.createObjectURL(blob));
      audio.play();
    }
  };
}

function stop() {
  if (mediaRecorder) mediaRecorder.stop();
  if (ws) ws.close();
}
