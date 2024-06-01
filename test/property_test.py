


def main():
    """Start of program."""
    # pallet_town_road utilizes the correct attributes,
    # expected outcome of the methods returning string + data without any errors
    pallet_town_road = Property("2 Pallet Town Road", 809490, "13 Years", 1996,
                                "HDB", "990 (sqft)", 680000)

    # vermilion_shore uses the wrong attributes on purpose, to test the validation methods,
    # expected outcome of some ERROR messages
    vermilion_shore = Property(12345, 12345, "21 Years", 3001,
                               "Office", "700 (sqft)", "wrong input")

    print(pallet_town_road.get_address())
    print(pallet_town_road.get_postal_code())
    print(pallet_town_road.get_tenure())
    print(pallet_town_road.get_completion_year())
    print(pallet_town_road.get_property_type())
    print(pallet_town_road.get_area())
    print(pallet_town_road.get_valuation())
    print(pallet_town_road.get_commission_rate())

    print(pallet_town_road)

    print(vermilion_shore.get_address())
    print(vermilion_shore.get_postal_code())
    print(vermilion_shore.get_tenure())
    print(vermilion_shore.get_completion_year())
    print(vermilion_shore.get_property_type())
    print(vermilion_shore.get_area())
    print(vermilion_shore.get_valuation())
    print(vermilion_shore.get_commission_rate())

    print(vermilion_shore)


main()
