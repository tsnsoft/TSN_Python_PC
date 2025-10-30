#!/usr/bin/env python3

"""Первичная подготовка html-файлов"""
import os


def scan_directory(scan_dir, scan_ext):
    """Получение списка файлов из нужного каталога"""
    found_files = []
    for root, dirs, files in os.walk(scan_dir):
        for name in files:
            if name.endswith(scan_ext):
                os.path.join(root, name)
                found_files.append(os.path.join(root, name))
    return found_files


def modify_file(file):
    """Модификация html-файла для использования"""
    repl1 = ('background:white', 'background:#FABF8F', 'background:#FFCC99', 'background:#B6DDE8',
             'background:yellow', 'background:#FFFEF2', 'background:#FEFEFE', 'background:#FFFEF7',
             'background:#F7F7F7')
    repl2 = ('font-family:Cambria;', 'font-family:Verdana;', 'font-family:"Cambria","serif";',
             'font-family:"Arial","sans-serif";', 'font-family:"Cambria","serif";',
             'font-family:"Verdana","sans-serif";', 'font-family:"Times New Roman","serif";')
    try:
        with open(file, 'r+', encoding='utf-8') as file_handler:
            lines = file_handler.read()
            for r1 in repl1:
                lines = lines.replace(r1, '')
            for r2 in repl2:
                lines = lines.replace(r2, 'font-family:mp_font;')
            lines = lines.replace('white', 'transparent')
            lines = lines.replace('text-decoration:underline', 'text-decoration:none')
            lines = lines.replace('mp_font, mp_font', 'mp_font')
            lines = lines.replace('"Verdana","sans-serif"', 'mp_font')
            file_handler.seek(0)
            file_handler.write(lines)
            file_handler.truncate()
            print("Обработан файл:", file)
    except Exception as e:
        print(e)
        print("Ошибка при обработке файла:", file)


def run():
    current_dir = os.path.abspath(os.curdir)
    print(current_dir)
    html_directory = os.path.join(current_dir, 'HTML')
    print(html_directory)

    htm_files = scan_directory(html_directory, (".htm"))
    print(htm_files)

    print("Найдено файлов для обработки:", len(htm_files))
    for file in htm_files:
        modify_file(file)


if __name__ == '__main__':
    run()
