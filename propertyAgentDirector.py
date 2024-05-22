from propertyAgent import PropertyAgent


class PropertyAgentDirector(PropertyAgent):

    def __init__(self, name, company, reg_num, year_start, unsold, sold):
        super().__init__(name, company, reg_num, year_start, unsold, sold)
        self.company = company
        self.reg_num = reg_num
        self.year_start = year_start
        self.not_sold = unsold
        self.sold = sold
        self.commission_rate = 0.01
        self.commission_sharing_rate = 0.75
        self.designation = "Director"

    def __str__(self):
        # check to see if commission sharing rate is valid
        if self.designation == "Director":
            if self.commission_sharing_rate < 0.75 or self.commission_sharing_rate > 0.9:
                return "Error, commission sharing rate is invalid. It should be between 0.75 and 0.9"
            else:
                pass
        else:
            pass

        return self.designation
