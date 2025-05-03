class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id     # Защищённый атрибут
        self.__name = name           # Защищённый атрибут
        self.__access_level = 'user' # Уровень доступа для обычных пользователей

    # Геттеры для доступа к защищённым атрибутам
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level
    
    def set_name(self, name):
        self.__name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'  # Уровень доступа администратора

        # Представим, что у нас есть список всех пользователей
        self.__users_list = []  # Защищённый список пользователей

    def get_access_level(self):
        return self.__access_level

    def add_user(self, user):
        """Добавляет пользователя в систему"""
        if isinstance(user, User):
            # Проверяем, не добавлен ли уже такой ID
            if not any(u.get_user_id() == user.get_user_id() for u in self.__users_list):
                self.__users_list.append(user)
                print(f"Пользователь {user.get_name()} добавлен.")
            else:
                print("Ошибка: Пользователь с таким ID уже существует.")
        else:
            print("Ошибка: Можно добавлять только объекты типа User.")

    def remove_user(self, user_id):
        """Удаляет пользователя по ID"""
        for user in self.__users_list:
            if user.get_user_id() == user_id:
                self.__users_list.remove(user)
                print(f"Пользователь с ID {user_id} удален.")
                return
        print("Ошибка: Пользователь не найден.")

    def list_users(self):
        """Выводит список всех пользователей"""
        print("\nСписок пользователей:")
        for user in self.__users_list:
            print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")
        print()
