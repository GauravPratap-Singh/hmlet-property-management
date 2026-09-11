class CreateUnitRequest:
    def __init__(
        self,
        unit_number: str | None = None,
        monthly_rent: str | None = None,
        status: str | None = None,
        properties_id: int | None = None,
        created_by: int | None = None,
    ):
        self.unit_number = unit_number
        self.monthly_rent = monthly_rent
        self.status = status
        self.properties_id = properties_id
        self.created_by = created_by
