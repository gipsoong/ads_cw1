from property import Property
from property_agent import PropertyAgent
from property_agent_director import PropertyAgentDirector


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

    # giovanni utilizes the correct attributes,
    # expected outcome of the methods returning string + data without any errors
    giovanni = PropertyAgentDirector("Giovanni", "Rocket Realtors", 107525,
                                     1995, [fuchsia_estate],
                                     [cinnabar_heights, saffron_arc], [brock, misty],
                                     0.05, 0.8)

    # blaine uses the wrong attributes on purpose, to test the validation methods,
    # expected outcome of some ERROR messages
    blaine = PropertyAgentDirector(123, 123, "Cinnabar",
                                   "1950", [fuchsia_estate],
                                   [cinnabar_heights, saffron_arc], [brock, misty],
                                   0.5, 0.8)

    print(giovanni.get_name())
    print(giovanni.get_company())
    print(giovanni.get_registration_number())
    print(giovanni.get_year_start())
    print(giovanni.get_properties_unsold())
    print(giovanni.get_properties_sold())
    print(giovanni.get_commission_sharing_rate())
    print(giovanni.get_agents())
    print(giovanni.get_overriding_rate())
    print(giovanni.get_commission_from_agents())
    print(giovanni.calculate_commission())

    print(giovanni)

    print(blaine.get_name())
    print(blaine.get_company())
    print(blaine.get_registration_number())
    print(blaine.get_year_start())
    print(blaine.get_properties_unsold())
    print(blaine.get_properties_sold())
    print(blaine.get_commission_sharing_rate())
    print(blaine.get_agents())
    print(blaine.get_overriding_rate())
    print(blaine.get_commission_from_agents())
    print(blaine.calculate_commission())

    print(blaine)


main()
