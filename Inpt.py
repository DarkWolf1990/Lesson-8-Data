

def Reader():

            x = input('Введите Фамилию:')
            y = input('Введите Имя:')
            z = input('Введите телефон:')
            h = input('Введите номер класса:')
            return x+y+z+h

Reader()
            
 # Метод считывает и возвращает считанные данные с файла file_name
def read_text_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read()
    return data

# Метод позволяет записать текст в файл
def write_text_in_file(file_name, text):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(text)
           


import hello as h  

print(h.f(1))

import hello as h  

print(h.f(1))

        
            