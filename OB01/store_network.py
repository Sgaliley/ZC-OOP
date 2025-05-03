class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Добавлен товар: {item_name}, цена: {price}, в магазин {self.name}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Удалён товар: {item_name}")
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")

    def get_item_price(self, item_name):
        return self.items.get(item_name)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Обновлена цена на '{item_name}' на {new_price}")
        else:
            print(f"Товар '{item_name}' не найден.")
