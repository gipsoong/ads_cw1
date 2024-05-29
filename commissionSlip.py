class CommissionSlip:
    """Initialise the attributes of "CommissionSlip"""

    # CalculateCommission calculates the annual commission earned by an agent/director
    def __init__(self, parameter):
        self.parameter = parameter

    def calculate_agent_commission(self):
        comm_sharing_rate = self.parameter.commission_sharing_rate
        total_commission = 0
        # agency_cut = self.x.calculate_agency_share()
        commission_slip_string = ""

        for i in self.parameter.sold:
            total_commission += (i.valuation * i.commission_rate) * comm_sharing_rate

            commission_slip_string += (f"- {i.address}, transacted at P${i.valuation:,.2f}."
                                       f" Net commission earned ="
                                       f" P${((i.valuation * i.commission_rate) * comm_sharing_rate):,.2f} \n"
                                       f"({i.valuation:,.2f} * {i.commission_rate} * {comm_sharing_rate} ="
                                       f" {((i.valuation * i.commission_rate) * comm_sharing_rate):,.2f})\n"
                                       f"\n")

        return (f"----------\n"
                f"COMMISSION SLIP of Property Agent {self.parameter.name}\n"
                f"{commission_slip_string}"
                f"TOTAL COMMISSION: P${total_commission:,.2f}")

    def calculate_overriding_commission(self):
        agents_total_net_commission = 0

        for i in self.parameter.agents:
            agents_total_net_commission += i.calculate_net_commission()

        total_overriding_commission = agents_total_net_commission * self.parameter.commission_rate_from_agents

        return total_overriding_commission

    def get_overriding_commission_breakdown(self):
        overriding_breakdown = ""
        for i in self.parameter.agents:
            from_agent = i.calculate_net_commission() * self.parameter.commission_rate_from_agents
            overriding_breakdown += (f"- P${from_agent:,.2f} earned from"
                                     f" {i.name}'s commission of P${i.calculate_net_commission():,.2f}\n"
                                     f"\n")

        return overriding_breakdown

    def calculate_director_commission(self):
        total_overriding_commission = self.calculate_overriding_commission()
        comm_sharing_rate = self.parameter.commission_sharing_rate
        total_commission = 0
        # agency_cut = self.x.calculate_agency_share()
        commission_slip_string = ""

        for i in self.parameter.sold:
            total_commission += (i.valuation * i.commission_rate) * comm_sharing_rate

            commission_slip_string += (f"- {i.address}, transacted at P${i.valuation:,.2f}."
                                       f" Net commission earned ="
                                       f" P${((i.valuation * i.commission_rate) * comm_sharing_rate):,.2f} \n"
                                       f"({i.valuation:,.2f} * {i.commission_rate} * {comm_sharing_rate} ="
                                       f" {((i.valuation * i.commission_rate) * comm_sharing_rate):,.2f})\n"
                                       f"\n")

        return (f"----------\n"
                f"COMMISSION SLIP of Property Director {self.parameter.name}\n"
                f"{commission_slip_string}"
                f"TOTAL COMMISSION: P${total_commission:,.2f}\n"
                f"\n"
                f"TOTAL OVERRIDING COMMISSION: P${total_overriding_commission:,.2f}\n"
                f"{self.get_overriding_commission_breakdown()}"
                f"FINAL TOTAL COMMISSION: P${(total_commission + total_overriding_commission):,.2f}")

    def get_commission_slip(self):
        """Simple function to check class name, then calls the corresponding function"""
        if type(self.parameter).__name__ == 'PropertyAgentDirector':
            return self.calculate_director_commission()

        else:
            return self.calculate_agent_commission()
