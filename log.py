import csv
import operation


def note_editor():
    see_all_names_and_bodys()
    id_of_note = input("Введите уникальный номер заметки,которую хотите отредактировать:")
    new_body_of_note=input("Введите новый текст заметки:")

    with open("list_of_notes.csv", encoding='utf=8') as file_name:
        file_read = csv.reader(file_name, lineterminator="\r", delimiter=';')
        array = list(file_read)

        for i in range(len(array)):
            for j in range(len(array[i])):
                if(array[i][j].__contains__(id_of_note)):
                    array[i][j+2]=new_body_of_note
                    notedate = operation.get_date_now()
                    notedate_str = notedate.strftime("%d.%m.%Y %H:%M:%S")
                    array[i][j + 3] = notedate_str
                    with open('list_of_notes.csv', 'w', newline='', encoding='utf=8') as f:
                        writer = csv.writer(f, lineterminator="\r", delimiter=';')
                        writer.writerows(array)

def take_note_by_needed_date():
    date_info = input("Введите дату в формате дд.мм.гггг: ")

    with open("list_of_notes.csv", encoding='utf=8') as file_name:
        file_read = csv.reader(file_name, lineterminator="\r", delimiter=';')
        array = list(file_read)

        for i in range(len(array)):
            for j in range(len(array[i])):
                if(array[i][j].__contains__(date_info)):

                    print('')
                    print(array[i][j-2]+ ': \n'+ array[i][j-1])

def write_in_csv(list):
    with open("list_of_notes.csv", 'w', encoding='utf=8') as nts:
        writer = csv.writer(nts, lineterminator="\r", delimiter=';')

        writer.writerow(list)
        writer.writerow("")

def show_id_of_notes():
    with open("list_of_notes.csv", encoding='utf=8') as file_name:
        reader = csv.DictReader(file_name, delimiter=";")

        for row in reader:
            print(row['id'] + "\n"+ row['name'])
        print("")

def show_name_of_notes():
    with open("list_of_notes.csv", encoding='utf=8') as file_name:
        reader = csv.DictReader(file_name, delimiter=";")

        for row in reader:
            print(row['name'] + "\n")
        print("")


def delete_in_csv(uuid):
    with open("list_of_notes.csv", encoding='utf=8') as file_name:
        file_read = csv.reader(file_name)
        array = list(file_read)

        for i in range(len(array)):
            for j in range(len(array[i])):
                if(array[i][j].__contains__(uuid)):
                    del array[i][j]

    with open('list_of_notes.csv', 'w', newline='', encoding='utf=8') as f:
        writer = csv.writer(f)
        writer.writerows(array)





def write_in_list(list):
    with open('list_of_notes.csv', 'a', encoding='utf=8') as nts:
        writer = csv.writer(nts, lineterminator="\r", delimiter=';')
        writer.writerow(list)

def see_all_names_and_bodys():
    with open('list_of_notes.csv', 'r', encoding='utf=8') as f:
        print("")
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            print(row['id'] + "\n "+row['name'] + ": \n"+ row['body'] + '\n' +row['date'])
        print("")
def see_all_notes():
    with open('list_of_notes.csv', 'r', encoding='utf=8') as f:
        print("")
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            print(row['name'] + ": \n"+ row['body'] + '\n' +row['date'])
            print("")
        print("")
def read_my_csv():
    with open("list_of_notes.csv", encoding='utf=8') as file_name:
        file_read = csv.reader(file_name)
        array = list(file_read)
        for i in range(len(array)):
            for j in range(len(array[i])):
                print(array[i][j], end=' ')
            print()

def read_my_csv_for_detele_item():
    with open("list_of_notes.csv") as file_name:
        file_read = csv.reader(file_name)

        array = list(file_read)

        print(array)






