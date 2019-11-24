import ui
import storage


def add_new_schedule(schedule):

    new_meeting = ui.get_input(['meeting title', 'duration in hours', 'start time'], 'Schedule a new meeting')
    schedule.append(new_meeting)
    return schedule


def cancel_the_meeting(schedule):

    FIRST_ELEMENT = 0
    try:
        cancel_which = int(ui.get_input(['Index'], 'Which meeting would you like to cancel?')[FIRST_ELEMENT])
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


def menu_handler(instruction):

    FIRST_ELEMENT = 0
    instruction = instruction[FIRST_ELEMENT].lower()
    decision = True
    if instruction == 's':
        # go to scheduling a meetin
        pass
    elif instruction == 'c':
        # go to meeting cancelling
        pass
    elif instruction == 'q':
        decision = False
    else:
        ui.print_result('Command Unknown. Please enter a proper one!')
    return decision


def menu():
    is_running = True
    while is_running:
        # print menu
        ui.print_menu(menu_stucture())
        # wait for user input
        is_running = menu_handler(ui.get_input(['what would you like to do?\n'], ''))
        # follow inputs instruction


menu()
