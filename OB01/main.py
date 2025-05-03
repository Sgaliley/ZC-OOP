from task_manager import TaskManager
from store_network import Store


if __name__ == "__main__":
    # Управление задачами
    tm = TaskManager()
    tm.add_task("Купить продукты", "2025-04-05")
    tm.add_task("Созвон с командой", "2025-04-06")
    tm.add_task("Подготовить отчёт", "2025-04-07")

    tm.show_current_tasks()

    print("\nОтмечаем первую задачу как выполненную...")
    tm.complete_task(0)
    tm.show_current_tasks()

    print("\n--- Работа с магазинами ---\n")

    # Создание магазинов
    store1 = Store("Фруктовый Рай", "ул. Ленина, д. 10")
    store2 = Store("Молочный Дом", "ул. Пушкина, д. 5")
    store3 = Store("Бакалея+", "пр. Мира, д. 18")

    # Добавляем товары
    store1.add_item("яблоки", 0.5)
    store1.add_item("бананы", 0.75)

    store2.add_item("молоко", 1.2)
    store2.add_item("кефир", 1.5)

    store3.add_item("сахар", 2.0)
    store3.add_item("соль", 0.3)

    # Тестирование методов одного из магазинов
    print(f"\nТестируем магазин: {store1.name}, адрес: {store1.address}")
    store1.add_item("апельсины", 0.9)
    print("Цена яблок:", store1.get_item_price("яблоки"))
    store1.update_item_price("яблоки", 0.6)
    print("Обновлённая цена яблок:", store1.get_item_price("яблоки"))
    store1.remove_item("бананы")
    print("После удаления бананов:", store1.items)
