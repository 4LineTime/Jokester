from database.database import *

def add_joke(joke):
    new_joke = Jokes(joke_text = f'{joke}')
    return new_joke.save()
def delete_joke(id):
    return Jokes.delete().where(Jokes.joke_id == id).execute()
def search_joke_id(id):
    return Jokes.select().where(Jokes.joke_id == id)