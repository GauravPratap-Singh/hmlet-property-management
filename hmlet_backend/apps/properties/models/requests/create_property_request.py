class CreatePropertyRequest:
    def __init__(
        self,
        property_name: str | None = None,
        address_line1: str | None = None,
        address_line2: str | None = None,
        postcode: str | None = None,
        country: str | None = None,
        created_by: int | None = None,
    ):
        self.property_name = property_name
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.postcode = postcode
        self.country = country
        self.created_by = created_by