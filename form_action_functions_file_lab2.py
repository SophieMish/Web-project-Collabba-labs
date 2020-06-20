import os, sys
import random


def solve_lab2(a, b, c):
    print(
        "\n<h3 class='h3'>№2020. Используя генератор случайных чисел получить одномерный массив числовых значений,насчитывающий А элементов в диапазоне В-С.\n"
        "Определить, имеются ли в массиве два числа из задаваемого диапазона, которые размещены последовательно и сообщить их индексы и значения.\n"
        "Для  Бизнес-информатики, дополнительно определить\n"
        "- сумму всех элеменов массива\n"
        "- количество и сумму  положительных и отрицательных элементов массива\n"
        "- среднее, максимальное,  минимальное значение данных в массиве</h3>")
    print("\n<h3 class='h'>РЕШЕНИЕ №2020</h3>")
    print("\n<h3 class='main_text'>Размер: ", a)
    print("Диапазон: oт", b, "до", c)
    arr = []
    for i in range(a):
        arr.append(random.randrange(b, c))
    print("\nВаш массив", arr)
    try:
        for i in range(len(arr)):
            if arr[i] - arr[i + 1] == -1:
                print(" ")
                print("Найденный элемент = ", arr[i], " Его индекс = ", i + 1)
                print("Найденный элемент = ", arr[i + 1], " Его индекс = ", i + 2)
            elif arr[i] - arr[i + 1] == 1:
                print(" ")
                print("Найденный элемент = ", arr[i], " Его индекс = ", i + 1)
                print("Найденный элемент = ", arr[i + 1], " Его индекс = ", i + 2)
            elif arr[i] == arr[i + 1]:
                print(" ")
                print("Найденный элемент = ", arr[i], " Его индекс = ", i + 1)
                print("Найденный элемент = ", arr[i + 1], " Его индекс = ", i + 2)
    except IndexError:
        print(" ")
    except ValueError:
        print(" ")
    print("Сумма всех элементов = ", sum(arr))
    p = 0
    n = 0
    z = 0
    for i in range(a):
        if arr[i] > 0:
            p += 1
        elif arr[i] < 0:
            n += 1
        else:
            z += 1
    print("\nПоложительных: ", p)
    print("Отрицательных: ", n)
    print("Равных нулю: ", z)
    print("\nМаксимум в массиве = ", max(arr))
    print("Минимум в массиве = ", min(arr))
    print("Среднее арифметическое массива = ", sum(arr) / len(arr))
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
    i = 0
    for form_key in form_keys_list:
        # print(i, ": ", form_key, " = ", form.getvalue(form_key))
        i += 1

    if "experience" in form:
        #print('\n\n Пример списка из строки запроса (experience): ', form.getvalue('experience'))
        strExperiences = form.getvalue('experience')
        #print("strExperiences: ", strExperiences)
        intExperiences = list()
        for item in strExperiences: intExperiences.append(int(item))
        #print("intExperiences: ", intExperiences, "   sum(intExperiences): ", sum(intExperiences), "\n")

    try:
        a = int(form.getvalue('a'))
        b = int(form.getvalue('b'))
        c = int(form.getvalue('c'))
        print(" ")
    except Exception as identifier:
        print(" ")
    else:
        solve_lab2(a, b, c)


def print_form_file(form):
    print('<form  action="./form_action_file.py" target="_self" method="get">')
    # print('<form  action="./py_sql_pages.py" target="_self" method="get">')
    print('''\
<!--Нижерасположенное удалять нельзя, редактировать можно-->
Введите размер массива A: <input type="Text" name="a" value="10" size="8"> 
Введите первое число диапазона B: <input type="Text" name="b" value="-5" size="8">
Введите второе число диапазона C: <input type="Text" name="c" value="10" size="8"></h3>
\n------------------------------------------------------------------------------\n
<!--Нижерасположенное удалять нельзя, редактировать можно-->
Название файла: <input type="Техт" name="000_file_name" value="g05u48_lab2.txt" >
Тип записи в файл:<select name="010_mode">
<OPTION value="a">a - дозаписать в файл(таблицу базы)</OPTION> 
    <OPTION value="w">w - очистить файл(таблицу базы) и записать </OPTION> 
    </select>
<input type="hidden" name="function" value="page">
<input type="hidden" name="page_id" value="8">
<input type="submit" name="submit" value="Отправить">
</form>
    ''')

def file_list(form):
    if "000_file_name" in form:
        file = "../tmp/txt/" + form["000_file_name"].value
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

    # listB = list()  # для формирования списка из столбца файла
    # r_stream = open(file, mode='r', encoding="utf-8")
    # print("\n\nПострочно считываем строки из ", file, "и разбираем на слова")
    # for line in r_stream.readlines():
    #     print(line, end='')
    # words = line.split(";")
    # print(words)
    # listB.append(words[15])
    # print("\nlistB(Список из 16-го столбца файла):", listB)
    # print("listB.__len__():", listB.__len__())