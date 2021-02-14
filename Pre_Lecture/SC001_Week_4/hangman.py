import json
import random
import requests

response = requests.get("http://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
data = response.json()
random_word = random.choice(data)
print(random_   word.upper())