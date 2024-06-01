from property import Property


class CommercialProperty(Property):

    def __init__(self, address, postal_code, tenure, completion_year, property_type, area, valuation,
                 commercial_property_type):
        super().__init__(address, postal_code, tenure, completion_year, property_type, area, valuation)
        """Initialise attributes of CommercialProperty class"""
        self.address = address
        self.postal_code = postal_code
        self.tenure = tenure
        self.completion_year = completion_year
        self.property_type = property_type
        self.area = area
        self.valuation = valuation
        self.commercial_property_type = commercial_property_type

    # custom class for CommercialProperty
    def get_commercial_property_type(self):
        if self.check_commercial_property_type():
            return f"Commercial Property Type: {self.commercial_property_type}"

        else:
            return (f"ERROR! Commercial Property Type '{self.commercial_property_type}' is invalid. Ensure that it is"
                    f" either 'Office', 'Factory' or 'Flatted Factory'.")

    def check_property_type(self):
        """Method to validate if property_type is Commercial"""
        if self.property_type.lower() == "commercial":
            return True
        else:
            return False

    def check_commercial_property_type(self):
        """Method to validate if commercial_property_type is one of the expected values: Office, Flatted Factory
        or Factory"""
        if (self.commercial_property_type.lower() == "office"
                or self.commercial_property_type.lower() == "factory"
                or self.commercial_property_type.lower() == "flatted factory"):
            return True
        else:
            return False

    def check_all_commercial_property(self):
        """Method to run all CommercialProperty checks"""
        if (self.check_address()
                and self.check_postal_code()
                and self.check_completion_year()
                and self.check_property_type()
                and self.check_commercial_property_type()
                and self.check_valuation()):
            return True

        else:
            return False

    def __str__(self):
        if self.check_address():
            return (f"- - - - - - - - - - \n"
                    # modifying this part of the string to better suit CommercialProperty
                    f"{self.address} ({self.property_type} {self.commercial_property_type}) {self.postal_code}, "
                    f"completed in {self.completion_year}. \n"
                    f"Total area of {self.area}, valued at P${self.valuation:,.2f} \n"
                    f"Current tenure is {self.tenure} \n"
                    f"Agent commission rate is fixed at {(self.commission_rate * 100):.0f}% of valuation. \n"
                    f"- - - - - - - - - -")

        else:
            return (f"ERROR! There seems to be a problem with one or more of the attributes."
                    f" Resolve the errors before printing this class!")
