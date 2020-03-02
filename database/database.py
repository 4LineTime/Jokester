from peewee import *

db = SqliteDatabase('jokester_application_db.sqlite')

class JokeBaseModel(Model):
    class Meta:
        database = db

class Jokes(JokeBaseModel):
    joke_id = AutoField()
    joke_text = TextField()


def connect_db():
    db.connect()
    db.create_tables([Jokes]) 