import os
from script_generator import generate_script
from script_to_audio import text_to_audio
from generate_footage_query import generate_queries_for_chunks
from compose_video import connect_everything
import ffmpeg
from img_generation import generate_images_from_keywords
from transcribe_audio import transcribe_audio_chunks



if __name__ == "__main__":

    os.environ['FFREPORT'] = ''  

    script_topic = input('Please Enter the topic of the video you wish to create: ')

    print("\n=== Starting script generation ===")
    script = str(generate_script(script_topic))
    print("=== Generated Script ===")
    print(script)

    print("\n=== Generating Audio ===")
    text_to_audio(script)
    print("✓ Audio generation completed successfully!")

    print("\n=== transcribing Audio ===")
    transcribed_chunks, chunk_durations = transcribe_audio_chunks('audio.mp3')
    print(f"Here are the transcribed chunks: {transcribed_chunks}")
    print("=== Audio transcribtion is done ===")

    print("\n=== started prompt generation this will take a while ===")
    img_prompts = generate_queries_for_chunks(script, transcribed_chunks)
    print("=== prompt generation is completed ===")
    print(f"Number of prompts are: {len(img_prompts)}\n")
    print(f"img prompts: {img_prompts}\n")
    
    print("\n=== Downloading Video Clips ===")
    generate_images_from_keywords(img_prompts)
    print("✓ Video clips downloaded successfully!")
    
    print("\n=== Combining Audio and Video ===")
    connect_everything('images', chunk_durations,'audio.mp3')
    print("✓ Video assembly completed!")
    


    
