from unittest import TestCase
from peewee import *
from database import *

db = 'database/test_joke.db'


class Test_Jokes(TestCase):

    def test_create_jokes(self):
        joke = joke(joke_id=1, joke_text='LOL')
        self.assertIn('1')
        self.assertIn('LOL')
        

