from requests import get


__all__ = ['geek', 'icanhazdad', 'chucknorris', 'icndb']
#API URL
url ="https://api.jokes.one/jod"
api_token = 'Not Applicable' #Don't need it for Joke of the day
headers = {'content-type': 'application/json',
	   'X-JokesOne-Api-Secret': format(api_token)}

#Generate Knock Knock Joke String
def generate_joke_request_knock():
    new_url = f'{url}?category=knock-knock'
    response = get(new_url, headers=headers)
    jokes=response.json()['contents']['jokes'][0]
    joke=jokes['joke']['text']
    return joke


#Generate Animal Joke String
def generate_joke_request_animal():
    new_url = f'{url}?category=animal'
    response = get(new_url, headers=headers)
    jokes=response.json()['contents']['jokes'][0]
    joke=jokes['joke']['text']
    return joke

#Generate Blonde Joke String
def generate_joke_request_blonde():
    new_url = f'{url}?category=blonde'
    response = get(new_url, headers=headers)
    jokes=response.json()['contents']['jokes'][0]
    joke=jokes['joke']['text']
    return joke

#Generate Joke of the Day String
def generate_joke_request_standard():
    response = get(url, headers=headers)
    jokes=response.json()['contents']['jokes'][0]
    joke=jokes['joke']['text']
    return joke


def geek():
    resp = get('https://geek-jokes.sameerkumar.website/api')
    if resp.status_code == 200:
        return resp.text[1:-2]


def icanhazdad():
    headers = {'Accept': 'text/plain'}
    rresp = get('https://icanhazdadjoke.com/', headers=headers)
    if rresp.status_code == 200:
        return rresp.text


def chucknorris():
    resp = get('https://api.chucknorris.io/jokes/random')
    if resp.status_code == 200:
        return resp.json()['value']


def icndb():
    resp = get('http://api.icndb.com/jokes/random/')
    if resp.status_code == 200:
        return resp.json()['value']['joke']


def get_joke(category):


    # for resp in __all__:
    #     if resp==category:
    #         return resp

        # if category == 'geek':
        #     resp= geek()
        if category=='icndb':
            resp = icndb()
        if category == 'icanhazdad':
            resp = icanhazdad()
        elif category=='chucknorris':
            resp = chucknorris()
        elif category=='animal':
            resp=generate_joke_request_animal()

        # else:
        #     resp=icndb()

        return resp


