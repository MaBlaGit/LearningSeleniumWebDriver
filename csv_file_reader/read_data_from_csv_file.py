import csv


def extract_data_from_csv_file(data):
    course_list = []
    with open(data, 'r') as csv_file:
        read_csv = csv.reader(csv_file)
        next(read_csv)
        for data_element in read_csv:
            course_list.append([data_element[0]])
    return course_list
