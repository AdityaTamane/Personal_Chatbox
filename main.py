import openai
from api import apikey

openai.api_key = apikey

def chat_with_Tom(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",  
            prompt=prompt,
            max_tokens=150  
        )
        
        reply = response['choices'][0]['text']
        print("Tom:", reply)
    
    except Exception as e:
        print(f"An error occurred: {e}")

print("Welcome, I am Tom your personal chatbox. \n! Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    chat_with_Tom(user_input)
