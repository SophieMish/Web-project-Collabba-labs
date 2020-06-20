#!/usr/bin/env python3.4
import os, sys
import cgi, cgitb
import form_action_functions_file_bash
import form_action_functions_file_lab1
import form_action_functions_file_lab2

cgitb.enable()
sys.stderr = sys.stdout
form = cgi.FieldStorage()


def form_action_file_bash(form):
    print("<pre>")

    form_action_functions_file_bash.form_dictionary(form)  # Анализируем строку запроса
    form_action_functions_file_bash.file_list(form)  # Записываем в файл и оцениваем содержание файла
    form_action_functions_file_bash.print_form_file(form)  # Создаем форму и отправляем данные на сервер
    print("</pre>")


def form_action_file_lab1(form):
    print("<pre>")
    form_action_functions_file_lab1.form_dictionary(form)  # Анализируем строку запроса
    form_action_functions_file_lab1.print_form_file(form)  # Создаем форму и отправляем данные на сервер
    form_action_functions_file_lab1.file_list(form)  # Записываем в файл и оцениваем содержание файла
    print("</pre>")


def form_action_file_lab2(form):
    print("<pre>")
    form_action_functions_file_lab2.form_dictionary(form)  # Анализируем строку запроса
    form_action_functions_file_lab2.print_form_file(form)  # Создаем форму и отправляем данные на сервер
    form_action_functions_file_lab2.file_list(form)  # Записываем в файл и оцениваем содержание файла
    print("</pre>")

if __name__ == '__main__':
    print("Content-type:text/html\r\n")
    print(
        "<html>",
        "<head>",
        "<title>Работа по ТОИ</title>",
       "<link href='https://fonts.googleapis.com/css2?family=Poiret+One&display=swap' rel='stylesheet'>"
       '<link rel="stylesheet" href="../public_html/site/labs.css">',
        "</head>",
        "<body style='background-color:white'>")

    if form.getvalue('chmod_1'):
        form_action_file_bash(form)
    elif form.getvalue('num'):
        form_action_file_lab1(form)
    else:
        form_action_file_lab2(form)
