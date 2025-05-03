from abc import ABC, abstractmethod


# Шаг 1: Абстрактный класс Weapon
class Weapon(ABC):
    @abstractmethod
    def attack(self) -> str:
        pass


# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self) -> str:
        return "удар мечом"


class Bow(Weapon):
    def attack(self) -> str:
        return "выстрел из лука"


# Шаг 3: Класс Fighter
class Fighter:
    def __init__(self, name: str):
        self.name = name
        self.weapon: Weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self, monster: 'Monster'):
        if self.weapon is None:
            print(f"{self.name} не выбрал оружие.")
            return False
        action = self.weapon.attack()
        print(f"{self.name} наносит {action}.")
        return monster.take_damage()


# Класс Monster
class Monster:
    def __init__(self, health: int = 1):
        self.health = health

    def take_damage(self) -> bool:
        self.health -= 1
        if self.health <= 0:
            print("Монстр побеждён!")
            return True
        else:
            print("Монстр всё ещё жив.")
            return False

    def is_defeated(self) -> bool:
        return self.health <= 0


# Шаг 4: Демонстрация боя
def battle_simulator():
    fighter = Fighter("Боец")
    monster = Monster()

    print("=== Бой начинается ===")

    # Боец выбирает меч
    fighter.change_weapon(Sword())
    print("Боец выбирает меч.")
    if fighter.attack(monster):
        print("Бой окончен.\n")

    # Новый бой
    monster = Monster()
    print("=== Новый бой ===")

    # Боец выбирает лук
    fighter.change_weapon(Bow())
    print("Боец выбирает лук.")
    if fighter.attack(monster):
        print("Бой окончен.")


# Запуск симуляции
if __name__ == "__main__":
    battle_simulator()
