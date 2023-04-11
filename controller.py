import view
import log
import datetime

def add_note():

    name = input("Введите название заметки: ")

    note_name=name.split()
    name = name + ".csv"
    #log.write_in_csv(name, note_name)


    notebody = input("Введите заметку: \n").split()

    log.write_in_csv(name, notebody)
    notedate = datetime.datetime.now()
    notedate_str = notedate.strftime("%d %b %Y").split()
    name_for_list = name.split()
    #log.write_in_csv(name, notedate_str)
    log.write_in_list(name_for_list, notedate_str)

def remove_this_note():
    name_for_delete = input("Введите имя заметки, которую необходимо удалить: ")
    log.delete_csv(name_for_delete)






def button_click_main():
    while (True):

        x = view.choose()
        if x==1:
            add_note()
            print("Заметка успешно создана")
        elif x == 4:
            remove_this_note()
            print("Заметка успешно удалена.")
        elif x == 6:
            print("Завершение работы программы.")
            break