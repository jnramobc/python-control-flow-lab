# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

# def print_greeting():
#     python_is_fun = True
#     if python_is_fun:
#         print("Python is fun!")

# # Call the function
# print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    letter_choice = input('Enter a letter "a-z": ').lower()

    # Check if the input is a single alphabetical character
    if len(letter_choice) == 1 and letter_choice.isalpha():
        # Check if the letter is a vowel
        if letter_choice in "aeiou":
            print(f"The letter {letter_choice} is a vowel.")
        else:
            print(f"The letter {letter_choice} is a consonant.")
    else:
        print("Please provide a valid single letter input.")


# call the function
check_letter()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    dog_age = input("Input a dog's age: ")

    # Check if the dog's age is valid
    if len(dog_age) <= 3 and dog_age.isnumeric() and int(dog_age) > 0:
        # Convert dog_age to integer after validation
        dog_age = int(dog_age)

        # Calculate dog years based on age
        if dog_age <= 2:
            print(f"The dog's age in dog years is {dog_age * 10}.")
        else:
            
            dog_years = (2 * 10) + ((dog_age - 2) * 7)
            print(f"The dog's age in dog years is {dog_years}.")
    else:
        print("Please enter a valid positive integer for the dog's age.")
# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    is_cold = input("Is it cold? (yes/no): ").lower()
    is_raining = input("Is it raining? (yes/no): ").lower()
    
    if is_cold == 'yes' and is_raining == 'yes':
        print("Wear a waterproof coat.")
    elif is_cold == 'yes' and is_raining == 'no':
        print("Wear a warm coat.")
    elif is_cold == 'no' and is_raining == 'yes':
        print("Carry an umbrella.")
    elif is_cold == 'no' and is_raining == 'no':
        print("Wear light clothing.")
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")

# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
      
    month = input("Enter the month of the year (Jan - Dec): ").capitalize()
    day = input("Enter the day of the month: ")

    
    if not day.isdigit():
        print("Invalid input. Day must be a number.")
        return

    day = int(day)

    # Validate the day range (1-31)
    if day < 1 or day > 31:
        print("Invalid day. Please enter a day between 1 and 31.")
        return

    # Check for the season based on month and day ranges
    if month in ["Dec", "Jan", "Feb"] or (month == "Mar" and day <= 19):
        if month == "Dec" and day >= 21:
            print(f"{month} {day} is in Winter.")
        elif month in ["Jan", "Feb"] or (month == "Mar" and day <= 19):
            print(f"{month} {day} is in Winter.")
        else:
            print(f"{month} {day} is not a valid winter date.")
    
    elif month in ["Mar", "Apr", "May"] or (month == "Jun" and day <= 20):
        if (month == "Mar" and day >= 20) or month in ["Apr", "May"] or (month == "Jun" and day <= 20):
            print(f"{month} {day} is in Spring.")
    
    elif month in ["Jun", "Jul", "Aug"] or (month == "Sep" and day <= 21):
        if (month == "Jun" and day >= 21) or month in ["Jul", "Aug"] or (month == "Sep" and day <= 21):
            print(f"{month} {day} is in Summer.")
    
    elif month in ["Sep", "Oct", "Nov"] or (month == "Dec" and day <= 20):
        if (month == "Sep" and day >= 22) or month in ["Oct", "Nov"] or (month == "Dec" and day <= 20):
            print(f"{month} {day} is in Fall.")
    
    else:
        print("Invalid month. Please enter a valid month (Jan - Dec).")

# Call the function
determine_season()
