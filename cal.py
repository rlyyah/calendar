import ui
import storage


def add_new_schedule(schedule):
    new_meeting = ui.get_input(['meeting title','duration in hours', 'start time'],'Schedule a new meeting')
    schedule.append(new_meeting)
    return schedule


def cancel_the_meeting(schedule):
    FIRST_ELEMENT = 0
    try:
        cancel_which = int(ui.get_input(['Index'],'Which meeting would you like to cancel?')[FIRST_ELEMENT])
    except ValueError as err:
        print(err)
    schedule.pop(cancel_which)
    return schedule


def menu_stucture():
    
    menu = ['(s) schedule a new meeting',
            '(c) cancel an existing meeting']
    label = 'Menu:'
    exit_msg = '(q) quit'

    return [label, menu, exit_msg]


def menu():
    is_running = True
    while is_running:
        # print menu
        # wait for user input
        # follow inputs instruction


