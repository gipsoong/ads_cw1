from commercial_property import CommercialProperty


def main():
    """Start of program."""
    # silph_co utilizes the correct attributes,
    # expected outcome of the methods returning string + data without any errors
    silph_co = CommercialProperty("1 Silph Co.", 888881, "41 Years", 1983,
                                  "Commercial", "9500 (sqft)",
                                  7500000, "Office")

    # viridian_city_ave uses the wrong attributes on purpose, to test the validation methods,
    # expected outcome of some ERROR messages
    viridian_city_ave = CommercialProperty(321, 1, "5 Years",
                                           1, "HDB", "2150 sqft",
                                           0, "Station")

    print(silph_co.get_address())
    print(silph_co.get_postal_code())
    print(silph_co.get_tenure())
    print(silph_co.get_completion_year())
    print(silph_co.get_property_type())
    print(silph_co.get_commercial_property_type())
    print(silph_co.get_area())
    print(silph_co.get_valuation())
    print(silph_co.get_commission_rate())

    print(silph_co)

    print(viridian_city_ave.get_address())
    print(viridian_city_ave.get_postal_code())
    print(viridian_city_ave.get_tenure())
    print(viridian_city_ave.get_completion_year())
    print(viridian_city_ave.get_property_type())
    print(viridian_city_ave.get_commercial_property_type())
    print(viridian_city_ave.get_area())
    print(viridian_city_ave.get_valuation())
    print(viridian_city_ave.get_commission_rate())

    print(viridian_city_ave)


main()
