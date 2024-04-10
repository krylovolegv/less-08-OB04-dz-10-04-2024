# Задача: Разработать простую игру, где игрок может использовать различные типы оружия
# для борьбы с монстрами. Программа должна быть спроектирована таким образом, чтобы легко
# можно было добавлять новые типы оружия, не изменяя существующий код бойцов или механизм боя

from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")

class Bow(Weapon):
    def attack(self):
        print("Боец наносит удар из лука.")

class Fighter:
    def __init__(self):
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon

    def fight(self, monster):
        if self.weapon:
            self.weapon.attack()
        else:
            print("Боец без оружия.")
        print(f"Монстр побежден!")

class Monster:
    pass

def play_game():
    fighter = Fighter()
    monster = Monster()  # Здесь должен быть класс Monster.

    weapons = [Sword(), Bow()]  # Список всех доступных оружий

    while True:
        print("Выберите оружие: 1 - Меч, 2 - Лук.")
        choice = int(input())
        if choice == 1:
            fighter.change_weapon(weapons[0])
        elif choice == 2:
            fighter.change_weapon(weapons[1])
        else:
            print("Неверный выбор.")
            continue

        fighter.fight(monster)

        answer = input("Хотите продолжить? (y/n)")
        if answer != 'y':
            break

play_game()


