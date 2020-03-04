import requests
url = 'https://geek-jokes.sameerkumar.website/api'

def generate_sameer_joke():
    response = requests.get(url)
    joke = response.json()['contents']
    print(joke)
    #joke =''
    return joke



generate_sameer_joke()
