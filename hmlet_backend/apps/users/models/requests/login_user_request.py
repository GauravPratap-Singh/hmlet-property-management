class LoginUserRequest:
    def __init__(self,
        username: str | None = None,
        password: str | None = None,
        ):
        self.username = username
        self.password = password