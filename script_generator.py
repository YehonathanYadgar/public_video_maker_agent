from openai import OpenAI
import os
from dotenv import load_dotenv
import prompts 

load_dotenv()  
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_script(user_content):

    completion = client.chat.completions.create(
        model="gpt-4.1-2025-04-14",
        messages=[
            {"role": "system", "content": f"{prompts.script_generator_prompt_short_form_bible}"},
            {
                "role": "user",
                "content": f'The topic of the video I am Working on is: {user_content} '
            }
        ]
    )

    return completion.choices[0].message.content

# Example usage
if __name__ == "__main__":
    result = generate_script("The history of jesus christ")
    print(result)