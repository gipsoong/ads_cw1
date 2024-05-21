class CommissionSlip:
    """Initialise the attributes of "CommissionSlip"""

    # CalculateCommission calculates the annual commission earned by an agent/director
    def __init__(self, total_sold, commission_rate, commission_sharing_rate):
        self.total_sold = total_sold
        self.commission_rate = commission_rate
        self.commission_sharing_rate = commission_sharing_rate

    def calculate_commission(self):

        amount_sold = 0
        for i in self.total_sold:
            amount_sold += i

        net_commission = (amount_sold * self.commission_rate) * self.commission_sharing_rate

        print(f"Commission earned for the year is ${net_commission}")
