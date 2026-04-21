backend/main.py core engine

from fastapi import FastAPI, WebSocket
from services.stt import transcribe_audio
from services.llm import process_intent
from services.tts import generate_audio

app = FastAPI()

@app.websocket("/voice")
async def voice_agent(ws: WebSocket):
    await ws.accept()

    while True:
        try:
            audio_bytes = await ws.receive_bytes()

            # 1. Speech → Text
            text = await transcribe_audio(audio_bytes)

            # 2. Text → Intent + Response
            response_text = await process_intent(text)

            # 3. Text → Audio
            audio_response = await generate_audio(response_text)

            # Send both text + audio
            await ws.send_text(response_text)
            await ws.send_bytes(audio_response)

        except Exception as e:
            await ws.send_text(f"Error: {str(e)}")
            break
