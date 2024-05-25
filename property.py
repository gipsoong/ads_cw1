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
        self.commission_rate = 0.01

    def get_address(self):
        return f"Address: {self.address}"

    def get_postal_code(self):
        return f"Postal Code: {self.postal_code}"

    def get_tenure(self):
        return f"Tenure: {self.tenure}"

    def get_completion_year(self):
        return f"Completed in: {self.completion_year}"

    def get_property_type(self):
        return f"Property Type: {self.property_type}"

    def get_area(self):
        return f"Size of property: {self.area}"

    def get_valuation(self):
        return f"Valuation: P${self.valuation:,.2f}"

    def get_commission_rate(self):
        return f"Commission rate: {self.commission_rate}"

    def __str__(self):
        return (f"- - - - - - - - - - \n"
                f"{self.address} ({self.property_type}) {self.postal_code}, completed in {self.completion_year}. \n"
                f"Total area of {self.area}, valued at P${self.valuation:,.2f} \n"
                f"Current tenure is {self.tenure} \n"
                f"Agent commission rate is fixed at {(self.commission_rate * 100):.0f}% of valuation. \n" 
                f"- - - - - - - - - -")
