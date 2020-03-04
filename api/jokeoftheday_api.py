import requests
from pprint import pprint

url ="https://api.jokes.one/jod "
headers = {'content-type': 'application/json',
	   'X-JokesOne-Api-Secret': format(api_token)}

def generate_joke_request_knock():
    url = f'{url}?category=knock-knock'
    response = requests.get(url, headers=headers)
    jokes=response.json()['contents']['jokes'][0]
    return jokes

def generate_joke_request_knock():
    url = f'{url}?category=knock-knock'
    response = requests.get(url, headers=headers)
    jokes=response.json()['contents']['jokes'][0]
    return jokes

def generate_joke_request_blonde():
    url = f'{url}?category=blonde'
    response = requests.get(url, headers=headers)
    jokes=response.json()['contents']['jokes'][0]
    return jokes

def generate_joke_request_standard():
    response = requests.get(url, headers=headers)
    jokes=response.json()['contents']['jokes'][0]
    return jokes