import ui.ui as ui
import configs.view_tools as view_tools

last_joke = ''

def menu_generator():
    function_actions = {
        1:search_joke,
        2:generate_random_joke,
        3:save_joke,
        4:delete_joke}
    
    return function_actions

def search_joke():
    term = ui.search()
    joke = view_tools.setup_search(term)
    global last_joke
    last_joke = joke
    ui.display_joke(joke)

def generate_random_joke():
    joke = view_tools.generate_random_joke()
    global last_joke
    last_joke = joke
    ui.display_joke(joke)

def save_joke():
    joke = view_tools.check_joke(last_joke)

    if not joke:
        return
    else:
        ui.display_joke(joke)
        ui.save_joke_confirmation(joke)
        return

def delete_joke():
    pass


def view_controller():
    menu = menu_generator()
    ui.introduction()
    
    while True:
        ui.display_options()
        selection = ui.input_selection()
        action = view_tools.make_selection(menu, selection)
        action()