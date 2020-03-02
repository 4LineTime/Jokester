def introduction():
    print('**********************************************')
    print('***   ___       _             _            ***')
    print('***  |_  |     | |           | |           ***')
    print('***    | | ___ | | _____  ___| |_ ___ _ __ ***')
    print('***    | |/ _ \| |/ / _ \/ __| __/ _ \ \'__|***')
    print('***/\__/ / (_) |   <  __/\__ \ ||  __/ |   ***')
    print('***\____/ \___/|_|\_\___||___/\__\___|_|   ***')
    print('**********************************************\n\n')



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


