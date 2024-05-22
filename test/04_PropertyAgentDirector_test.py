from property import Property
from propertyAgentDirector import PropertyAgentDirector


def main():
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

    janice = PropertyAgentDirector("John", "Huttons", 309872,
                                   2004, [property_1, property_3],
                                   [property_2, property_4, property_5])

    print(janice)


main()
