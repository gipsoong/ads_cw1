class CommissionSlip:
    """Initialise the attributes of "CommissionSlip"""

    # CalculateCommission calculates the annual commission earned by an agent/director
    def __init__(self, x):
        self.x = x

    def calculate_agent_commission(self):
        comm_sharing_rate = self.x.commission_sharing_rate
        total_commission = 0
        print(f"----------\n"
              f"COMMISSION SLIP of Property Agent {self.x.name}:")
        for i in self.x.sold:
            total_commission += (i.valuation * i.commission_rate) * comm_sharing_rate

            print(f"- {i.address}, transacted at P${i.valuation:,.2f}."
                  f" Net commission earned = P${((i.valuation * i.commission_rate) * comm_sharing_rate):,.2f}\n"
                  f"({i.valuation:,.2f} * {i.commission_rate} * {comm_sharing_rate} ="
                  f" {((i.valuation * i.commission_rate) * comm_sharing_rate):,.2f})")

        print(f"TOTAL COMMISSION: P${total_commission:,.2f}")

    def calculate_director_commission(self):
        comm_sharing_rate = self.x.commission_sharing_rate
        print(f"----------\n"
              f"COMMISSION SLIP of Property Director {self.x.name}:")
        for i in self.x.sold:
            print(f"- {i.address}, transacted at P${i.valuation:,.2f}."
                  f" Net commission earned = P${((i.valuation * i.commission_rate) * comm_sharing_rate):,.2f}\n"
                  f"({i.valuation:,.2f} * {i.commission_rate} * {comm_sharing_rate} ="
                  f" {((i.valuation * i.commission_rate) * comm_sharing_rate):,.2f})")

    def get_commission_slip(self):
        """Simple function to check class name, then calls the corresponding function"""
        if type(self.x).__name__ == 'PropertyAgentDirector':
            return self.calculate_director_commission()

        else:
            self.calculate_agent_commission()
