import os, sys
import json


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
    print("<font size='5'>")
    for form_key in form_keys_list:

        print(i, ": ", form_key, " = ", form.getvalue(form_key))
        i += 1
    print("</font>")

    if "experience" in form:
        print('<h3 class="main_text">Пример списка из строки запроса (experience): ', form.getvalue('experience'))
        strExperiences = form.getvalue('experience')
        print("strExperiences: ", strExperiences)
        intExperiences = list()
        for item in strExperiences: intExperiences.append(int(item))
        print("intExperiences: ", intExperiences, "   sum(intExperiences): ", sum(intExperiences))
        print('</h3>')

    try:
        print(" ")
    except Exception as identifier:
        print("\n\nОшибка в строке запроса")
        print(identifier)
    else:
        print("<h3 class='h3'>Решаем задание №2...</h3>")


def print_form_file(form):
    print("Отправляем данные на сервер...")
    print('<form  action="./form_action_file.py" target="_self" method="get">')
    # print('<form  action="./py_sql_pages.py" target="_self" method="get">')
    print('''
<!--Нижерасположенное удалять нельзя, редактировать можно-->
Название файла: <input type="Техт" name="000_file_name" value="g06u33_file.txt" >
Тип записи в файл:<select name="010_mode">
<OPTION value="a">a - дозаписать в файл(таблицу базы)</OPTION> 
    <OPTION value="w">w - очистить файл(таблицу базы) и записать </OPTION> 
    </select>
<input type="hidden" name="function" value="page">
<input type="hidden" name="page_id" value="8">
<input type="submit" name="submit" value="Отправить">
</form>
    ''')
    print("<a href = 'http://g05u48.nn2000.info/public_html/site/index_bash.htm' target='_self'>⮲Вернуться обратно</a>")


def file_list(form):
    print("<h3 class='h3'>Рeшаем пункт №1</h3>")
    arr = []
    arr.append(int(form["cat_1"].value))
    arr.append(int(form["cat_2"].value))
    arr.append(int(form["chmod_1"].value))
    arr.append(int(form["chmod_2"].value))
    arr.append(int(form["chmod_3"].value))
    arr.append(int(form["cp1251_utf8"].value))
    arr.append(int(form["drivehq_01"].value))
    arr.append(int(form["drivehq_02"].value))
    arr.append(int(form["homebz2"].value))
    arr.append(int(form["homebz3"].value))
    arr.append(int(form["iconv_01"].value))
    arr.append(int(form["iconv_02"].value))
    arr.append(int(form["ls_1"].value))
    arr.append(int(form["ls_home_cgi-bin"].value))
    arr.append(int(form["ls_home_public_html"].value))
    arr.append(int(form["mkdir_1"].value))
    arr.append(int(form["mkdir_2"].value))
    arr.append(int(form["mkdir_3"].value))
    arr.append(int(form["tarbz1"].value))
    print("<h3 class='main_text'>Сформированный массив баллов:", arr)
    print("Длина массива = ", len(arr))
    print("Сумма всех баллов = ", sum(arr))
    print("Среднее арифметическое всего массива = ", sum(arr) / len(arr))
    print("Максимум массива = ", max(arr))
    print("Минимум массива = ", min(arr),'</h3>')

    print("<h3 class='h3'>Рeшаем пункт №2</h3>")
    if "000_file_name" in form:
        file = "../tmp/" + form["000_file_name"].value
        print("\n<font size='5'>Записываем в:", file)
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
        print('</font>')

        listB = []  # для формирования списка из столбца файла
        r_stream = open(file, mode='r', encoding="utf-8")
        print("\n\n<h3 class='h3'>Построчно считываем строки из ", file, "и разбираем на слова</h3> "
                                                                         "<font size='5'>")
        for line in r_stream.readlines():
            print(line, end=' ')
            words = line.split(";")
            print(words)
            listB.append(int(words[15]))
        print("</font><h3 class='main_text'>")
        print("\nСписок из 16-го столбца файла:", listB)
        print("Длина 16 столбца = ", len(listB))
        print("Сумма 16 столбца = ", sum(listB))
        print("Среднее арифметическое = ", sum(listB) / len(listB))
        print("Максимальное число 16 столбца = ", max(listB))
        print("Мининальное число 16 столбца = ", min(listB),'<h3>')

