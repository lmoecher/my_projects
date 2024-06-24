def get_requirments(): 
    print("Developer: Logan Moecher")
    print("IT/ICT Student Percentage")
    print("\nProgram Requirments:\n"
        + "1. Find number of IT/ICT students in class.\n"
        + "2. Calculate IT/ICT Student Percentage.\n"
        + "3. Must use float data type (to facilitate right-alignment).\n"
        + "4. Format, right-align numbers, and round two decimal places.\n")


def calculate_it_ict_student_percentage():
    # initialize variables
    it = 0 
    ict = 0
    total_students = 0
    percent_it = 0.0
    percent_ict = 0.0

    # IPO" Input > Process > Output
    # get user data
    print("Input: ")
    it = int(input("Enter number of IT students: "))
    ict = int(input("Enter number of ICT students: "))

    # Process:
    # calculate total number of students
    total_students = it + ict

    # calculate percentage of IT students
    # (Python 3: integer division implicity casts to float)
    percent_it = it / total_students

    # calculate percentage of ICT students
    # (Python 3: integer division implicity casts to float)
    percent_ict = ict / total_students

    # print output
    # https://docs.python.org/3/library/string.html#format-specification-mini-language
    # https://docs.python.org/3/library/string.html#string-formatting
    # https://www.python-course.eu/python3_formatted_output.php
    # https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3

    # Note: % automatically multiplies by 100 followed by %
    print("\nOutput:")
    print("{0:17} {1:>5.2f}".format("Total Students:", total_students))
    print("{0:17} {1:>.2%}".format("IT Students:", percent_it))
    print("{0:17} {1:>.2%}".format("ICT Students:", percent_ict))
