def get_requirements():
    print("Developer: Logan Moecher")
    print("Temperature Conversion Program\n")
    print("\nProgram Requirments:\n"
        + "1. Program converts user-entered temperatures into Fahrenheit or Celsius scales.\n"
        + "2. Program continues to prompt for user entry until no longer request.\n"
        + "3. Note: upper or lower case letters permitted. though, incorrect entries are not permitted.\n"
        + "4. Note: Program does not validate numeric data (optional requirement).\n")

def temperature_conversion():
    # initialize variables
    temperature = 0.0
    choice = '' # initialize to space character
    type = ''   # initialize to space character

    # IPO: Input > Process > Output
    # # get user data
    print("Input: ")

    choice = input("Do you want to convert a temperature (y or n)? ").lower()

    # Porcess and Output
    print("\nOutput: ")

    while (choice[0] == 'y'):
        type = input("Fahrenheit to Celsius? Type \"f\", or Celsius to Fahrenheit? Type \"c\": ").lower()

        if type[0] == 'f':
            temperature = float(input("Enter temperature in Fahrenheit: "))
            temperature = ((temperature - 32)*5)/9
            print("Temperature in Celsius = " + str(temperature))
            choice = input("\nDo you want to convert another temperature (y or n)? ").lower()

        elif type[0] == 'c':
            temperature = float(input("Enter temperature in Celsius: "))
            temperature = (temperature * 9/5)+ 32
            print("Temperature in Fahrenheit = " + str(temperature))
            choice = input("\nDo you want to convert another temperature (y or n)? ").lower()

        else:
            print("Incorrect entry. Please try again.")
            choice = input("\nDo you want to convert a temperature (y or n)? ").lower()

    print("\nThank you for using our Temperature Conversion Program!")