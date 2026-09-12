class CreateContractRequest:
    def __init__(
            self,
            member_id: int | None = None,
            unit_id: int | None = None,
            start_date: str | None = None,
            end_date: str | None = None,
            monthly_rent: str | None = None,
            created_by: int | None = None,
            ):
        self.member_id = member_id
        self.unit_id = unit_id
        self.start_date = start_date
        self.end_date = end_date
        self.monthly_rent = monthly_rent
        self.created_by = created_by