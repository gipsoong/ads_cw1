from propertyAgent import PropertyAgent


class PropertyAgentDirector(PropertyAgent):

    def __init__(self, name, company, registration_number, year_start, unsold, sold, agents,
                 commission_rate_from_agents, commission_sharing_rate):
        super().__init__(name, company, registration_number, year_start, unsold, sold)
        self.company = company
        self.registration_number = registration_number
        self.year_start = year_start
        self.not_sold = unsold
        self.sold = sold
        self.agents = agents
        self.commission_rate_from_agents = commission_rate_from_agents
        self.commission_sharing_rate = commission_sharing_rate

    def get_commission_sharing_rate(self):
        # check to see if commission sharing rate is valid
        if self.commission_sharing_rate < 0.75 or self.commission_sharing_rate > 0.9:
            return (f"Error, input of {self.commission_sharing_rate} is invalid."
                    f"The commission sharing rate should be between 0.75 and 0.9")
        else:
            return (f"----------\n"
                    f"COMMISSION SHARING RATE:\n"
                    f"{(self.commission_sharing_rate * 10):.0f}%")

    def get_agents(self):
        print(f"----------\n"
              f"AGENTS UNDER {self.name}:")

        for i in self.agents:
            print(f"{i.name}, {i.registration_number}")

    def get_commission_rate_from_agents(self):
        print(f"----------\n"
              f"COMMISSION RATE FROM AGENTS:\n"
              f"{(self.commission_rate_from_agents * 100):.0f}%")

    def get_commission_from_agents(self):
        agents_total_commission = 0
        print(f"----------\n"
              f"TOTAL COMMISSION FROM AGENTS")
        for i in self.agents:
            for x in i.sold:
                agents_total_commission += (x.valuation * x.commission_rate) * i.commission_sharing_rate

        total_commission_from_agents = agents_total_commission * self.commission_rate_from_agents

        print(f"P${total_commission_from_agents:,.2f}")

    def calculate_commission_from_agents(self):
        agents_total_commission = 0
        for i in self.agents:
            for x in i.sold:
                agents_total_commission += (x.valuation * x.commission_rate) * i.commission_sharing_rate

        total_commission_from_agents = agents_total_commission * self.commission_rate_from_agents

        return total_commission_from_agents

    def calculate_director_total_commission(self):
        net_commission = (self.get_total_sold() * 0.01) * self.commission_sharing_rate
        total_net_commission = net_commission + self.calculate_commission_from_agents()

        return total_net_commission

    def __str__(self):
        return (f"----------\n"
                f"Property Director {self.name}, registration number {self.registration_number}."
                f" Representing {self.company} since {self.year_start}.\n"
                f"Total value of properties sold this year: P${self.get_total_sold():,.2f}\n"
                f"Total net commission earned this year: P${self.calculate_director_total_commission():,.2f}\n"
                f"* net commission of P${self.calculate_net_commission():,.2f} from property sales,"
                f" in addition to P${self.calculate_commission_from_agents():,.2f} earned from agents' commission.\n"
                f"----------")
