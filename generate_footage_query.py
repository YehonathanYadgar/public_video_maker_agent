from openai import OpenAI
import os
from dotenv import load_dotenv
from prompts import keyword_generator_system_prompt_bible

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def generate_queries_for_chunks(full_script, script_chunks):
    """
    Generates footage queries for a list of script chunks using the OpenAI API.

    Args:
        script_chunks: A list of strings, where each string is a chunk of the script.

    Returns:
        A list of strings, where each string is a generated footage query corresponding
        to the input script chunk.
    """
    generated_queries = []
    previous_query = "No previous image prompt. " 
    for chunk in script_chunks:
        try:
            user_content = (
                f"Heres the full video script: \n {full_script} \n "
                f"Heres the current script chunk: {chunk} \n "
                f"Heres the previous image prompt generated(so you wont make consequtive images to simaler and make it boring): {previous_query}"
            )
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": keyword_generator_system_prompt_bible},
                    {
                        "role": "user",
                        "content": user_content
                    }
                ]
            )
            query = completion.choices[0].message.content
            generated_queries.append(query)
            previous_query = query 
        except Exception as e:
            print(f"Error processing chunk: {chunk[:50]}... - {e}")

            generated_queries.append(f"Error generating query: {e}")
            previous_query = "Error in previous generation." 

    return generated_queries

if __name__ == "__main__":
    example_full_script = "Jesus was born in judea. He was born to Mary. Mary was poor" 
    example_chunks = [
        "Jesus was born in judea",
        "He was born to Mary",
        "Mary was poor"
    ]
    queries = generate_queries_for_chunks(example_full_script, example_chunks) 
    print(queries)