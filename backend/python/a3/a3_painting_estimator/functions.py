def get_requirements():
    print()
print("Developer: Logan Moecher")
print("Painting Estimator")
print("\nProgram Requirements:\n"
        + "1. Calculate home interior paint cost (w/o primer).\n"
        + "2. Must use float data types.\n"
        + "3. Must use SQFT_PER_GALLON constant (350).\n"
        + "4. Must use iteration structure (aka loop).\n"
        + "5. Format. right align numbers, and round to two decimal places.\n"
        + "6. Create at least five functions that are called by the program:\n"
            + "\ta. main(): calls two other functions: get_requirements() and estimate_painting_cost()\n"
            + "\tb. get_requirements(): displays the program requirements.\n"
            + "\tc. estimate_painting_cost(): calculates interior home painting, and print functions.\n"
            + "\td. print_painting_estimate(): displays painting costs.\n"
            + "\te. print_painting_percentage(): displays painting costs percentages.\n")

SQFT_PER_GALLON = 350.00

def estimate_painting_cost(inter, ppg, sq_rate):
    number_of_gallons = inter / SQFT_PER_GALLON
    paint_cost = number_of_gallons * ppg
    tot_labor = sq_rate * inter
    total_fee = tot_labor + paint_cost
    
    return number_of_gallons, paint_cost, tot_labor, total_fee

def print_painting_estimate(a, b, e):
    print('Number of gallons:{0:>13,.2f}'.format(a))
    print('Paint per gallon:{0:>5}{1:>9,.2f}'.format('$',e))
    print('Labor per Sqft:{0:>7}{1:>9,.2f}'.format('$',b))
    
def print_painting_percentage(pc, labor, total):
    paint_percent = pc / total
    labor_percent = labor / total
    total_percent = total / total
    print('Cost\t\tAmount\t\tPercentage')
    print('Paint:\t${0:>15,.2f}{1:>15.2%}'.format(pc, paint_percent))
    print('Labor:\t${0:>15,.2f}{1:>15.2%}'.format(labor, labor_percent))
    print('Total:\t${0:>15,.2f}{1:>15.2%}'.format(total, total_percent))

def main():
    repeat = 'y'
    while repeat.lower() =='y':
        print("Input: ")
        total_interior = float(input('Enter total interior sq ft: '))
        ppg_paint = float(input('Enter price per gallon of paint: '))
        paint_hr_rate = float(input('Enter hourly painting rate per sq ft: '))
        print()

        if repeat.lower() == 'y':
            n, p, tl, tt = estimate_painting_cost(total_interior, ppg_paint, paint_hr_rate)
            print("Output: ")
            print('Item\t\t\tAmount')
            print('Total Sqft:{0:>20,.2f}'.format(total_interior))
            print('Sqft per Gallon:{0:>15,.2f}'.format(SQFT_PER_GALLON))
            print_painting_estimate(n, paint_hr_rate, ppg_paint)
            print()
            print_painting_percentage(p, tl, tt)
            repeat = input('would you like to repeat (y/n): ')
            print()
        else:
            break
    print("Thank you for using our Painting Estimator!")


if __name__ == "__main__":
    pass