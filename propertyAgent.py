class PropertyAgent:

    def __init__(self, name, company, registration_number, year_start, unsold, sold):
        self.name = name
        self.company = company
        self.registration_number = registration_number
        self.year_start = year_start
        self.unsold = unsold
        self.sold = sold
        self.commission_sharing_rate = 0.7

    def get_name(self):
        return (f"----------\n"
                f"NAME: {self.name}")

    def get_company(self):
        return (f"----------\n"
                f"COMPANY: {self.company}")

    def get_registration_number(self):
        return (f"----------\n"
                f"REGISTRATION NUMBER: {self.registration_number}")

    def get_year_start(self):
        return (f"-----------\n"
                f"YEAR STARTED: {self.year_start}")

    def get_properties_unsold(self):
        print(f"----------\n"
              f"UNSOLD PROPERTIES:")

        for i in self.unsold:
            print(f"{i.address} ({i.property_type}) {i.postal_code}, valued at P${i.valuation:,.0f}")

    def get_properties_sold(self):
        print(f"-----------\n"
              f"SOLD PROPERTIES:")

        for i in self.sold:
            print(f"{i.address} ({i.property_type}) {i.postal_code}, sold at P${i.valuation:,.0f}")

    def get_total_sold(self):
        total_sold = 0
        for i in self.sold:
            total_sold += i.valuation

        return total_sold

    def get_commission_sharing_rate(self):
        return (f"----------\n"
                f"COMMISSION SHARING RATE:\n"
                f"{(self.commission_sharing_rate * 10):.0f}%")

    def calculate_gross_commission(self):
        gross_commission = 0
        for i in self.sold:
            gross_commission += (i.valuation * i.commission_rate)

        return gross_commission

    def calculate_net_commission(self):
        gross_commission = self.calculate_gross_commission()
        net_commission = gross_commission * self.commission_sharing_rate
        return net_commission

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
                f" (P${self.calculate_agency_share():,})")

    def __str__(self):
        return (f"----------\n"
                f"Property Agent {self.name}, registration number {self.registration_number}."
                f" Representing {self.company} since {self.year_start}.\n"
                f"Total value of properties sold this year: P${self.get_total_sold():,}\n"
                f"Net commission earned this year: P${self.calculate_net_commission():,}\n"
                f"----------")
