class PropertyAgent:

    def __init__(self, name, company, registration_number, year_start, unsold, sold):
        """Initialise attributes of PropertyAgent class"""
        self.name = name
        self.company = company
        self.registration_number = registration_number
        self.year_start = year_start
        self.unsold = unsold
        self.sold = sold
        self.commission_sharing_rate = 0.7

    def get_name(self):
        if self.check_name:
            return (f"----------\n"
                    f"NAME: {self.name}")
        else:
            return (f"ERROR! Name '{self.name}' is invalid. Ensure that it is"
                    f" a string!")

    def get_company(self):
        if self.check_company():
            return (f"----------\n"
                    f"COMPANY: {self.company}")
        else:
            return (f"ERROR! Company '{self.name}' is invalid. Ensure that it is"
                    f" a string!")

    def get_registration_number(self):
        if self.check_registration_number():
            return (f"----------\n"
                    f"REGISTRATION NUMBER: {self.registration_number}")
        else:
            return (f"ERROR! Registration number '{self.name}' is invalid. Ensure that it is"
                    f" a six digit integer!")

    def get_year_start(self):
        if self.check_year_start():
            return (f"-----------\n"
                    f"YEAR STARTED: {self.year_start}")
        else:
            return (f"ERROR! Start year '{self.year_start}' is invalid. Ensure that it is"
                    f" an integer and a realistic year!")

    def get_properties_unsold(self):
        unsold_string = ""
        for i in self.unsold:
            if i == self.unsold[-1]:
                unsold_string += f"{i.address} ({i.property_type}) {i.postal_code}, valued at P${i.valuation:,.0f}"
            else:
                unsold_string += f"{i.address} ({i.property_type}) {i.postal_code}, valued at P${i.valuation:,.0f}\n"

        if self.check_unsold():
            return (f"----------\n"
                    f"UNSOLD PROPERTIES:\n"
                    f"{unsold_string}")
        else:
            return (f"ERROR! Unsold list contains an error. Ensure that"
                    f" you are passing a property or commercial property!")

    def get_properties_sold(self):
        sold_string = ""
        for i in self.sold:
            if i == self.sold[-1]:
                sold_string += f"{i.address} ({i.property_type}) {i.postal_code}, valued at P${i.valuation:,.0f}"
            else:
                sold_string += f"{i.address} ({i.property_type}) {i.postal_code}, valued at P${i.valuation:,.0f}\n"

        if self.check_sold():
            return (f"----------\n"
                    f"SOLD PROPERTIES:\n"
                    f"{sold_string}")
        else:
            return (f"ERROR! Sold list contains an error. Ensure that"
                    f" you are passing a property or commercial property!")

    def get_total_sold(self):
        """Method to calculate and return the valuation of the total properties sold"""
        total_sold = 0
        for i in self.sold:
            total_sold += i.valuation

        return total_sold

    def get_commission_sharing_rate(self):
        return (f"----------\n"
                f"COMMISSION SHARING RATE:\n"
                f"{(self.commission_sharing_rate * 10):.0f}%")

    def calculate_gross_commission(self):
        """Method to calculate and return the gross commission"""
        gross_commission = 0
        for i in self.sold:
            gross_commission += (i.valuation * i.commission_rate)

        return gross_commission

    def calculate_net_commission(self):
        """Method to calculate and return the net commission"""
        gross_commission = self.calculate_gross_commission()
        net_commission = gross_commission * self.commission_sharing_rate
        return net_commission

    def calculate_agency_share_rate(self):
        agency_cut_rate = 1 - self.commission_sharing_rate
        return agency_cut_rate

    def calculate_agency_share(self):
        gross_commission = self.calculate_gross_commission()
        agency_cut = gross_commission * (1 - self.commission_sharing_rate)
        return agency_cut

    def calculate_commission(self):
        agency_cut_rate = (1 - self.commission_sharing_rate) * 100

        return (f"----------\n"
                f"ANNUAL COMMISSION (NET):\n"
                f"P${(self.calculate_net_commission()):,.2f}\n"
                f"* net commission earned after deduction of {agency_cut_rate:.0f}% agency cut"
                f" (P${self.calculate_agency_share():,.2f})")

    def check_name(self):
        """Method to validate if name is a string"""
        if isinstance(self.name, str):
            return True
        else:
            return False

    def check_company(self):
        """Method to validate if company is a string"""
        if isinstance(self.company, str):
            return True
        else:
            return False

    def check_registration_number(self):
        """Method to validate if registration_number is an integer and six digits"""
        if isinstance(self.registration_number, int) and (99999 < self.registration_number <= 999999):
            return True
        else:
            return False

    def check_year_start(self):
        """Method to validate if year_start is an integer and within a realistic range"""
        if isinstance(self.year_start, int) and (1950 < self.year_start <= 2024):
            return True
        else:
            return False

    def check_unsold(self):
        """Method to check if items in the unsold list are Properties/CommercialProperties.
            There's a level of redundancy as an Error will be thrown even without this method"""
        # variable to counter length of unsold list
        counter = 0
        for i in self.unsold:
            # checking if the list contains any undesired attributes
            if type(i).__name__ == 'Property' or type(i).__name__ == 'CommercialProperty':
                counter += 1

            else:
                counter += 0

        # if counter == length of unsold list, return True
        return counter == len(self.unsold)

    def check_sold(self):
        """Method to check if items in the sold list are Properties/CommercialProperties.
            There's a level of redundancy as an Error will be thrown even without this method"""
        # variable to counter length of unsold list
        counter = 0
        for i in self.sold:
            # checking if the list contains any undesired attributes
            if type(i).__name__ == 'Property' or type(i).__name__ == 'CommercialProperty':
                counter += 1

            else:
                counter += 0

        # if counter == length of sold list, return True
        return counter == len(self.sold)

    def check_all_property_agent(self):
        """Method to run all PropertyAgent checks"""
        if (self.check_name()
                and self.check_company()
                and self.check_registration_number()
                and self.check_year_start()
                and self.check_unsold()
                and self.check_sold()):
            return True

        else:
            return False

    def __str__(self):
        if self.check_all_property_agent():
            return (f"----------\n"
                    f"Property Agent {self.name}, registration number {self.registration_number}."
                    f" Representing {self.company} since {self.year_start}.\n"
                    f"Total value of properties sold this year: P${self.get_total_sold():,}\n"
                    f"Net commission earned this year: P${self.calculate_net_commission():,.0f}\n"
                    f"----------")
        else:
            return (f"ERROR! There seems to be a problem with one or more of the attributes."
                    f" Resolve the errors before printing this class!")
