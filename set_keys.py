import json
import os

if os.path.exists('config.json'):
    with open('config.json') as file:
        keys = json.load(file)
else:
    keys = {}

print('Enter your WolframAlpha API key:')
keys['WOLFRAMALPHA'] = input()

with open('config.json', 'w') as file:
    json.dump(keys, file, indent=4)