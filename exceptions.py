class UserAlreadyExistsError(Exception):
    def __init__(self, username, message="Пользователь с таким именем уже существует."):
        self.username = username
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} Username: {self.username}"

class UserNotFoundError(Exception):
    def __init__(self, username, message="Пользователь с таким именем не найден."):
        self.username = username
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} Username: {self.username}"
