import csv

# NORMAL METHOD
# with open('names.csv', "r") as f:
#     csv_reader = csv.reader(f)

#     # next(csv_reader)  # start from 1 index

#     with open('practise_new.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')

#         for line in csv_reader:
#             csv_writer.writerow(line)
#     # for line in csv_reader:
#     #     print(line[2])


# DICT READER METHOD
# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     for line in csv_reader:
#         print(line['email'])

# DICT METHOD FOR WRITING CSV FILE
# using Dict method we can select particular column and parse to another csv file.
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('dict_new_names.csv', 'w') as new_file:
        # fieldnames must be same as written in original csv file
        fieldnames = ['me', 'last_name']  # Do not mension the column which we dont want
        csv_writer = csv.DictWriter(
            new_file, fieldnames=fieldnames, delimiter='\t')

        # It also copy the header from original csv file.
        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']  # delete email column
            csv_writer.writerow(line)
