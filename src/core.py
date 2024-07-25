import io


def read_file_records(file, type):
    records = []
    with open(file, 'r') as file:
        for r in file:
            if type == 'pipe':
                record = r.strip().split('|')
            elif type == 'comma':
                record = r.strip().split(',')
            elif type == 'space':
                record = r.strip().split(' ')
            records.append(record)
    return records


def sorted_by_gender_and_last_name(result):
    records = sorted(result, key=lambda r: (r[2], r[0]))
    return records


def sorted_by_dob(result):
    records = sorted(result, key=lambda r: r[4])
    return records


def sorted_by_last_name_desc(result):
    records = sorted(result, key=lambda r: r[0], reverse=True)
    return records


if __name__ == "__main__":

    #result = []

    pipe_records = read_file_records("../resources/pipe_delimiter.txt", 'pipe')
    comma_records = read_file_records("../resources/comma_delimiter.txt", 'comma')
    space_records = read_file_records("../resources/space_delimiter.txt", "space")

    result = pipe_records + comma_records + space_records
    output1 = sorted_by_gender_and_last_name(result)
    output2 = sorted_by_dob(result)
    output3 = sorted_by_last_name_desc(result)

    print("\nsorted_by_gender_and_last_name :")
    for record in output1:
        print(record)

    print("\nsorted_by_dob :")
    for record in output2:
        print(record)

    print("\nsorted_by_last_name_desc :")
    for record in output3:
        print(record)
