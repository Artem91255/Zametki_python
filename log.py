import csv
import os

import controller




def write_in_csv(name,text):
    with open(name, 'w', encoding='utf=8') as nts:
        writer = csv.writer(nts, lineterminator="\r", delimiter=' ')

        writer.writerow(text)
        writer.writerow("")

def delete_csv(name):
    name_to_delete = name+".csv"
    os.remove(name_to_delete)

def write_in_list(name,date):
    name_for_list = name+date

    with open('list_of_notes.csv', 'a', encoding='utf=8') as nts:
        writer = csv.writer(nts, lineterminator="\r", delimiter=' ')
        writer.writerow(name)
        writer.writerow(name_for_list)








