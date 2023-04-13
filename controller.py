import view
import log
import datetime
from random import randint
#идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки
# Приложение должно запускаться без ошибок, должно уметь сохранять данные
# в файл, уметь читать данные из файла, делать выборку по дате, выводить на
# экран выбранную запись, выводить на экран весь список записок, добавлять
# записку, редактировать ее и удалять
def add_note():

    name = input("Введите название заметки: ")
    notebody = input("Введите заметку: \n")

    notedate = datetime.datetime.now()
    notedate_str = notedate.strftime("%d %b %Y")
    random_number =randint(0,10000)
    list_for_csv = []
    list_for_csv.append(random_number)
    list_for_csv.append(name)
    list_for_csv.append(notebody)
    list_for_csv.append(notedate_str)
    log.write_in_list(list_for_csv)

def remove_this_note():
    name_for_delete = input("Введите имя заметки, которую необходимо удалить: ")
    log.delete_csv(name_for_delete)

def read_from_csv():
    # name = input("Введите название заметки: ")
    log.read_my_csv()




def button_click_main():
    while (True):

        x = view.choose()
        if x==1:
            add_note()
            print("Заметка успешно создана")
        elif x == 2:
            read_from_csv()

        elif x == 4:
            remove_this_note()
            print("Заметка успешно удалена.")
        elif x == 6:
            print("Завершение работы программы.")
            break