from property import Property
from propertyAgent import PropertyAgent


def main():
    """Start of program."""
    # creating Property instances to store in PropertyAgent's sold/unsold attributes
    pewter_ave = Property("43 Pewter Avenue", 809490, "21 Years", 2003,
                          "HDB", "990 (sqft)", 450000)

    viridian_drive = Property("19 Viridian Drive", 809490, "21 Years", 2003,
                              "Landed", "1500 (sqft)", 1500000)

    cerulean_cove = Property("3 Cerulean Cove", 809490, "21 Years", 2003,
                             "Landed", "1700 (sqft)", 2500000)

    vermilion_shore = Property("8 Vermilion Shore", 809490, "21 Years", 2003,
                               "Condo", "700 (sqft)", 900000)

    pewter_road = Property("21 Pewter Road", 809490, "21 Years", 2021,
                           "Condo", "400 (sqft)", 850000)

    brock = PropertyAgent("Brock", "Pewter Estate", 309872,
                          2004, [pewter_ave, cerulean_cove],
                          [viridian_drive, vermilion_shore, pewter_road])

    print(brock.get_name())
    print(brock.get_company())
    print(brock.get_registration_number())
    print(brock.get_year_start())
    print(brock.get_properties_unsold())
    print(brock.get_properties_sold())
    print(brock.get_commission_sharing_rate())
    print(brock.calculate_commission())

    print(brock)


main()
