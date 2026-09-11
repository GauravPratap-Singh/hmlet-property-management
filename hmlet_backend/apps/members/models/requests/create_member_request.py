class CreateMemberRequest:
    def __init__(self,
        first_name: str | None = None,
        last_name: str | None = None,
        email: str | None = None,
        created_by: int | None = None,
        ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_by = created_by