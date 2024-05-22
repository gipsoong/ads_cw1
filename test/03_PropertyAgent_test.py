from propertyAgent import PropertyAgent
from property import Property


def main():
    """Start of program."""
    # creating Property instances to store in PropertyAgent's sold/unsold attributes
    property_1 = Property("1 Duxton Road", 809490, "21 Years", 2003,
                          "HDB", "990 (sqft)", 680000)

    property_2 = Property("1 Duxton Road", 809490, "21 Years", 2003,
                          "HDB", "990 (sqft)", 500000)

    property_3 = Property("1 Duxton Road", 809490, "21 Years", 2003,
                          "HDB", "990 (sqft)", 475000)

    property_4 = Property("1 Duxton Road", 809490, "21 Years", 2003,
                          "HDB", "990 (sqft)", 486500)

    property_5 = Property("1 Duxton Road", 809490, "21 Years", 2003,
                          "HDB", "990 (sqft)", 602000)

    agent_john = PropertyAgent("John", "Huttons", 309872,
                               2004, [property_1, property_3],
                               [property_2, property_4, property_5])

    print(agent_john)


main()
