from propertyAgent import PropertyAgent
from propertyAgentDirector import PropertyAgentDirector
from commissionSlip import CommissionSlip


def main():
    """Start of program."""
    # creating agents
    john = PropertyAgent(["1", "2", "3"], ["4", "5", "6"], "NexProp",
                         100901, "2005")

    # creating directors
    director_june = PropertyAgentDirector(["1", "2", "3"], ["4", "5", "6"], "NexProp",
                                          100902, "2005")

    # just printing to see
    print(john)
    print(director_june)

    # creating commission slip for agent
    agent_commission = CommissionSlip(john.sold, john.agent_commission_rate,
                                      john.agent_commission_sharing_rate)

    agent_commission.calculate_commission()


main()  # start program.
