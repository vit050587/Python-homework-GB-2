# Решить с помощью генераторов списка.
# 1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
#    Примечание: Списки фруктов создайте вручную в начале файла.

fruits1 = ['apple', 'banana', 'ogange', 'kiwi', 'pear']

fruits2 = ['banana', 'kiwi', 'tangerine']

result = []

for fruit in fruits1:
    if fruit in fruits2:
        result.append(fruit)

print(result)

result = [fruit for fruit in fruits1 if fruit in fruits2]

print(result)
