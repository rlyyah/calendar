def get_input(data_format, label):
    inputs = []
    print_result(label)
    for question in data_format:
        inputs.append(input(question))
    return inputs


def print_result(message):
    print(message)