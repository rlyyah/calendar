def get_input(data_format, label):
    inputs = []
    print_result(label)
    for question in data_format:
        inputs.append(input(question))
    return inputs


def print_result(message):
    print(message)


def print_menu(menu_list):
    
    LABEL = 0
    MENU = 1
    EXIT = 2

    print(menu_list[LABEL])
    for option in menu_list[MENU]:
        print(option)
    print(menu_list[EXIT])

def print_schedule(schedule):

    DESC = 0
    DURATION = 1
    START_TIME = 2
    
    print('Your schedule for today')
    for meeting in schedule:
        print(f'{meeting[START_TIME]} - {int(meeting[START_TIME]) + int(DURATION)} {DESC}')
