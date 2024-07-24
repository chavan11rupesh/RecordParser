import io


def read_records(file, type):
    records = []
    with open(file, 'r') as file:
        for r in file:
            if type == 'pipe-delimiter':
                record = r.strip().split('|')
            elif type == 'comma-delimiter':
                record = r.strip().split(',')
            elif type == 'space-delimiter':
                record = r.strip().split(' ')
            records.append(record)
    return records



