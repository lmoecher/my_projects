"""Defines two functions: 

1. get_requirements()
2. calculate_sqft_to_acre()
"""

# number of square feet in an acre (constant)
SQ_FEET_PER_ACRE = 43560


def get_requirements():
    """Accepts 0 args. Displays program requirments."""
    print("Developer: Logan Moecher")
    print("Square feet to Acres")
    print("\nProgram Requirements: \n"
        + "1. Research: number of square feet to acre of land.\n"
        + "2. Must use float data type for user input and calculation.\n"
        + "3. Format and round conversation to two decimal places.\n")


def calculate_sqft_to_acre():
    """Accepts 0 args. Calculate square feet to acres, and print output."""
    # variables hold (land) tract size and number of acres
    tract_size = 0.0
    acres = 0.0

    # get square feet in track
    print("Input:")
    tract_size = float(input('Enter square feet: '))
    # calculate acreage
    acres = tract_size / SQ_FEET_PER_ACRE

    # print number of acres
    # https://docs.python.org/3/library/string.html#format-specification-mini-language
    # https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3

    print("\nOutput:")
    print("{0:,.2f} {1} {2:,.2f} {3}".format(tract_size, "square feet =", acres, "acres"))