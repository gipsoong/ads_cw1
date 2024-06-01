from property import Property
from commercial_property import CommercialProperty
from property_agent import PropertyAgent
from property_agent_director import PropertyAgentDirector
from commission_slip import CommissionSlip


def main():
    """Start of program."""
    # creating Property instances (15)
    # 5 unsold properties and 3 sold properties per agent
    # there will be some overlap, it is intended as there would be no real benefit to creating 30 unique properties
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

    lavender_street = Property("5 Lavender Street", 601372, "15 Years", 2007,
                               "HDB", "800 (sqft)", 750000)

    cerulean_waters = Property("2 Cerulean Waters", 425400, "5 Years", 2019,
                               "Condo", "850 (sqft)", 1500000)

    pallet_estate = Property("9 Pallet Estate", 110925, "33 Years", 1981,
                             "Landed", "1500 (sqft)", 1250000)

    celadon_central = CommercialProperty("10 Celadon Central", 714905, "3 Years",
                                         2021, "Commercial", "6000 (sqft)",
                                         7500000, "Factory")

    indigo_plateau_road = CommercialProperty("5 Indigo Plateau Road", 504941, "11 Years",
                                             2007, "Commercial", "3000 (sqft)",
                                             3500000, "Office")

    viridian_grove = Property("12 Viridian Grove", 425401, "1 Year", 2023,
                              "HDB", "800 (sqft)", 1500000)

    lavender_heights = Property("4 Lavender Heights", 113925, "34 Years", 1990,
                                "Condo", "1500 (sqft)", 1900000)

    fuchsia_estate = Property("13 Fuchsia Estate", 809490, "27 Years", 1998,
                              "HDB", "1100 (sqft)", 825000)

    saffron_arc = Property("44 Saffron Arc", 915630, "19 Years", 2015,
                           "Condo", "800 (sqft)", 1300000)

    cinnabar_heights = Property("2 Cinnabar Heights", 110005, "15 Years", 1999,
                                "Landed", "990 (sqft)", 3850000)

    # first agent under Giovanni
    james = PropertyAgent("James", "Rocket Realtors", 309872,
                          2004, [pewter_ave, cerulean_cove, cinnabar_heights, saffron_arc, fuchsia_estate],
                          [viridian_drive, vermilion_shore, pewter_road])

    # second agent under Giovanni
    jessie = PropertyAgent("Jessie", "Rocket Realtors", 290520,
                           2010, [lavender_street, lavender_heights,
                                  indigo_plateau_road, viridian_grove, viridian_drive],
                           [cerulean_waters, fuchsia_estate, pallet_estate])

    # third agent under Giovanni
    meowth = PropertyAgent("Meowth", "Rocket Realtors", 999992,
                           2001, [indigo_plateau_road, cerulean_cove, cerulean_waters,
                                  viridian_drive, cinnabar_heights],
                           [lavender_heights, viridian_grove, fuchsia_estate])

    # first property agent director
    giovanni = PropertyAgentDirector("Giovanni", "Rocket Realtors", 107525,
                                     1995, [cinnabar_heights],
                                     [celadon_central, indigo_plateau_road], [james, jessie, meowth],
                                     0.05, 0.8)

    # first agent under Agatha
    lorelei = PropertyAgent("Lorelei", "Elite Four", 399872,
                            2004, [fuchsia_estate, celadon_central, pewter_ave,
                                   pallet_estate, cinnabar_heights],
                            [viridian_drive, vermilion_shore, pewter_road])

    # second agent under Agatha
    lance = PropertyAgent("Lance", "Elite Four", 293526,
                          2010, [celadon_central, cinnabar_heights, pewter_ave,
                                 viridian_drive, viridian_grove],
                          [cerulean_waters, pallet_estate, fuchsia_estate])

    # third agent under Agatha
    bruno = PropertyAgent("Bruno", "Elite Four", 999991,
                          2001, [lavender_street, cerulean_waters,
                                 cerulean_cove, pewter_road, pewter_ave],
                          [lavender_heights, viridian_grove, pallet_estate])

    # second property agent director
    agatha = PropertyAgentDirector("Agatha", "Elite Four", 107524,
                                   1995, [fuchsia_estate],
                                   [cinnabar_heights, saffron_arc], [james, jessie, meowth],
                                   0.2, 0.5)

    jessie_commission_slip = CommissionSlip(jessie)
    james_commission_slip = CommissionSlip(james)
    meowth_commission_slip = CommissionSlip(meowth)
    giovanni_commission_slip = CommissionSlip(giovanni)

    lorelei_commission_slip = CommissionSlip(lorelei)
    lance_commission_slip = CommissionSlip(lance)
    bruno_commission_slip = CommissionSlip(bruno)
    agatha_commission_slip = CommissionSlip(agatha)

    # these will result in the expected output as the attributes are all correct
    print(jessie_commission_slip)
    print(james_commission_slip)
    print(meowth_commission_slip)
    print(giovanni_commission_slip)

    # errors will be thrown as one or more of the attributes are invalid (in this case it is
    # commission_rate_from_agents)
    print(lorelei_commission_slip)
    print(lance_commission_slip)
    print(bruno_commission_slip)
    print(agatha_commission_slip)


main()
