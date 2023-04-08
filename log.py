import csv


import controller


# def create_the_name(name_of_the_note):
#     note_name=name_of_the_note+".csv"  #Название заметки будет также названием файла
#     return note_name

def write_in_csv(name,text):
    with open(name, 'a', encoding='utf=8') as nts:
        writer = csv.writer(nts, lineterminator="\r")
        writer.writerow(text)
        writer.writerow("")




