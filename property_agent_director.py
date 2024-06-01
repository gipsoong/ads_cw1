from property_agent import PropertyAgent


class PropertyAgentDirector(PropertyAgent):

    def __init__(self, name, company, registration_number, year_start, unsold, sold, agents,
                 overriding_rate, commission_sharing_rate):
        super().__init__(name, company, registration_number, year_start, unsold, sold)
        """Initialise attributes of PropertyAgentDirector class"""
        self.company = company
        self.registration_number = registration_number
        self.year_start = year_start
        self.not_sold = unsold
        self.sold = sold
        self.agents = agents
        self.overriding_rate = overriding_rate
        self.commission_sharing_rate = commission_sharing_rate

    def get_agents(self):
        agents_string = ""

        for i in self.agents:
            if i == self.agents[-1]:
                agents_string += f"{i.name}, {i.registration_number}"
            else:
                agents_string += f"{i.name}, {i.registration_number}\n"

        return (f"----------\n"
                f"AGENTS UNDER {self.name}:\n"
                f"{agents_string}")

    def get_overriding_rate(self):
        if self.check_overriding_rate():
            return (f"----------\n"
                    f"COMMISSION RATE FROM AGENTS:\n"
                    f"{(self.overriding_rate * 100):.0f}%")
        else:
            return (f"Error, input of {self.overriding_rate} is invalid. "
                    f"The overriding rate should be a float between 0.05 and 0.15")

    def get_commission_sharing_rate(self):
        if self.check_commission_sharing_rate():
            return (f"----------\n"
                    f"COMMISSION SHARING RATE:\n"
                    f"{(self.commission_sharing_rate * 10):.0f}%")
        else:
            return (f"Error, input of {self.commission_sharing_rate} is invalid. "
                    f"The commission sharing rate should be a float between 0.75 and 0.9")

    def get_commission_from_agents(self):
        agents_total_commission = 0
        for i in self.agents:
            for x in i.sold:
                agents_total_commission += (x.valuation * x.commission_rate) * i.commission_sharing_rate

        total_commission_from_agents = agents_total_commission * self.overriding_rate

        return (f"----------\n"
                f"TOTAL COMMISSION FROM AGENTS\n"
                f"P${total_commission_from_agents:,.2f}")

    def calculate_commission_from_agents(self):
        """Method to calculate and return the total net commission earned from agents under the director"""
        agents_total_commission = 0
        for i in self.agents:
            for x in i.sold:
                agents_total_commission += (x.valuation * x.commission_rate) * i.commission_sharing_rate

        total_commission_from_agents = agents_total_commission * self.overriding_rate

        return total_commission_from_agents

    def calculate_director_total_commission(self):
        """Method to calculate and return the net commission"""
        net_commission = (self.get_total_sold() * 0.01) * self.commission_sharing_rate
        total_net_commission = net_commission + self.calculate_commission_from_agents()

        return total_net_commission

    def check_commission_sharing_rate(self):
        """Method to validate if commission_sharing_rate is a float and within the specified range"""
        if isinstance(self.commission_sharing_rate, float) and 0.75 < self.commission_sharing_rate < 0.9:
            return True
        else:
            return False

    def check_overriding_rate(self):
        """Method to validate if commission_rate_from_agents is a float and within the specified range"""
        if isinstance(self.overriding_rate, float) and 0.05 <= self.overriding_rate <= 0.15:
            return True
        else:
            return False

    def check_all_property_agent_director(self):
        """Method to run all PropertyAgentDirector checks"""
        if (self.check_name()
                and self.check_company()
                and self.check_registration_number()
                and self.check_year_start()
                and self.check_unsold()
                and self.check_sold()
                and self.check_commission_sharing_rate()
                and self.check_overriding_rate()):
            return True

        else:
            return False

    def __str__(self):
        if self.check_all_property_agent_director():
            return (f"----------\n"
                    f"Property Director {self.name}, registration number {self.registration_number}."
                    f" Representing {self.company} since {self.year_start}.\n"
                    f"Total value of properties sold this year: P${self.get_total_sold():,.2f}\n"
                    f"Total net commission earned this year: P${self.calculate_director_total_commission():,.2f}\n"
                    f"* net commission of P${self.calculate_net_commission():,.2f} from property sales,"
                    f" in addition to P${self.calculate_commission_from_agents():,.2f}"
                    f" earned from agents' commission.\n"
                    f"----------")
        else:
            return (f"ERROR! There seems to be a problem with one or more of the attributes."
                    f" Resolve the errors before printing this class!")
