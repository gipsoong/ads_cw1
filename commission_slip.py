class CommissionSlip:
    def __init__(self, arg):
        """Initialise attribute of PropertyAgentDirector class"""
        self.arg = arg

    def calculate_agent_commission(self):
        comm_sharing_rate = self.arg.commission_sharing_rate
        total_commission = 0    # initialize total_commission as 0, for loop will add to this variable
        commission_slip_string = ""

        for i in self.arg.sold:
            total_commission += (i.valuation * i.commission_rate) * comm_sharing_rate

            commission_slip_string += (f"- {i.address}, transacted at P${i.valuation:,.2f}."
                                       f" Net commission earned ="
                                       f" P${((i.valuation * i.commission_rate) * comm_sharing_rate):,.2f} \n"
                                       f"({i.valuation:,.2f} * {i.commission_rate} * {comm_sharing_rate} ="
                                       f" {((i.valuation * i.commission_rate) * comm_sharing_rate):,.2f})\n"
                                       f"\n")

        return (f"----------\n"
                f"COMMISSION SLIP of Property Agent {self.arg.name}\n"
                f"{commission_slip_string}"
                f"TOTAL COMMISSION: P${total_commission:,.2f}")

    def calculate_overriding_commission(self):
        """Method to calculate and return the total overriding commission"""
        agents_total_net_commission = 0

        for i in self.arg.agents:
            agents_total_net_commission += i.calculate_net_commission()

        total_overriding_commission = agents_total_net_commission * self.arg.overriding_rate

        return total_overriding_commission

    def calculate_overriding_commission_breakdown(self):
        """Method to calculate and return the breakdown of the total overriding commission"""
        overriding_breakdown = ""
        for i in self.arg.agents:
            from_agent = i.calculate_net_commission() * self.arg.overriding_rate
            overriding_breakdown += (f"- P${from_agent:,.2f} earned from"
                                     f" overriding {i.name}'s commission of P${i.calculate_net_commission():,.2f}\n"
                                     f"({self.arg.overriding_rate} * {i.calculate_net_commission():,.2f} = "
                                     f"{from_agent:,.2f})\n"
                                     f"\n")

        return overriding_breakdown

    def calculate_director_commission(self):
        total_overriding_commission = self.calculate_overriding_commission()
        comm_sharing_rate = self.arg.commission_sharing_rate
        total_commission = 0    # initialize total_commission as 0, for loop will add to this variable
        commission_slip_string = ""

        for i in self.arg.sold:
            total_commission += (i.valuation * i.commission_rate) * comm_sharing_rate

            commission_slip_string += (f"- {i.address}, transacted at P${i.valuation:,.2f}."
                                       f" Net commission earned ="
                                       f" P${((i.valuation * i.commission_rate) * comm_sharing_rate):,.2f} \n"
                                       f"({i.valuation:,.2f} * {i.commission_rate} * {comm_sharing_rate} ="
                                       f" {((i.valuation * i.commission_rate) * comm_sharing_rate):,.2f})\n"
                                       f"\n")

        return (f"----------\n"
                f"COMMISSION SLIP of Property Director {self.arg.name}\n"
                f"{commission_slip_string}"
                f"TOTAL COMMISSION (SELF): P${total_commission:,.2f}\n"
                f"\n"
                f"TOTAL OVERRIDING COMMISSION: P${total_overriding_commission:,.2f}\n"
                f"{self.calculate_overriding_commission_breakdown()}"
                f"FINAL TOTAL COMMISSION: P${(total_commission + total_overriding_commission):,.2f}")

    def __str__(self):
        """Method to check class name and check for any invalid attributes,
                 then calls the corresponding function if there are no errors"""
        if type(self.arg).__name__ == 'PropertyAgentDirector' and self.arg.check_all_property_agent_director():
            return self.calculate_director_commission()

        elif type(self.arg).__name__ == 'PropertyAgent' and self.arg.check_all_property_agent():
            return self.calculate_agent_commission()

        # else, throws an error if any of the above statements return False
        else:
            return (f"----------\n"
                    f"ERROR! There seems to be a problem with {self.arg.name}."
                    f" Make sure the attributes are correct before calling this method!")
