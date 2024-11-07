def get_requirements(): 
    print("Developer: Logan Moecher")
    print("Miles Per Gallon")
    print("\nProgram Requirments:\n"
        + "1. Convert MPG.\n"
        + "2. Must use float data type for user input and calculation.\n"
        + "3. Format and round conversation to two decimal places.\n")


def calculate_miles_per_gallon():
    #initialize variables
    miles = 0.0
    gallons = 0.0
    mpg = 0.0

    # get user data
    print("Input:")
    miles = float(input('Enter miles driven: '))
    # gallons of fuel used
    gallons = float(input('Enter gallons of fuel used: '))

    # calculate miles-per-gallon
    mpg = miles / gallons

    # print output
    # https://docs.python.org/3/library/string.html#format-specification-mini-language
    # https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3

    print("\nOutput:")
    print("{0:,.2f} {1} {2:,.2f} {3} {4:,.2f} {5}".format(miles, "miles driven and", gallons, "gallons used =", mpg, "mpg"))
    