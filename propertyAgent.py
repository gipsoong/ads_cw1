

class PropertyAgent:
    agent_comm_sharing_rate = 0.7

    def __init__(self, not_sold, sold, company, reg_num, year_start):
        self.not_sold = not_sold
        self.sold = sold
        self.company = company
        self.reg_num = reg_num
        self.year_start = year_start
