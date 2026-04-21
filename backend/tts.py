services/tts.py (Text to speech) 

import requests

API_KEY = "YOUR_ELEVENLABS_API_KEY"

async def generate_audio(text):
    url = "https://api.elevenlabs.io/v1/text-to-speech"

    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.7
        }
    }

    response = requests.post(url, json=data, headers=headers)

    return response.content
