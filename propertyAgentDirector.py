from propertyAgent import PropertyAgent


class PropertyAgentDirector(PropertyAgent):

    def __init__(self, not_sold, sold, company, reg_num, year_start):
        super().__init__(not_sold, sold, company, reg_num, year_start)
        self.not_sold = not_sold
        self.sold = sold
        self.company = company
        self.reg_num = reg_num
        self.year_start = year_start
        self.commission_from_agents = 0.05
        self.director_comm_sharing = 0.75
