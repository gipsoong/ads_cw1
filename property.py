class Property:
    commission_rate = 0.01  # declared as a class attribute as it is a fixed value

    def __init__(self, address, postal_code, tenure, completion_year, property_type, area,
                 valuation):
        """Initialise attributes of Property class"""
        self.address = address
        self.postal_code = postal_code
        self.tenure = tenure
        self.completion_year = completion_year
        self.property_type = property_type
        self.area = area
        self.valuation = valuation

    def __str__(self):
        return f"{self.address}, {self.property_type}"
