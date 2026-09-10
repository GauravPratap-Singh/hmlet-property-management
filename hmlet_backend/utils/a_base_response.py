class ABaseResponse:
    def __init_(self,reason_code:int | None, message: str | None):
        self.reason_code: int | None = reason_code
        self.message: str | None = message