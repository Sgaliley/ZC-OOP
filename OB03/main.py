import pickle


# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass  # Базовый метод, будет переопределен в подклассах

    def eat(self):
        print(f"{self.name} ест")


# Подклассы
class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        print("Чирик-чирик")

    def fly(self):
        print(f"{self.name} летает")


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print("Ррррр")


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print("Шшшшш")


# Полиморфизм: функция для вызова звука
def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} говорит:", end=" ")
        animal.make_sound()


# Классы сотрудников
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")


# Класс Zoo с композицией
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное: {animal.name}")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Добавлен сотрудник: {employee.name}")

    def list_animals(self):
        print("\nЖивотные в зоопарке:")
        for animal in self.animals:
            print(f"{animal.name}, возраст: {animal.age}")

    def list_employees(self):
        print("\nСотрудники зоопарка:")
        for employee in self.employees:
            print(employee.name)

    def save_to_file(self, filename='zoo_data.pkl'):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
        print("Зоопарк сохранён в файл.")

    @staticmethod
    def load_from_file(filename='zoo_data.pkl'):
        try:
            with open(filename, 'rb') as f:
                zoo = pickle.load(f)
            print("Зоопарк загружен из файла.")
            return zoo
        except FileNotFoundError:
            print("Файл не найден. Создан новый зоопарк.")
            return Zoo()


# --- Основной код ---
if __name__ == "__main__":
    # Создаём зоопарк
    my_zoo = Zoo()

    # Добавляем животных
    bird = Bird("Твитти", 2, 30)
    lion = Mammal("Лео", 5, "золотистый")
    snake = Reptile("Шустрый", 3, "гладкий")  # Теперь передан scale_type

    my_zoo.add_animal(bird)
    my_zoo.add_animal(lion)
    my_zoo.add_animal(snake)

    # Добавляем сотрудников
    keeper = ZooKeeper("Иван")
    vet = Veterinarian("Ольга")

    my_zoo.add_employee(keeper)
    my_zoo.add_employee(vet)

    # Полиморфизм: вызываем общий метод у разных объектов
    animal_sound(my_zoo.animals)

    # Используем методы сотрудников
    keeper.feed_animal(lion)
    vet.heal_animal(snake)

    # Сохраняем состояние зоопарка
    my_zoo.save_to_file()

    # Загружаем обратно
    loaded_zoo = Zoo.load_from_file()

    # Проверяем загруженный зоопарк
    loaded_zoo.list_animals()
    loaded_zoo.list_employees()
