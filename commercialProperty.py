from property import Property


class CommercialProperty(Property):

    def __init__(self, postal_code, tenure, completion_year, property_type, area, commission_rate, valuation,
                 commercial_property_type):
        super().__init__(postal_code, tenure, completion_year, property_type, area, commission_rate, valuation)
        """Initialise attributes of CommercialProperty class"""
        self.postal_code = postal_code
        self.tenure = tenure
        self.completion_year = completion_year
        self.property_type = property_type
        self.area = area
        self.commission_rate = commission_rate
        self.valuation = valuation
        self.commercial_property_type = commercial_property_type
