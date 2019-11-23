def read_calendar_file(file_name):
    data = []
    with open(file_name, 'r') as f:
        for line in f:
            splitted = line.strip().split(';')
            data.append(splitted)
        return data


def write_data_to_file(file_name, data):
    with open(file_name, 'w') as f:
        for line in data:
            compressed = ';'.join(line)
            compressed += '\n'
            f.write(compressed)
