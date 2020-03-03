import configs.view_tools as view_tools

def introduction():
    print('**********************************************')
    print('***   ___       _             _            ***')
    print('***  |_  |     | |           | |           ***')
    print('***    | | ___ | | _____  ___| |_ ___ _ __ ***')
    print('***    | |/ _ \| |/ / _ \/ __| __/ _ \ \'__|***')
    print('***/\__/ / (_) |   <  __/\__ \ ||  __/ |   ***')
    print('***\____/ \___/|_|\_\___||___/\__\___|_|   ***')
    print('**********************************************\n\n')

def display_options():
    print(
        '\nMenu Options\n\n',
        '1. Search Joke\n',
        '2. Generate Random Joke\n',
        '3. Save Last Joke\n',
        '4. Delete Joke\n',
        '0. Exit program\n'
    )

def input_selection():
    while True:
        try:
            selection = int(input('\nEnter in a selection:'))
            if selection > 5:
                print('\nThat in not a valid options.')
                
            elif selection >= 0:
                return selection
            else:
                print('\nYou can not enter a value lower than 0')

        except ValueError:
            print('\nYou can only enter whole numbers')

def display_saved_jokes(jokes):
    for j in jokes:
        print(j)

def search():
    return input("What do you want to search?")

def search_joke_id():
    while True:
        try:
            id = int(input("What is the id for the joke that you want to search"))
            if id > 0:
                return id
            else:
                print('You cannot enter a value lower than 1')
        
        except ValueError:
            print('\nYou can only enter a number\n')


def display_joke(joke):
    return print('\n' + joke + '\n')

def save_joke_confirmation(joke):

    while True:
        # try: 
        yes_or_no = input('\nWould you like to save this joke? Enter y for yes and n for no.\nEnter Here:')
        yes_or_no = yes_or_no.lower().strip()

        if yes_or_no == 'y':
            view_tools.add_to_database(joke)
            return
        elif yes_or_no.lower()== 'n':
            print('\nNo changes have been made')
            return
        else:
            print('\nThat is not a valid options')
        # except:
        #     print('\nThere was a error. Please try again')