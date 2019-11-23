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