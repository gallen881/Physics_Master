from llama_cpp import Llama
import json
import requests
import sys

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
        return "Error: " + r.text
    
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
        'content':'You are a professional physics master, you can answer the physics questions you know.' + ' If you are not sure about the answer, especially problems that require calculation or internet, you must use WolframAlpha. To use WolframAlpha, please only output "<|wolframalpha|>" in the message, and then only output the question you want to use WolframAlpha to calculate. For example, "<|wolframalpha|>X^2+2X+1=0". After system get the answer from WolframAlpha, you can continue to answer the question. If you have new question, please output "<|wolframalpha|>your question here" again.' if WOLFRAMALPHA_KEY else ''
    }
]

if not WOLFRAMALPHA_KEY:
    print('Warning: WolframAlpha API key is not set. You will not be able to use WolframAlpha to answer questions. To set the key, please edit the config.json file.')
    print('WolframAlpha disabled.')
else:
    print('WolframAlpha enabled.')

user_inputing = True
while True:
    if user_inputing:
        user_input = input('\033[94mYou: \033[0m')
        user_message = {'role': 'user', 'content': user_input}
        messages.append(user_message)
    print('Physics Master is thinking...', end='\r')
    r = llm.create_chat_completion(
        messages=messages
    )
    sys.stdout.write("\033[K")
    # print(r)
    # print(messages)
    llm_message = r['choices'][0]['message']
    messages.append(llm_message)
    if '<|wolframalpha|>' in llm_message['content']:
        question = llm_message['content'].replace('<|wolframalpha|>', '').strip()
        answer = wolframalpha_query(question)
        messages.append({'role': 'wolframalpha', 'content': answer})
        user_inputing = False
        continue
    print('\033[96mPhysics Master: \033[0m', llm_message['content'])
    user_inputing = True