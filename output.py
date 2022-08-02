# def read_text_from_file(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         data = file.read()
#     print("data")

import csv
from easygui import *
import input as ip

def output_data_student():
    dict_data_student = {}
    with open('student_base.csv', 'r', encoding='cp1251') as sb:
        file_reader = csv.DictReader(sb, delimiter=";")
        count = 0
        for row in sb:
            if count > 0:
                try:
                    data_student = row.split(';')
                    # print(data_student)
                    student_id, surname, name, date_of_birth = data_student
                    date_of_birth = date_of_birth.replace('\n', '')
                    dict_data_student[int(student_id)] = [surname, name, date_of_birth]
                except ValueError:
                    continue
            count += 1
    return dict_data_student

def print_output_data_student(dict_data_student):
    title = 'Данные о учениках'
    text = ''
    for i in dict_data_student.keys():
        count = 0
        text += f'id ученика = {i}; '
        for j in dict_data_student[i]:
            if count == 0:
                text += f'Фамилия: {j}; '
                count += 1
            elif count == 1:
                text += f'Имя: {j}; '
                count += 1
            elif count == 2:
                text += f'Дата рождения: {j}'
                count += 1
        text += '\n'
    msgbox(text, title)

def output_data_class():
    dict_data_class = {}
    with open('class_base.csv', 'r', encoding='cp1251') as сb:
        file_reader = csv.DictReader(сb, delimiter=";")
        count = 0
        for row in сb:
            if count > 0:
                try:
                    data_class = row.split(';')
                    class_id, number, letter = data_class
                    letter = letter.replace('\n', '')
                    dict_data_class[int(class_id)] = [number, letter]
                except ValueError:
                    continue
            count += 1
    return dict_data_class

# print(output_data_class())

def print_output_data_class(dict_data_class):
    title = 'Данные о классах'
    text = ''
    for i in dict_data_class.keys():
        count = 0
        text += f'id класса = {i}; '
        for j in dict_data_class[i]:
            if count == 0 :
                text += f'Класс: {j}'
                count += 1
            elif count == 1:
                text += f'{j}'
                count += 1
        text += '\n'
    msgbox(text, title)
