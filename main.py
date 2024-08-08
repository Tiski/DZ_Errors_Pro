from user import User
from user_manager import UserManager
from exceptions import UserAlreadyExistsError, UserNotFoundError

def main():
    user_manager = UserManager()

    # Пробуем добавить нескольких пользователей
    try:
        user1 = User(username="alice", email="alice@example.com", age=30)
        user_manager.add_user(user1)
        user2 = User(username="bob", email="bob@example.com", age=25)
        user_manager.add_user(user2)
        user3 = User(username="alice", email="alice_new@example.com", age=22)
        user_manager.add_user(user3)  # Должно вызвать UserAlreadyExistsError
    except UserAlreadyExistsError as e:
        print(e)

    # Пробуем удалить пользователя, которого нет
    try:
        user_manager.remove_user("charlie")  # Должно вызвать UserNotFoundError
    except UserNotFoundError as e:
        print(e)

    # Пробуем найти пользователя по имени
    try:
        user = user_manager.find_user("bob")
        print(user)
        user = user_manager.find_user("charlie")  # Должно вызвать UserNotFoundError
    except UserNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()
