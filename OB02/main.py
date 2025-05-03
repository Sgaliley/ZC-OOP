from users import User, Admin


if __name__ == "__main__":
    # Создаем администратора
    admin = Admin("A001", "Иван")
    
    # Создаем обычных пользователей
    user1 = User("U001", "Александр")
    user2 = User("U002", "Мария")

    # Администратор добавляет пользователей
    admin.add_user(user1)
    admin.add_user(user2)

    # Попробуем добавить того же пользователя снова
    admin.add_user(user1)

    # Вывести список пользователей
    admin.list_users()

    # Удалить одного пользователя
    admin.remove_user("U001")

    # Вывести обновлённый список
    admin.list_users()