def get_input(data_format, label):
    inputs = []
    for question in data_format:
        inputs.append(input(question))
    return inputs

