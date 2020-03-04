import requests
from pprint import pprint

#API URL
url ="https://api.jokes.one/jod"
api_token = 'Not Applicable' #Don't need it for Joke of the day
headers = {'content-type': 'application/json',
	   'X-JokesOne-Api-Secret': format(api_token)}

#Generate Knock Knock Joke String
def generate_joke_request_knock():
    new_url = f'{url}?category=knock-knock'
    response = requests.get(new_url, headers=headers)
    jokes=response.json()['contents']['jokes'][0]
    joke=jokes['joke']['text']
    return joke


#Generate Animal Joke String
def generate_joke_request_animal():
    new_url = f'{url}?category=animal'
    response = requests.get(new_url, headers=headers)
    jokes=response.json()['contents']['jokes'][0]
    joke=jokes['joke']['text']
    return joke

#Generate Blonde Joke String
def generate_joke_request_blonde():
    new_url = f'{url}?category=blonde'
    response = requests.get(new_url, headers=headers)
    jokes=response.json()['contents']['jokes'][0]
    joke=jokes['joke']['text']
    return joke

#Generate Joke of the Day String
def generate_joke_request_standard():
    response = requests.get(url, headers=headers)
    jokes=response.json()['contents']['jokes'][0]
    joke=jokes['joke']['text']
    return joke

print(generate_joke_request_knock())