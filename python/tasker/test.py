import json

with open('taski.json', 'r') as f:
    tasks = json.load(f)
print(tasks)