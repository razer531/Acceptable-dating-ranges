import os
import matplotlib.pyplot as plt
## some comment - 2223232

def centroid_coordinates(x1, y1, x2, y2, x3, y3):
     return (x1+x2+x3)/3, (y1+y2+y3)/3

def average(lst):
    return sum(lst) / len(lst)

def print_colored(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def clear_screen():
        os.system('clear' if os.name == 'posix' else 'cls')

def calculate_minimum_age(guy_age):
        minimum_age = guy_age / 2 + 7
        return int(minimum_age)

def calculate_maximum_age(guy_age):
        maximum_age = (guy_age - 7) * 2
        return int(maximum_age)

def print_age_table(start, end):
    print("GUY AGE | MIN GIRL AGE | MAX GIRL AGE")
    print("-" * 37)  # Adjusted length to match the headers
    
    guy_ages = []
    min_girl_ages = []
    max_girl_ages = []

    for guy_age in range(start, end + 1):
        min_girl_age = calculate_minimum_age(guy_age)
        max_girl_age = calculate_maximum_age(guy_age)

        # Format and print colored text
        guy_age_colored = print_colored(f"{guy_age:8}", 36)  # Bright blue color code is 36
        min_girl_age_colored = print_colored(f"{min_girl_age:10}", 32)  # Green color code is 32
        max_girl_age_colored = print_colored(f"{max_girl_age:10}", 32)
        
        print(f"{guy_age_colored} | {min_girl_age_colored} | {max_girl_age_colored}")
        
        guy_ages.append(guy_age)
        min_girl_ages.append(min_girl_age)
        max_girl_ages.append(max_girl_age)

    midpoint_y_min = average(min_girl_ages)
    midpoint_y_max = average(max_girl_ages)

    upper_x, upper_y = centroid_coordinates(start, min(max_girl_ages), start, max_girl_ages[-1], end, max_girl_ages[-1])

    plt.figure(figsize=(10, 6))

    plt.text(upper_x, upper_y, 'MOMMY ZONE', ha='center', fontsize=12, color='black', rotation=0, weight='bold')
    plt.text((start+end)/2, (average(min_girl_ages) + average(max_girl_ages) )/2, 'ACCEPTABLE ZONE', ha='center', fontsize=12, color='black', rotation=0, weight='bold')
    plt.text((start+end)/2, midpoint_y_min/2, 'PREDATOR ZONE', ha='center', fontsize=12, color='black', rotation=0, weight='bold')

    plt.plot(guy_ages, min_girl_ages, color='blue', label="Min/Max Girl Age")
    plt.plot(guy_ages, max_girl_ages, color='blue')

    plt.fill_between(guy_ages, min_girl_ages, max_girl_ages, color='lightgreen', alpha=0.5)
    plt.fill_between(guy_ages, 0, min_girl_ages, color='lightcoral', alpha=0.5)
    plt.fill_between(guy_ages, max_girl_ages, max(max_girl_ages), color='lightcoral', alpha=0.5)
    plt.xlabel("Guy Age")
    plt.ylabel("Girl Age")
    plt.title("Appropriate Dating Age Range")
    plt.legend()
    plt.grid(True)
    plt.show()

clear_screen()
print("This is legal dating age calculator which tells you the maximum and minimum age a woman can have for a guy to be able to date her without being creepy.")
print()

while True:
    ans = None
    while ans != "age" and ans != "range":
        ans = input("For one age enter \"age\". For a range of ages enter \"range\"\n")
        clear_screen()

    if ans == "age":
        num = int(input("Enter age: "))
        print_age_table(num, num)
    else:
        start = int(input("Enter starting age: "))
        end = int(input("Enter last age: "))
        print_age_table(start, end)

    ans = None
    while ans != "y" and ans != "n":
        ans = input("Start over? (y/n) ")
    if ans == "n":
        break

