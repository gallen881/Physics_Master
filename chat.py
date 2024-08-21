from llama_cpp import Llama
import urllib.parse
import json
import requests
import sys
import os
import time

def wolframalpha_query(question):
    print('Physics Master is using WolframAlpha...', end='\r')
    query = urllib.parse.quote_plus('calculate ' + question)
    query_url = f"http://api.wolframalpha.com/v2/query?" \
                f"appid={WOLFRAMALPHA_KEY}" \
                f"&input={query}" \
                f"&includepodid=Result" \
                f"&output=json"
    r = requests.get(query_url)
    sys.stdout.write("\033[K")
    if r.status_code == 200:
        try:
            return r.json()["queryresult"]["pods"][0]["subpods"][0]["plaintext"]
        except:
            print(question)
            print(r.json()["queryresult"])
    else:
        return ''

def prompt_from_messages(messages):
    prompt = ''
    for message in messages:
        prompt += f"<|start_header_id|>{message['role']}<|end_header_id|>\n\n"
        prompt += f"{message['content']}<|eot_id|>"
    prompt = prompt[:-10]
    return prompt
        
keys = {}
if os.path.exists('config.json'):
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
        'content':'You are a professional physics master, you can answer the physics questions you know.' + ' If you are not sure about the answer, especially problems that require calculation or internet, you must use WolframAlpha. To use WolframAlpha, please ONLY output "<|wolframalpha|>" in the message, and then ONLY output the calculaion formula you want to use WolframAlpha to calculate. For example, "<|wolframalpha|>x^2+2x+1=0" or "<|wolframalpha|>1024*512/3", a <|wolframalpha|> tag can ONLY use in a calculation formula, other information is not necessary. <|wolframalpha|x^2+2x+1=0|> is a wrong example. After system get the answer from WolframAlpha, you can continue to answer the question. If you have new question, please output "<|wolframalpha|>your question here" again.' if WOLFRAMALPHA_KEY else ''
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
use_wolframalpha = False
while True:
    if use_wolframalpha:
        use_wolframalpha = False
        # print('Asking WolframAlpha: ' + query)
        query = ''
        for i in wolf_answer.split():
            print(i, end=' ', flush=True)
        response = llm.create_completion(
            prompt=prompt_from_messages(messages)
        )
        print(response['choices'][0]['text'])
        messages[-1]['content'] += response['choices'][0]['text']

    chat_history[-1]['messages'] = messages
    with open('chat_history.json', 'w', encoding='utf8') as file:
        json.dump(chat_history, file, indent=4)
    user_input = input('\033[94mYou: \033[0m')
    user_message = {'role': 'user', 'content': user_input}
    messages.append(user_message)
    print('Physics Master is thinking...', end='\r')
    response = llm.create_chat_completion(
        messages=messages,
        stream=True
    )
    # print(response)
    sys.stdout.write("\033[K")
    wolf_token = ''
    for chunk in response:
        delta = chunk['choices'][0]['delta']
        if 'role' in delta:
            messages.append({'role': delta['role'], 'content': ''})
            print("\033[95mPhysics Master: \033[0m", end='', flush=True)
        elif 'content' in delta:
            token = delta['content']
            if '<|wolframalpha|>' in wolf_token:
                use_wolframalpha = True
                query = wolf_token.replace('<|wolframalpha|>', '')
                wolf_token = ''

            if use_wolframalpha:
                if '\n' in token:
                    wolf_answer = wolframalpha_query(query)
                    messages[-1]['content'] += wolf_answer
                    break
                else:
                    query += token
                continue


            wolf_token += token
            if wolf_token == '<|wolframalpha|>'[:len(wolf_token)] or '<|wolframalpha|>' in wolf_token:
                continue
            else:
                token = wolf_token
                wolf_token = ''

            messages[-1]['content'] += token
            print(token, end="", flush=True)
    print()
    if use_wolframalpha and query:
        wolf_answer = wolframalpha_query(query)
        messages[-1]['content'] += wolf_answer
        query = ''