class Property:
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
        self.commission_rate = 0.01  # fixed value of 1%

    def get_address(self):
        if self.check_address():
            return f"Address: {self.address}"
        else:
            return (f"ERROR! Address '{self.address}' is invalid. Ensure that it is"
                    f" an integer and more than 0!")

    def get_postal_code(self):
        if self.check_postal_code():
            return f"Postal Code: {self.postal_code}"
        else:
            return (f"ERROR! Postal Code '{self.postal_code}' is invalid. Ensure that it is"
                    f" a string and six digits!")

    def get_tenure(self):
        return f"Tenure: {self.tenure}"

    def get_completion_year(self):
        if self.check_completion_year():
            return f"Completed in: {self.completion_year}"
        else:
            return (f"ERROR! Completion Year '{self.completion_year}' is invalid. Ensure that it is"
                    f" an integer and between the year 1800 and 3000!")

    def get_property_type(self):
        if self.check_property_type():
            return f"Property Type: {self.property_type}"
        else:
            return (f"ERROR! Property Type '{self.property_type}' is invalid. Ensure that it is"
                    f" a string and either 'HDB', 'Landed' or 'Condo'.")

    def get_area(self):
        return f"Size of property: {self.area}"

    def get_valuation(self):
        if self.check_valuation():
            return f"Valuation: P${self.valuation:,.2f}"
        else:
            return (f"ERROR! Valuation of '{self.property_type}' is invalid. Ensure that it is"
                    f" an integer and more than 0!")

    def get_commission_rate(self):
        return f"Commission rate: {self.commission_rate}"

    def check_address(self):
        """Method to validate if address is a string"""
        if isinstance(self.address, str):
            return True
        else:
            return False

    def check_postal_code(self):
        """Method to validate if postal_code is an integer and six digits"""
        if isinstance(self.postal_code, int) and (99999 < self.postal_code <= 999999):
            return True
        else:
            return False

    def check_completion_year(self):
        """Method to validate if completion_year is an integer and within a realistic range"""
        if isinstance(self.completion_year, int) and (1800 < self.completion_year <= 3000):
            return True
        else:
            return False

    def check_property_type(self):
        """Method to validate if commercial_property_type is one of the expected values: Office, Flatted Factory
        or Factory"""
        if (self.property_type.lower() == "hdb"
                or self.property_type.lower() == "landed"
                or self.property_type.lower() == "condo"
                or self.property_type.lower() == "condominium"):
            return True
        else:
            return False

    def check_valuation(self):
        """Method to validate if valuation is more than 0"""
        if isinstance(self.valuation, int) and self.valuation > 0:
            return True
        else:
            return False

    def check_all_property(self):
        """Method to run all Property checks"""
        if (self.check_address()
                and self.check_postal_code()
                and self.check_completion_year()
                and self.check_property_type()
                and self.check_valuation()):
            return True

        else:
            return False

    def __str__(self):
        if self.check_all_property():
            return (f"- - - - - - - - - - \n"
                    f"{self.address} ({self.property_type}) {self.postal_code}, completed in {self.completion_year}. \n"
                    f"Total area of {self.area}, valued at P${self.valuation:,.2f} \n"
                    f"Current tenure is {self.tenure} \n"
                    f"Agent commission rate is fixed at {(self.commission_rate * 100):.0f}% of valuation. \n"
                    f"- - - - - - - - - -")
        else:
            return (f"ERROR! There seems to be a problem with one or more of the attributes."
                    f" Resolve the errors before printing this class!")
