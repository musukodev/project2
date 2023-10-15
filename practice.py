import requests

api_key = "4b0ac7cb-5d16-485c-a21f-2ab6e27a95a2"
word = "potato"
url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"

res = requests.get(url)

definition = res.json()

print(definition)