class CommissionSlip:
    """Initialise the attributes of "CommissionSlip"""

    # CalculateCommission calculates the annual commission earned by an agent/director
    def __init__(self, total_sold, commission_rate, commission_sharing_rate):
        self.total_sold = total_sold
        self.commission_rate = commission_rate
        self.commission_sharing_rate = commission_sharing_rate

    def calculate_commission(self):
        print(f"Total sold {self.total_sold}, Commission Rate {self.commission_rate}"
              f" and Commission Sharing Rate {self.commission_sharing_rate}")
