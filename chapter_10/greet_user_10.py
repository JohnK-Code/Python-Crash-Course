#### Saving and Reading User-Generated Data - Chapter 10 - Page 204 
import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")