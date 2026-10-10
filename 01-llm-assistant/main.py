import os 
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

# check if the api key can be loaded properly
# print("API key loaded:", bool(os.getenv("OPENAI_API_KEY")))

client = OpenAI()

# add memory to remember the conversation and define the role
messages = [
    {
        "role": "developer",
        "content": ("You are a patient Python tutor. "
    "For programming exercises, your first reply must give "
    "one short hint and ask the learner to attempt the code. "
    "Do not provide complete solution code in that first reply. "
    "Provide the full solution only if the learner explicitly asks for it."
)
    }
]

while True:

    user_prompt = input("User: ")

    if user_prompt.strip().lower() == "quit":
        break
    
    # append messages
    messages.append({"role":"user", "content": user_prompt})

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=messages,
        max_output_tokens=300
    )

    # append the assistants answer
    messages.append({"role": "assistant", "content": response.output_text})
    print("Assistant:", response.output_text)


