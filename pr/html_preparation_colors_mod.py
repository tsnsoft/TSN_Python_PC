#!/usr/bin/env python3

"""Вторичная подготовка html-файлов"""
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
    # color1 = "911E42"
    color1 = "911E42"
    color2 = "4F81BD"

    try:
        with open(file, 'r+', encoding='utf-8') as file_handler:
            lines = file_handler.read()
            lines = lines.replace(color2, color1)
            file_handler.seek(0)
            file_handler.write(lines)
            file_handler.truncate()
            print("Обработан файл:", file)
    except Exception as e:
        print(e)
        print("Ошибка при обработке файла:", file)


def run():
    current_dir = os.path.abspath(os.curdir)
    html_directory = os.path.join(current_dir, 'HTML')

    htm_files = scan_directory(html_directory, (".htm"))

    print("Найдено файлов для обработки:", len(htm_files))
    for file in htm_files:
        modify_file(file)


if __name__ == '__main__':
    run()
