class PropertyAgent:

    def __init__(self, name, company, reg_num, year_start, not_sold, sold):
        self.name = name
        self.company = company
        self.reg_num = reg_num
        self.year_start = year_start
        self.not_sold = not_sold
        self.sold = sold
        self.commission_rate = 0.01
        self.agent_commission_sharing_rate = 0.7

    def __str__(self):
        # calculating the total value of properties sold
        total_sold = 0
        i = 0
        while i < len(self.sold):
            total_sold += self.sold[i].valuation
            i += 1

        # calculating the net commission
        net_commission = (total_sold * self.commission_rate) * self.agent_commission_sharing_rate

        return (f"---------- \n"
                f"{self.name}, registration number {self.reg_num}."
                f" Representing {self.company} since {self.year_start}.\n"
                f"Total value of properties sold this year: S${total_sold}\n"
                f"Net commission earned this year: S${net_commission}\n"
                f"----------")
