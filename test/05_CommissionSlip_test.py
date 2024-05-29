from property import Property
from commercialProperty import CommercialProperty
from propertyAgent import PropertyAgent
from propertyAgentDirector import PropertyAgentDirector
from commissionSlip import CommissionSlip


def main():
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

    # first agent
    brock = PropertyAgent("Brock", "Pewter Estate", 309872,
                          2004, [pewter_ave, cerulean_cove],
                          [viridian_drive, vermilion_shore, pewter_road])

    # second set of Property instances
    lavender_street = Property("5 Lavender Street", 601372, "15 Years", 2007,
                               "HDB", "800 (sqft)", 750000)

    cerulean_waters = Property("2 Cerulean Waters", 425400, "5 Years", 2019,
                               "Condo", "850 (sqft)", 1500000)

    pallet_estate = Property("9 Pallet Estate", 110925, "33 Years", 1981,
                             "Landed", "1500 (sqft)", 1250000)

    celadon_central = Property("10 Celadon Central", 714905, "3 Years", 2021,
                               "Condo", "600 (sqft)", 975000)

    # second agent
    misty = PropertyAgent("Misty", "Cerulean Network", 290520,
                          2010, [lavender_street],
                          [cerulean_waters, celadon_central, pallet_estate])

    # Property instances for the PropertyAgentDirector

    fuchsia_estate = Property("13 Fuchsia Estate", 809490, "27 Years", 1998,
                              "HDB", "1100 (sqft)", 825000)

    saffron_arc = Property("44 Saffron Arc", 915630, "19 Years", 2015,
                           "Condo", "800 (sqft)", 1300000)

    cinnabar_heights = Property("2 Cinnabar Heights", 110005, "15 Years", 1999,
                                "Landed", "990 (sqft)", 3850000)

    # creating a PropertyAgentDirectory
    giovanni = PropertyAgentDirector("Giovanni", "Rocket Realtors", 107525,
                                     1995, [fuchsia_estate],
                                     [cinnabar_heights, saffron_arc], [brock, misty],
                                     0.05, 0.8)

    misty_commission_slip = CommissionSlip(misty)
    brock_commission_slip = CommissionSlip(brock)
    giovanni_commission_slip = CommissionSlip(giovanni)

    print(misty_commission_slip.get_commission_slip())
    print(brock_commission_slip.get_commission_slip())
    print(giovanni_commission_slip.get_commission_slip())


main()
