def add_user(users, name, age):
    """Добавляет пользователя в словарь"""
    try:
        age = int(age)
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        users[name] = age
        print(f"Пользователь {name} успешно добавлен")
    except ValueError as e:
        print(f"Ошибка: {e}. Возраст должен быть целым положительным числом")

def remove_user(users, name):
    """Удаляет пользователя по имени"""
    if name in users:
        del users[name]
        print(f"Пользователь {name} успешно удален")
    else:
        print(f"Ошибка: Пользователь {name} не найден")

def list_users(users):
    """Выводит список всех пользователей"""
    if not users:
        print("Список пользователей пуст")
    else:
        print("Список пользователей:")
        for name, age in users.items():
            print(f"- {name}: {age} лет")