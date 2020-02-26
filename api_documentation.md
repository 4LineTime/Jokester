Jokester Api documentation.


PRAW - Python Reddit Api wrapper. (Not fully tested)

In order to successfully use this we need to use OAuth and PRAW (Python reddit api wrapper).
Currently it requires that we fill out a form for a OAuth project. I have already currently made the project
so contact me on slack to be added to the project. Once you are added to the project there will be a client
number and a client password that we will be working with. Ill provide links so that this Api is easier to access.
The project will primarily be ran through flask as a read only idea so that no content will be effected.
Praw Quickstart link: https://praw.readthedocs.io/en/latest/getting_started/quick_start.html
Reddit Documentation (https://www.reddit.com/dev/api/)
--------------------------------------------------------------------------------------------------------------


Tumblr API (Not fully tested)

This api also uses OAuth to access authoration to the api. They have a client library available called pytumblr.
The search queries for this seems very simplistic using the library but needs further testing.
Useful links:
- Pytumblr (https://github.com/tumblr/pytumblr)
- Tumblr api documentation (https://www.tumblr.com/docs/en/api/v2)
--------------------------------------------------------------------------------------------------------------


Yomomma Api (Tested)

This api sends back a yo momma joke when you send a request. There is no account needed for this api.
Links:
https://yomomma.info/
--------------------------------------------------------------------------------------------------------------


ICanHazDadJoke Api (Not fully tested)

This api allows search querys. The only think that the creators of this api request for authentication
is setting a user-agent component. This seems promising but has not been tested.
Links:
https://icanhazdadjoke.com/api#authentication
