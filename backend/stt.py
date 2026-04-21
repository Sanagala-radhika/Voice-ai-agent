services/stt.py (speech to text)

import whisper
import uuid

model = whisper.load_model("base")

async def transcribe_audio(audio_bytes):
    file_name = f"temp_{uuid.uuid4()}.wav"

    with open(file_name, "wb") as f:
        f.write(audio_bytes)

    result = model.transcribe(file_name)
    return result["text"]
