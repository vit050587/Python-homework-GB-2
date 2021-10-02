import os, shutil, datetime


# создание файла
def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if (text):
            f.write(text)


# создание папки
def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')


# просмотр списка файлов и папок
def get_list(folder_only=False):
    result = os.listdir()
    if folder_only:
        result = [f for f in result if (os.path.isdir(f))]
    print(result)


# удаление файла или папки
def delete_file(name):
    try:
        if os.path.isdir(name):
            os.rmdir(name)
        else:
            os.remove(name)
    except FileNotFoundError:
        print('Файл не найден')


# копирование файла или папки
def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже есть')
    else:
        shutil.copy(name, new_name)


# текущая рабочая директория
def get_work_dir():
    return print(os.getcwd())


# изменить рабочий каталог
def change_work_folder(name):
    if (os.path.exists(name)):
        try:
            if (os.path.isdir(name)):
                os.chdir(name)
                print(os.listdir())
        except:
            print('Не удается изменить каталог')
        else:
            print('Текущая рабочая директория = ' + os.getcwd())
    else:
        print('Такого пути не существует')


# запись информации в файл
def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')
