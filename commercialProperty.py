from property import Property


class CommercialProperty(Property):

    def __init__(self, address, postal_code, tenure, completion_year, property_type, area, valuation,
                 commercial_property_type):
        super().__init__(address, postal_code, tenure, completion_year, property_type, area, valuation)
        self.commercial_property_type = commercial_property_type  # why must this be the first?
        self.address = address
        self.postal_code = postal_code
        self.tenure = tenure
        self.completion_year = completion_year
        self.property_type = property_type
        self.area = area
        self.valuation = valuation

    def check_commercial_property_type(self):
        """A function to validate if commercial_property_type is one of the expected values: Office, Flatted Factory
        or Factory"""
        if (self.commercial_property_type.lower() == "office"
                or self.commercial_property_type.lower() == "factory"
                or self.commercial_property_type.lower() == "flatted factory"):
            return True
        else:
            return False

    # custom class for CommercialProperty
    def get_commercial_property_type(self):
        if self.check_commercial_property_type():
            return f"Commercial Property Type: {self.commercial_property_type}"

        else:
            return (f"ERROR! Commercial Property Type '{self.commercial_property_type}' is invalid. Ensure that it is"
                    f" either 'Office', 'Factory' or 'Flatted Factory'")

    def __str__(self):
        if self.check_commercial_property_type():
            return (f"- - - - - - - - - - \n"
                    # modifying this part of the string to better suit CommercialProperty
                    f"{self.address} ({self.property_type} {self.commercial_property_type}) {self.postal_code}, completed "
                    f"in {self.completion_year}. \n"
                    f"Total area of {self.area}, valued at P${self.valuation:,.2f} \n"
                    f"Current tenure is {self.tenure} \n"
                    f"Agent commission rate is fixed at {(self.commission_rate * 100):.0f}% of valuation. \n"
                    f"- - - - - - - - - -")

        else:
            return (f"ERROR! Commercial Property Type '{self.commercial_property_type}' is invalid. Ensure that it is"
                    f" either 'Office', 'Factory' or 'Flatted Factory'")

