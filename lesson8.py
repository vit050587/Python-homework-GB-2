# 1. В консольный файловый менеджер добавить проверку ввода пользователя
# для всех функции с параметрами (на уроке разбирали на примере одной функции).
# 2. Добавить возможность изменения текущей рабочей директории.
# 3. Добавить возможность развлечения в процессе работы с менеджером.
# Для этого добавить в менеджер запуск одной из игр: “угадай число” или “угадай число (наоборот)”.

import sys
from core import get_list, create_file, create_folder, delete_file, copy_file, get_work_dir, \
    change_work_folder, save_info
from game_reverse import game_reverse

save_info('Начало')
try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать команду! help')
else:

    if command == 'list':
        folder_only = False
        try:
            folder_only = bool(sys.argv[2])
        except:
            pass
        finally:
            get_list(folder_only)

    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)

    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)

    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла или папки')
        else:
            delete_file(name)

    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Отсутствуют названия файлов')
        else:
            copy_file(name, new_name)

    elif command == 'work_folder':
        get_work_dir()

    elif command == 'change_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            change_work_folder(name)

    elif command == 'game':
        game_reverse()

    elif command == 'help':
        print('Доступные команды:')
        print('   list          - вывод списка файлов и папок')
        print('   create_file   - создать новый файл')
        print('   create_folder - создать новую папку')
        print('   delete        - удалить файл или папку')
        print('   copy          - копировать файл или папку')
        print('   work_folder   - вывод рабочей директории')
        print('   change_folder - изменить рабочую директорию')
        print('   game          - игра "Угадай число (наоборот)"')
        print('   help          - показать доступные команды')

    save_info('Конец')
