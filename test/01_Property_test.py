from property import Property


def main():
    """Start of program."""
    pallet_town = Property("2 Pallet Town Road", 809490, "13 Years", 1996,
                          "HDB", "990 (sqft)", 680000)

    print(pallet_town.get_address())
    print(pallet_town.get_postal_code())
    print(pallet_town.get_tenure())
    print(pallet_town.get_completion_year())
    print(pallet_town.get_property_type())
    print(pallet_town.get_area())
    print(pallet_town.get_valuation())
    print(pallet_town.get_commission_rate())

    print(pallet_town)


main()
