from database.database import *

def add_joke(joke):
    return Jokes(joke_text = joke)

def delete_joke(id):
    return Jokes.delete().where(Jokes.joke_id = id).execute()

def search_joke_id(id):
    return Jokes.select().where(Jokes.joke_id = id)