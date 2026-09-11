class ABaseResponse:
    def __init__(self,reason_code:int | None, message: str | None):
        self.reason_code: int | None = reason_code
        self.message: str | None = message