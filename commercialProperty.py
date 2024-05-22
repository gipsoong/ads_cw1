from property import Property


class CommercialProperty(Property):
    # property_type is set to a default of "commercial", as it is to remain unchanged

    def __init__(self, postal_code, tenure, completion_year, area, valuation, commercial_property_type, address,
                 property_type):
        """Initialise attributes of CommercialProperty class"""
        super().__init__(address, postal_code, tenure, completion_year, property_type, area, valuation)
        self.postal_code = postal_code
        self.tenure = tenure
        self.completion_year = completion_year
        self.area = area
        self.valuation = valuation
        self.commercial_property_type = commercial_property_type
        self.property_type = "Commercial"
