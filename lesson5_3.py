# Создайте модуль main.py.
# Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций.
# Вызовите каждую функцию в main.py и проверьте что все работает как надо.
# Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1),
# так и отдельные функции из модуля.

import lesson5_2
from lesson5_1 import create_folders, delete_folders


create_folders()
delete_folders()
print(lesson5_2.get_random([1, 2, 3, 4]))
print(lesson5_2.get_random([]))