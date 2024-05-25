from commercialProperty import CommercialProperty


def main():
    """Start of program."""
    viridian = CommercialProperty("10th Viridian City Avenue", 9401488, "5 years",
                                  2001, "Commercial", "2150 sqft", 1250000000,
                                  "error")

    print(viridian.get_address())
    print(viridian.get_postal_code())
    print(viridian.get_tenure())
    print(viridian.get_completion_year())
    print(viridian.get_property_type())
    # get_commercial_property_type calls class method check_commercial_property_type to check if the input is valid
    print(viridian.get_commercial_property_type())
    print(viridian.get_area())
    print(viridian.get_valuation())
    print(viridian.get_commission_rate())

    print(viridian)


main()
