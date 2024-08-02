import openai
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a chave API do ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"Error: {e}"

def main():
    while True:
        prompt = input("Usuario: ")
        if prompt.lower() in ["exit", "quit"]:
            print("Exiting chat...")
            break
        response = chat_with_gpt(prompt)
        print(f"GPT-3.5: {response}")

if __name__ == "__main__":
    main()
