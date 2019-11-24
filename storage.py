def read_calendar_file(file_name):
    data = []
    with open(file_name, 'r') as f:
        for line in f:
            splitted = line.strip().split(';')
            data.append(splitted)
        return data
