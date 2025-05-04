import random

# Класс героя
class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        if other.health < 0:
            other.health = 0
        print(f"{self.name} атаковал. У {other.name} осталось {other.health} здоровья.")

    def is_alive(self):
        return self.health > 0

# Класс игры
class Game:
    def __init__(self):
        self.player = Hero("Игрок")
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!")
        while True:
            # Ход игрока
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.player.name} победил!")
                break

            # Ход компьютера
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.computer.name} победил!")
                break

# Запуск игры
if __name__ == "__main__":
    game = Game()
    game.start()