import os 
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

# check if the api key can be loaded properly
# print("API key loaded:", bool(os.getenv("OPENAI_API_KEY")))

client = OpenAI()

# add memory to remember the conversation
messages = []

while True:

    user_prompt = input("What do you want to know?: ")

    if user_prompt.strip() == "quit":
        break
    
    # append messages
    messages.append({"role":"user", "content": user_prompt})
    
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=user_prompt,
        max_output_tokens=100
    )

    print("Assistant:",response.output_text)