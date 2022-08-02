# import interface as Iface
# import output as ot
# import input as It

import easygui
from easygui import *
import input as ip
import output as op
import interface as inf
import change as ch
import delete

def main_menu():
    output = inf.menu()
    while True:
        match output:
            case 'Выход':
                break
            case 'Ученики':
                output_students = inf.menu_students()
                match output_students:
                    case 'Выход':
                        break
                    case 'Выход в главное меню':
                        output = inf.menu()
                    case 'Добавить ученика':
                        student_data = inf.menu_input_student()
                        try:
                            ip.input_data_student(student_data)
                        except TypeError:
                            msgbox('Не удалось добавить данные', 'Ошибка')
                            continue
                    case 'Удалить ученика':
                        student_data = inf.menu_delete_student()
                        try:
                            delete.delete_data_student(student_data)
                        except TypeError:
                            msgbox('Не удалось удалить данные', 'Ошибка')
                            continue
                    case 'Изменить данные об ученике':
                        new_student_data = inf.menu_change_student()
                        try:
                            ch.change_data_student(new_student_data)
                        except TypeError:
                            msgbox('Не удалось изменить данные', 'Ошибка')
                            continue
                    case 'Просмотреть все данные об учениках':
                        op.print_output_data_student(op.output_data_student())
            case 'Классы':
                output_class = inf.menu_class()
                match output_class:
                    case 'Выход':
                        break
                    case 'Выход в главное меню':
                        output = inf.menu()
                    case 'Добавить класс':
                        class_data = inf.menu_input_class()
                        try:
                            ip.input_data_class(class_data)
                        except TypeError:
                            continue
                    case 'Удалить класс':
                        inf.menu_delete_class()
                    case 'Изменить данные о классе':
                        inf.menu_change_class()
                    case 'Просмотреть данные обо всех классах':
                        op.print_output_data_class(op.output_data_class())


main_menu()

