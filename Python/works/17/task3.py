import json
import os

def create(name):
    open(name, 'w').close()

def write(name, text):
    with open(name, 'w') as f:
        f.write(text)

def delete(name):
    if os.path.exists(name):
        os.remove(name)


with open('commands.json', 'r') as f:
    data = json.load(f)

for c in data['commands']:
    cmd = c['cmd']

    if cmd == 'create':
        create(c['name'])

    elif cmd == 'write':
        write(c['name'], c['text'])

    elif cmd == 'delete':
        delete(c['name'])