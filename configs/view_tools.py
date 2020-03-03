import api.icanhazdadjoke_api as dad_joke_api
import random

def make_selection(menu, selection):
    if selection == 1:
        return menu[1]
    elif selection == 2:
        return menu[2]
    elif selection == 3:
        return menu[3]
    elif selection == 4:
        return menu[4]
    elif selection == 0:
        print("Thank you for using the program. Goodbye!")
        raise SystemExit
    else:
        print("\nThat is not a valid option")

def setup_search(term):
    joke_list = []

    data = dad_joke_api.search_api_request(term)

    for result in data['results']:
        joke_list.append(result['joke'])

    return random.choice(joke_list)

def joke_store(joke):
    pass

    
def check_joke(joke):
    pass

    
def generate_random_joke():
    data = dad_joke_api.generate_joke_request()

    return data['joke']

def add_to_database(joke):
    pass
def delete_from_database(id):
    pass

    
        


    