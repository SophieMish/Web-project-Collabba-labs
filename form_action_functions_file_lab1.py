import os, sys
import random


def solve_lab1(num):
    print("\n<h3 class='h3'>№1002. Дано вещественное число. Определить, какое это число: положительное, отрицательное, ноль.</h3>")
    print("\n<h3 class='h'>РЕШЕНИЕ №1002</h3>")
    print("\n<h3 class='main_text'>Было введено число: ", num)
    if num > 0:
        print("Число положительное")
    elif num < 0:
        print("Число отрицательное")
    elif num == 0:
        print("Число равно нулю")
    print("\n------------------------------------------------------------------------------")


def form_dictionary(form):
    form_keys_list = list()
    form_values_list = list()
    form_values_dict = dict()
    i = 0
    for form_key in form.keys():
        form_keys_list.append(form_key)
        form_values_list.append(form.getvalue(form_key))
        form_values_dict.update({form_key: form.getvalue(form_key)})
        i += 1
    form_keys_list.sort()
    # i = 0
    # for form_key in form_keys_list:
    #     print(i, ": ", form_key, " = ", form.getvalue(form_key))
    #     i += 1

    if "experience" in form:
        #print('\n\n Пример списка из строки запроса (experience): ', form.getvalue('experience'))
        strExperiences = form.getvalue('experience')
        #print("strExperiences: ", strExperiences)
        intExperiences = list()
        for item in strExperiences: intExperiences.append(int(item))
        #print("intExperiences: ", intExperiences, "   sum(intExperiences): ", sum(intExperiences), "\n")

    try:
        num = float(form.getvalue('num'))
        print(" ")
    except Exception as identifier:
        print(" ")
    else:
        solve_lab1(num)



def print_form_file(form):
    print('<form  action="./form_action_file.py" target="_self" method="get">')
    # print('<form  action="./py_sql_pages.py" target="_self" method="get">')
    print('''\
<!--Нижерасположенное удалять нельзя, редактировать можно-->
Введите вещественное число: <input type="Техт" name="num" value="0" >
\n------------------------------------------------------------------------------\n
Название файла: <input type="Техт" name="000_file_name" value="g05u48_lab1.txt" >
Тип записи в файл:<select name="010_mode"></h3>
<OPTION value="a">a - дозаписать в файл(таблицу базы)</OPTION> 
    <OPTION value="w">w - очистить файл(таблицу базы) и записать </OPTION> 
    </select>
<input type="hidden" name="function" value="page">
<input type="hidden" name="page_id" value="8">
<input type="submit" name="submit" value="Отправить">
</form>
    ''')


def file_list(form):
    global file_stream, form_key, form_value, line, file
    if "000_file_name" in form:
        file = "../tmp/" + form["000_file_name"].value
    print("\nЗаписываем в:", file)
    if (form["010_mode"].value == 'w'):  # 0 - очищаем файл
        file_stream = open(file, mode='w', encoding="utf-8", errors=None)
    file_stream.close()
    file_stream = open(file, mode='a', encoding="utf-8", errors=None)
    form_keys_list = list()
    for form_key in form.keys():
        form_keys_list.append(form_key)
    form_keys_list.sort()
    for form_key in form_keys_list:
        form_value = form.getvalue(form_key)
    file_stream.write("%1s;%1s;" % (form_key, form_value))
    sys.stdout.write("%1s;%1s;" % (form_key, form_value))
    file_stream.write("\n")
    file_stream.close()

    listB = list()  # для формирования списка из столбца файла
    r_stream = open(file, mode='r', encoding="utf-8")
    print("\n\nПострочно считываем строки из ", file, "и разбираем на слова")
    for line in r_stream.readlines():
        print(line, end='')
    words = line.split(";")
    print(words)
    listB.append(words[15])
    print("\nlistB(Список из 16-го столбца файла):", listB)
    print("listB.__len__():", listB.__len__())
