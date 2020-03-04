from database.database import *

def add_joke(joke):
    try:
        new_joke = Jokes(joke_text = f'{joke}')
        return new_joke.save()
    except:
        print('There was a error')
def delete_joke(id):
    return Jokes.delete().where(Jokes.joke_id == id).execute()
def search_joke_id(id):
    return Jokes.select().where(Jokes.joke_id == id)

def select_all_records():
    joke_list = []
    for j in Jokes.select():
        joke_list.append(j.joke_id)
        joke_list.append(j.joke_text)

    return joke_list