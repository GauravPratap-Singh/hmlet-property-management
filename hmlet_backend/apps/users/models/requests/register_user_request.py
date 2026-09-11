class RegisterUserRequest:
    def __init__(self,
        username: str | None = None,
        email: str | None = None,
        password: str | None = None,
        ):
        self.username = username
        self.email = email
        self.password = password