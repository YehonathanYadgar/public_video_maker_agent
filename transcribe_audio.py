from openai import OpenAI
import os
from typing import Tuple, List

client = OpenAI()

def transcribe_audio_chunks(audio_file_path: str) -> Tuple[List[str], List[float]]:
    """
    Transcribes the audio file at the given path into natural chunks using OpenAI Whisper.

    Args:
        audio_file_path: The path to the audio file (e.g., mp3, wav).

    Returns:
        A tuple containing two lists:
        1. A list of strings, where each string is a transcribed chunk/segment.
        2. A list of floats, where each float is the duration of the corresponding chunk in seconds.
        Returns ([], []) if the file doesn't exist or transcription fails.
    """

    try:
        with open(audio_file_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="verbose_json",
                timestamp_granularities=["segment"] # Request segment-level timestamps
            )

        chunks = []
        durations = []
        for segment in transcription.segments:
            chunks.append(segment.text)
            duration = segment.end - segment.start
            durations.append(duration)

        return chunks, durations
    except Exception as e:
        print(f"An error occurred during transcription: {e}")
        return [], []

# Example usage:
if __name__ == "__main__":
    test_audio_path = "audio.mp3"
    transcribed_chunks, chunk_durations = transcribe_audio_chunks(test_audio_path)
    print(transcribed_chunks)
    