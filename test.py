import json


f = open('users.json')
text = json.load(f)
print(type(text['users']))