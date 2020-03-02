import requests

from pprint import pprint

headers = {
    'Accept': 'application/json',
    'User-Agent': 'jokester:https://github.com/4LineTime/Jokester',
    'Email': 'yc8121yl@minnstate.edu'  # This is another valid field
}


url = "https://icanhazdadjoke.com/"


return requests.get(url, headers=headers).json()
