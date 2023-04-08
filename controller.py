import view
import log
import datetime

def add_note():

    name = input("Введите название заметки: ")

    note_name=name.split()
    name = name + ".csv"
    log.write_in_csv(name, note_name)


    notebody = input("Введите заметку: \n").split()
    log.write_in_csv(name, notebody)
    notedate = datetime.datetime.now()
    notedatestr = notedate.strftime("%d %b %Y").split()
    log.write_in_csv(name, notedatestr)
    # log.write_in_csv("")



def button_click_main():
    while (True):

        x = view.choose()
        if x==1:
            add_note()
            print("Заметка успешно создана")
        elif x == 6:
            print("Завершение работы программы.")
            break