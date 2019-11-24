import ui
import storage


def add_new_schedule(schedule):

    validation = True
    
    while validation:
        new_meeting = ui.get_input(['meeting title', 'duration in hours', 'start time'], 'Schedule a new meeting')
        validation = validate_new_meeting(new_meeting)

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


def validate_new_meeting(meeting):

    DESC = 0
    DURATION = 1
    START_TIME = 2
    validated = False

    try:
        int(meeting[DURATION])
        int(meeting[START_TIME])
        validated = True
    except ValueError:
        print('Wrong format of ')
        validated = False

    return validated

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
    file_name = 'schedule.csv'
    schedule = storage.read_calendar_file(file_name)
    save = storage.write_data_to_file

    if instruction == 's':
        # go to scheduling a meetin
        save(file_name, add_new_schedule(schedule))
        pass
    elif instruction == 'c':
        # go to meeting cancelling
        save(file_name, cancel_the_meeting(schedule))
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
