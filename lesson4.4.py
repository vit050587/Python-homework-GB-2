# 2.	Вычисляет урон по отношению к броне.
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.




player_name = input('Введите имя игрока')

player = {
    'name': player_name,
    'health': 100,
    'damage': 50,
    'armor' : 1.2
}

enemy_name = input('Введите врага')
enemy = {
    'name': enemy_name,
    'health': 50,
    'damage': 30,
    'armor' : 1
}
def get_damage(damage, armor):
    return damage / armor

def attack(unit, target):
    damage = get_damage(unit['damage'], target['armor'])
    target['health'] -= unit['damage']


attack(player, enemy)
print(enemy)

attack(enemy, player)
print(player)
