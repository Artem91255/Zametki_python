
def input_name_of_note():

    input_head = input("Введите название заметки:")
    return input_head + '.csv'

def input_body_of_note():

    imput_body = input("Введите заметку:")
    return imput_body

def choose():
    print('Выберите нужный пункт меню \n 1. Создать заметку \n 2. Просмотреть список заметок \n '
          '3. Редактировать заметку \n 4. Удалить заметку \n 6. Выход ')
    x = int(input('Введите нужный пукнт меню:'))

    return x