import requests
url = 'https://geek-jokes.sameerkumar.website/api'

def generate_sameer_joke():
    response = requests.get(url)
    joke = response.json() #the whole json file is a joke. No dictionary needed
    return joke