from unittest import TestCase
from api.jokeoftheday_api import *

class TestJokes(TestCase):
    def test_knock(self):
        joke = generate_joke_request_knock()
        self.assertTrue(len(joke)>1)