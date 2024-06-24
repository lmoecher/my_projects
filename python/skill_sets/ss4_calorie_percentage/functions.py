def get_requirements():
    print("Calorie Percentage")
    print("\nProgram Requirements:\n"
        +"1. Find calories per grams of fat , carbs, and protein.\n"
        +"2. Calculate percentages.\n"
        +"3. Must use float data types.\n"
        +"4. Format, right-align numbers, and round to the two decimal places.")

def calculate(fat, carbs, protein):
    fat_cal = fat * 9
    carb_cal = carbs * 4
    protein_cal = protein * 4
    return fat_cal, carb_cal, protein_cal

def main():
    print()
    print("Input: ")
    tot_fat = float(input('Enter total fat grams: '))
    tot_carbs = float(input('Enter total carb grams: '))
    tot_prot = float(input('Enter total protein grams: '))
    f, c, p = calculate(tot_fat, tot_carbs, tot_prot)
    total = f + c + p
    fat_perc = f / total
    carb_perc = c / total
    prot_perc = p / total
    print("\nOutput: ")
    print('{0}{1:>15}{2:>15}'.format('Type', 'Calories', 'Percentage'))
    print('{0}{1:>15.2f}{2:>15.2%}'.format('Fat', f, fat_perc))
    print('{0}{1:>13.2f}{2:>15.2%}'.format('Carbs', c, carb_perc))
    print('{0}{1:>11.2f}{2:>15.2%}'.format('Protein', p, prot_perc))
get_requirements()
main()