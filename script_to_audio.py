import os
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI
from prompts import voice_prompt_bible

load_dotenv()

client = OpenAI()

def text_to_audio(text):

    speech_file_path = Path(__file__).parent / "audio.mp3"

    with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="ash",
    instructions=voice_prompt_bible,
    input=text,
    ) as response:
        response.stream_to_file(speech_file_path)


