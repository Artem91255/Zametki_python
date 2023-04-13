import csv
import os

import controller




# def write_in_csv(name,text):
#     with open(name, 'w', encoding='utf=8') as nts:
#         writer = csv.writer(nts, lineterminator="\r", delimiter=';')
#
#         writer.writerow(text)
#         writer.writerow("")

def delete_csv(name):
    name_to_delete = name+".csv"
    os.remove(name_to_delete)

def write_in_list(list):

    with open('list_of_notes.csv', 'a', encoding='utf=8') as nts:
        writer = csv.writer(nts, lineterminator="\r", delimiter=';')
        writer.writerow(list)

def read_my_csv():
    with open('list_of_notes.csv', 'r', encoding='utf=8') as f:
        print("")
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:

            print(row['name'] + ": "+ row['body'])
        print("")











