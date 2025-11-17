def read_csv(file_path):
    import csv
    data = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            keyword = row['Keyword'].strip().lower()
            commands = row['Commands'].strip().split('\n')
            data[keyword] = commands
    return data

def format_response(commands):
    return "\n".join(commands) if commands else "No commands found for the given query."