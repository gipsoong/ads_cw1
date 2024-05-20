from propertyAgent import PropertyAgent

def main():
    """Start of program."""
    agent_john = PropertyAgent(["1", "2", "3"], ["4", "5", "6"], "NexProp",
                               100901, "2005")

    print(agent_john)
    print(agent_john.not_sold)
    print(agent_john.agent_commission_rate)
    print(agent_john.agent_commission_sharing_rate)

main() # start program.