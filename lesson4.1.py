#1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

def person_info(name, age,city):
    result = f'{name}, {age} год(а) проживает в городе {city}'
    return result


print(person_info('Василий', 21, 'Москва'))
print(person_info('Костя', 21, 'Пермь'))
print(person_info('Криска', 21, 'Пенза'))
print(person_info('Вова', 21, 'Мытищи'))
print(person_info('Андр', 21, 'Москва'))