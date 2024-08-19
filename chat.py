from llama_cpp import Llama
import json
import requests
import sys
import os
import time

def wolframalpha_query(question):
    print('Physics Master is using WolframAlpha...', end='\r')
    api_url = "https://api.wolframalpha.com/v1/spoken"
    params = {
        "appid": WOLFRAMALPHA_KEY,
        "i": question
    }
    r = requests.get(api_url, params=params)
    sys.stdout.write("\033[K") 
    if r.status_code == 200:
        return r.text
    else:
        return 'Error: ' + r.text + '. Please ONLY output "<|wolfamalpha|>question have to calculate here". For example, "<|wolframalpha|>x^2+2x+1=0". Here is the wrong example: "Thank you for the reminder. Here is the correct input:\n\n<|wolframalpha|>x^2+2x+1=0"'
    
with open('config.json') as file:
    keys = json.load(file)

WOLFRAMALPHA_KEY = keys.get('WOLFRAMALPHA', '')

llm = Llama.from_pretrained(
    repo_id='gallen881/Llama-3-8B-Physics_Master-GGUF',
    filename='unsloth.Q4_K_M.gguf',
    n_ctx=2048,
    verbose=False
)

messages = [
    {
        'role': 'system',
        'content':'You are a professional physics master, you can answer the physics questions you know.' + ' If you are not sure about the answer, especially problems that require calculation or internet, you must use WolframAlpha. To use WolframAlpha, please ONLY output "<|wolframalpha|>" in the message, and then ONLY output the question you want to use WolframAlpha to calculate. For example, "<|wolframalpha|>x^2+2x+1=0", other information is not necessary. After system get the answer from WolframAlpha, you can continue to answer the question. If you have new question, please output "<|wolframalpha|>your question here" again.' if WOLFRAMALPHA_KEY else ''
    }
]

if not WOLFRAMALPHA_KEY:
    print('Warning: WolframAlpha API key is not set. You will not be able to use WolframAlpha to answer questions. To set the key, please edit the config.json file.')
    print('WolframAlpha disabled.')
else:
    print('WolframAlpha enabled.')

if os.path.exists('chat_history.json'):
    with open('chat_history.json', encoding='utf8') as file:
        chat_history = json.load(file)
else:
    chat_history = []

chat_time = time.time()
chat_history.append({"time": chat_time, "messages": None})
user_inputing = True
while True:
    chat_history[-1]['messages'] = messages
    with open('chat_history.json', 'w', encoding='utf8') as file:
        json.dump(chat_history, file, indent=4)
    if user_inputing:
        user_input = input('\033[94mYou: \033[0m')
        user_message = {'role': 'user', 'content': user_input}
        messages.append(user_message)
    print('Physics Master is thinking...', end='\r')
    r = llm.create_chat_completion(
        messages=messages
    )
    sys.stdout.write("\033[K")
    llm_message = r['choices'][0]['message']
    messages.append(llm_message)
    if '<|wolframalpha|>' in llm_message['content']:
        question = llm_message['content'].replace('<|wolframalpha|>', '').strip()
        answer = wolframalpha_query(question)
        if not answer.startswith('Error'): print('\033[95mWolframAlpha: \033[0m', answer)
        messages.append({'role': 'wolframalpha', 'content': answer})
        user_inputing = False
        continue
    print('\033[96mPhysics Master: \033[0m', llm_message['content'])
    user_inputing = True