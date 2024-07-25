import io
import sys


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

    pipe_delimiter_file = sys.argv[1]
    comma_delimiter_file = sys.argv[2]
    space_delimiter_file = sys.argv[3]

    pipe_records = read_file_records(pipe_delimiter_file, 'pipe')
    comma_records = read_file_records(comma_delimiter_file, 'comma')
    space_records = read_file_records(space_delimiter_file, "space")

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
