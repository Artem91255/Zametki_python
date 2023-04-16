import operation
import view
import log
import datetime
from random import randint
#идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки
# Приложение должно запускаться без ошибок, должно уметь сохранять данные
# в файл, уметь читать данные из файла, делать выборку по дате, выводить на
# экран выбранную запись, выводить на экран весь список записок, добавлять
# записку, редактировать ее и удалять
import uuid
def add_note():

    name = input("Введите название заметки: ")
    notebody = input("Введите заметку: \n")

    notedate = operation.get_date_now()
    notedate_str = notedate.strftime("%d.%m.%Y %H:%M:%S")
    # notedate_obj = datetime.datetime.strptime(notedate, "%d.%m.%Y")
    id = uuid.uuid4()
    list_for_csv = []
    list_for_csv.append(id)
    list_for_csv.append(name)
    list_for_csv.append(notebody)
    list_for_csv.append(notedate_str)
    log.write_in_list(list_for_csv)


def remove_this_note():
    print("Вывожу список заметок:")
    log.show_id_of_notes()
    name_for_delete = input("Введите уникальный номер заметки, которую необходимо удалить: ")
    log.delete_in_csv(name_for_delete)

def read_from_csv():

    log.see_all_notes()

def edit_my_note():
    log.note_editor()


def filter_by_date():

    log.take_note_by_needed_date()


def button_click_main():
    while (True):

        x = view.choose()
        if x==1:
            add_note()
            print("Заметка успешно создана")
        elif x == 2:
            read_from_csv()
        elif x == 3:
            edit_my_note()
            print("Заметка успешно изменена")
        elif x == 4:
            remove_this_note()
            print("Заметка успешно удалена.")
        elif x == 5:
            filter_by_date()
            print("")
        elif x == 6:
            print("Завершение работы программы.")
            break