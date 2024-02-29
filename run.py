# Import libraries
import sys
import time
from google.oauth2.service_account import Credentials
import gspread
from datetime import datetime
import os
import colorama
from colorama import Fore, Back

colorama.init(autoreset=True)  # Reset the color and the style automatically

"""
For the import of the gspread library and setting up the APIs, I used the
instructions of the Code Institute love sandwiches walkthrough
"""

# Const to list the APIs that the  program should access in order to run.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
# Load the credentials from the service account json file
CREDS = Credentials.from_service_account_file("creds.json")
# Define the scope and authenticate
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# Open the google spreadsheet and access the worksheets
SHEET = GSPREAD_CLIENT.open("life-in-numbers-secure")
WORKSHEET_USER = SHEET.get_worksheet(0)

CURRENT_YEAR = datetime.now().year

# Empty dictionary to store the duplicated worksheets
worksheets = {}


def clear_screen():
    """
    Clears the screen from text,
    Code fpr print statement was given me by my mentor brian macheria
    """
    print("\033c", end="")


def delete_worksheet(worksheet):
    """
    Deletes a worksheet from google sheet 'life in numbers'

    Args:
        worksheet: The worksheet to be deleted.
    """
    SHEET.del_worksheet(worksheet)


def duplicate_worksheet(sheet_name, new_sheet_name):
    """
    Duplicates an existing worksheet

    Args:
        sheet_name: Name of the worksheet that's going to be duplicated
        new_sheet_name: Name of the duplicated worksheet
    """
    new_worksheet = sheet_name.duplicate()
    new_worksheet.update_title(new_sheet_name)
    worksheets[new_sheet_name] = new_worksheet


def typing_print(text):
    """
    Prints text character by character with a delay of 0.05 seconds.
    Tutorial was found at 101computing

    Args:
        text: Text to be printed to the console with time delay as a string
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.025)  # pause execution with a 0.025 seconds delay


def program_start():
    """
    Displays the program logo and disclaimer
    """
    program_logo()
    typing_print("In this application, you will learn some facts based on data"
                 " related to your\nlife by entering some details about"
                 " yourself. You have the option to select\nfrom two different"
                 " topics.\n"
                 )
    disclaimer()


def disclaimer():
    """
    Prints a disclaimer that informs the user about the storage of the input
    and provides the possibility to end the application by asking to continue.

    Raises:
        ValueError, if the answer to continue wasn't given, is a number, or is
        not y, yes, n or no
    """
    print(Fore.MAGENTA + "DISCLAIMER: ")
    print("The data entered is stored in a Google Worksheet for the duration"
          " of use. Once\nall the data has been completed and a topic has been"
          " selected, you can exit the\nprogram. The data entered will then be"
          " deleted automatically.\nPlease ensure that when you start the"
          " program, you go to the end of it, and the\nfarewell message has"
          " been displayed to guarantee that your data has been \ndeleted"
          " correctly."
          )
    while True:
        continue_answer = (
            input(
                Fore.CYAN
                + "Do you want to continue? (y for yes / n for no)"
                + Fore.WHITE
                + "\n"
            )
            .lower()
            .strip()
        )
        try:
            if continue_answer == "y" or continue_answer == "yes":
                print(Fore.GREEN + "Great!")
                typing_print("Let's start with your name and your birth "
                             "year:\n")
                break
            elif continue_answer == "n" or continue_answer == "no":
                print(
                    "Thank you for visiting this application. See you soon at "
                    + Fore.GREEN
                    + "Your Life in Numbers."
                )
                time.sleep(3)  # Clear the screen after a 3 seconds delay
                clear_screen()
                sys.exit()
            elif not continue_answer:
                raise ValueError(
                    Fore.RED
                    + "You must give an answer if you would like to continue."
                    " y for yes or n for no"
                )
            elif ((continue_answer not in ["n", "y"]) or
                  (continue_answer.isdigit())):
                raise ValueError(Fore.RED + "Please enter only y or n")
        except ValueError as e:
            print(e)


def program_end():
    """
    Displays a goodbye message, clears screen, deletes worksheet
    and ends the program
    """
    print(
        Fore.BLUE
        + f"\n{user.name}"
        + Fore.WHITE
        + ", thank you for visiting this application."
    )
    print("See you soon at " + Fore.GREEN + "Your Life in Numbers.")
    typing_print(
        "The program will end in 5 seconds and delete your inputs from"
        " the worksheet."
    )
    # Wait for 5 seconds until the screen is cleared and the appliacation ends
    time.sleep(5)
    delete_worksheet(worksheets[new_sheet_name])
    clear_screen()
    sys.exit()  # terminate the program


def program_logo():
    """
    Prints an ASCII Art Logo for the application 'Your Life in Numbers'
    """
    print(
        Fore.GREEN
        + r"""
 ____ ____ ____ ____ _________ ____ ____ ____ ____ _________
||Y |||o |||u |||r |||       |||L |||i |||f |||e |||       ||
||__|||__|||__|||__|||_______|||__|||__|||__|||__|||_______||
|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/_______\|
 ____ ____ _________ ____ ____ ____ ____ ____ ____ ____
||i |||n |||       |||N |||u |||m |||b |||e |||r |||s ||
||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
"""
    )


def get_name():
    """
    Asks user for their name and validates the input.

    Returns:
        username (str): The username as capitalized string

    Raises:
        ValueError, if no name has been entered, name is longer than 15
        characters long, contains a number, or has a special character
    """
    while True:
        try:
            username = (
                input(
                    Fore.CYAN
                    + "Please enter your name (max. 15 letters, no numbers"
                    " or special characters): "
                    + Fore.WHITE
                    + "\n"
                )
                .capitalize()
                .strip()
            )
            if len(username) > 15:
                raise ValueError(
                    Fore.RED
                    + "Sorry, your name is too long."
                    " Please use only 15 letters."
                )
            elif not username:
                raise ValueError(Fore.RED + "Sorry, you must add a name.")
            elif username.isalpha() is False:
                raise ValueError(
                    Fore.RED
                    + "Sorry, no spaces, numbers or special characters."
                )
            print(
                "Welcome to "
                + Fore.GREEN
                + "Your Life in Numbers"
                + Fore.WHITE
                + "! Nice to meet you,"
                + Fore.BLUE
                + f" {username}."
            )
            break
        # Print an error message if input is invalid
        except ValueError as e:
            print(e)

    return username


def get_birth_year():
    """
    Gets users birth year and validate the input.

    Returns:
        birth_year (int): The birth year as an integer

    Raises:
        ValueError, if no birth year has been entered, the year of birth has
        less than 4 numbers, contains not only numbers, is more than 116 years
        from the current year away, or is greater than the current year
    """
    while True:
        try:
            birth_year = input(
                Fore.CYAN
                + "Please enter your birth year (format: yyyy): "
                + Fore.WHITE
                + "\n"
            ).strip()
            # The oldest person in the world as officially recognised
            # by Guinness World Records was 116 years old.
            min_year = CURRENT_YEAR - 116
            max_year = CURRENT_YEAR + 0
            # Check if the birth year is within a reasonable range
            if not birth_year:
                raise ValueError(
                    Fore.RED
                    + "Sorry, you must add a birth year."
                    )
            elif not birth_year.isdigit() or len(birth_year) != 4:
                raise ValueError(
                    Fore.RED
                    + "Sorry, wrong format. Your birth year needs four numbers"
                    " (e.g. 1999)."
                )
            birth_year_num = int(birth_year)
            if birth_year_num <= min_year:
                raise ValueError(
                    Fore.RED
                    + "It seems like you've lived for centuries; please enter"
                    " a number in a reasonable\nrange."
                )
            elif birth_year_num >= max_year:
                raise ValueError(
                    Fore.RED
                    + "It seems like you are a (future) baby. Please enter at"
                    " least the last year."
                )
            # For better UX show the user the input was valid
            print(Fore.GREEN + f"Great age! {birth_year} is valid")
            time.sleep(2)  # pause for 2 seconds
            clear_screen()
            break
        # Print an error message if input is invalid
        except ValueError as e:
            print(e)
    return int(birth_year)


def get_gender():
    """
    Get the users gender and validate input.

    Returns:
        gender (str): The gender as lowercase string
    """
    program_logo()
    typing_print(
        "Some of the predictions are based on scientific calculations that"
        " include gender"
    )
    print(
        Fore.LIGHTYELLOW_EX
        + "\nATTENTION!\n"
        + Fore.WHITE
        + "Dear "
        + Fore.RED
        + "L"
        + Fore.MAGENTA
        + "G"
        + Fore.YELLOW
        + "B"
        + Fore.GREEN
        + "T"
        + Fore.BLUE
        + "Q"
        + Fore.CYAN
        + "+ "
        + Fore.WHITE
        + "Community,"
    )
    print("It's true that this isn't perfect, but since some of the"
          " calculations require\ngender, a statement needs to be made for"
          " gender assigned at birth or current\nphysical sex. Be sure, that"
          " the information will not be used for a\ndiscriminatory purpose."
          " Please use m for male and f for female."
          )
    while True:
        try:
            gender = (
                input(
                    Fore.CYAN
                    + "Please enter your gender assigned at birth or your"
                    " current physical sex (m/f):"
                    + Fore.WHITE
                    + "\n"
                )
                .lower()
                .strip()
            )
            if not gender:
                raise ValueError(
                    Fore.RED
                    + "Since some of the calculations require gender, please"
                    " enter m or f."
                )
            elif gender.isdigit() or len(gender) != 1:
                raise ValueError(
                    Fore.RED + "Sorry wrong format. Please enter only m or f."
                )
            elif gender not in ["m", "f"]:
                raise ValueError(Fore.RED + "Please enter only m or f")
            print(Fore.GREEN + "Your input can be used for the calculations.")
            break
        # Print an error message if input is invalid
        except ValueError as e:
            print(e)
    return gender


def get_weight_and_height(var, units):
    """
    Get user input for a float number

    Args:
        var (str): The variable or quantity for which the user is expected to
        input a value
        units (str): units in which the variable or quantity is expected to be
        inputted

    Returns:
        float_input (float): The number input as a float
    """
    typing_print(
        f"Your {var} should be given in {units} and contain a point for the "
        "decimal place.\n"
    )
    while True:
        value = input(
            Fore.CYAN
            + f"Please enter your {var} in {units}:"
            + Fore.WHITE
            + "\n"
        ).strip()
        try:
            # Convert the input to a float
            float_input = float(value)
            return float_input
        except ValueError:
            # Print an error message if input is invalid
            print(
                Fore.RED
                + f"Invalid entry! Please enter your {var} in {units} with a"
                " point for decimal."
            )


def validate_weight_and_height(var, units, average_min, max_input):
    """
    Validate the users input for weight and height

    Args:
        var (str): The variable or quantity for which the user is expected to
        input a value
        units (str): units in which the variable or quantity is expected to be
        inputed
        average_min (float): The minimum variable the user can give
        max_input (float): The maximum input the user can give

    Returns:
        values (float): The validated number as a float

    Raises:
        ValueError, if the given input is not within a reasonable range
    """
    while True:
        values = get_weight_and_height(var, units)
        try:
            if values < average_min:
                raise ValueError(
                    Fore.RED
                    + f"{values} seems to be incorrect. The average {var} of a"
                    f" newborn is {average_min} {units}."
                )
            elif values > max_input:
                raise ValueError(
                    Fore.RED
                    + f"{values} seems to be incorrect. {max_input} {units} is"
                    " the guiness world record."
                )
            else:
                print(Fore.GREEN + f"Well done. {values} {units} is valid")
                return values
        except ValueError as e:
            print(e)


class User:
    """
    Represents the user who is utilizing the application
    """

    def __init__(self, name, year_of_birth, gender, height, weight, age):
        """
        Initialize the properties of the instance

        Args:
            self:
            name (str): The name of the user
            year_of_birth (int): The birt year of the user
            gender (str): The gender of the user
            height (float): The height of the user
            weight (float): The weight of the user
            age (int): The age of the user
        """
        self.name = name
        self.year_of_birth = year_of_birth
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age


def topic_question():
    """
    Asks the user which topic should be calculated.
    After validation of user input, display the corresponding function/message
    """
    typing_print("The topics are in the process of loading...")
    time.sleep(2)  # Wait for 2 seconds before the screen is cleared.
    clear_screen()
    program_logo()
    # print menu
    typing_print(
        "Please choose a topic you are interested in getting some calculations"
        " on:\n"
    )
    print("\n1. Health")
    print("2. Trivia")
    print("3. Exit\n")
    # Ask user for input and validate the input
    while True:
        try:
            account_selection = input(
                Fore.CYAN
                + "Enter your selection (1, 2 or 3): \n"
                + Fore.WHITE
                + ""
            ).strip()
            if account_selection == "1":
                health()
                next_topic("trivia")
            elif account_selection == "2":
                trivia()
                next_topic("health")
            elif account_selection == "3":
                program_end()
                break
            else:
                print(Fore.RED
                      + "Sorry, invalid input. Please enter 1, 2 or 3!")
        except ValueError as e:
            print(f"Sorry {e}, please try again and click the 'Run Prgramm'"
                  " Button. \n")


def next_topic(topic):
    """
    Allows the user to choose whether to proceed to the next topic or end the
    program.

    Args:
        topic (str): The other/next topic, that can be displayed

    Raises:
        ValueError, if the given answer is a number, or not y or n
    """
    while True:
        try:
            next_topic_input = (
                input(
                    Fore.CYAN
                    + "\nDo you want to know something about the other topic"
                    f" {topic}? (y/n)"
                    + Fore.WHITE
                    + "\n"
                )
                .lower()
                .strip()
            )
            if next_topic_input == "y" and topic == "trivia":
                trivia()
                input(Fore.CYAN + "\nPress Enter to end the application...\n")
                program_end()
            elif next_topic_input == "y" and topic == "health":
                health()
                input(Fore.CYAN + "\nPress Enter to end the application...\n")
                program_end()
                sys.exit()
            elif next_topic_input == "n":
                program_end()
                sys.exit()
            elif not next_topic_input:
                raise ValueError(
                    Fore.RED
                    + "You must give an answer. Please enter y for yes or n"
                    " for no"
                )
            elif ((next_topic_input not in ["n", "y"]) or
                  (next_topic_input.isdigit())):
                raise ValueError(Fore.RED + "Please enter only y or n")
        except ValueError as e:
            print(e)


def health():
    """
    Stores all the calculations for the topic health, like calulating the bmi,
    life expectancy and calories
    """
    clear_screen()
    program_logo()
    typing_print("Get ready to learn something about the topic:\n")
    print(Fore.MAGENTA + "\nHEALTH")
    time.sleep(1.5)  # time delay of 1.5 seconds
    calculate_bmi(user.weight, user.height, user.gender, user.age)
    time.sleep(1)  # time delay of 1 second
    calculate_life_expectancy()
    time.sleep(1)
    mifflin_st_jeor_equation(user.weight, user.height, user.gender, user.age)


def trivia():
    """
    Stores all the calculations for the topic trivia, like calculating the age,
    dog years and celestial age
    """
    clear_screen()
    program_logo()
    typing_print("\nGet ready to learn something about the topic:\n")
    print(Fore.MAGENTA + "\nTRIVIA\n")
    time.sleep(1.5)  # time delay of 1.5 seconds
    # get the calculated age of the user from the worksheet
    user_age = worksheets[new_sheet_name].acell("F2").value
    user_age_num = int(user_age)
    print(Fore.YELLOW + "Happy Birthday\n")
    print(
        "Wow, it seems like you are (turning) "
        + Fore.BLUE
        + f"{user_age_num}"
        + Fore.WHITE
        + " this year. What a marvelous age!"
    )
    time.sleep(1)  # time delay of 1 second
    human_to_dog_years(user_age_num)
    time.sleep(1)
    print(Fore.YELLOW + "\nCelestial Age\n")
    celestial_age(user_age_num)


def calculate_age(birth_year):
    """
    Calculates the age of the user based on the input given

    Args::
        birth_year (int): The birth year of the user

    Returns:
        age (int): The calculated age of the user
    """
    age = CURRENT_YEAR - birth_year
    return age


def calculate_bmi(weight, height, gender, age):
    """
    Calculates the bmi of the user

    Args:
        weight (float): The weight of the user
        height (float): The height of the user
        gender (str): The gender of the user
        age (int): The age of the user

    Return:
        bmi (float): The calculated BMI rounded by 2 decimal points
    """
    bmi = round(weight / (height * 2), 2)  # Round the BMI on 2 decimal points
    print(Fore.YELLOW + "\nBMI\n")
    if age < 20:
        print("To get a result for your BMI, you must be older than 19 years."
              " For your age,\nthis value is given in percentiles. We are"
              " currently working on implementing\nthis calculation, so it is"
              " worth coming back."
              )
    else:
        print("Your BMI is" + Fore.BLUE + f" {bmi}. ")
        if gender == "m":
            # The numbers for the classification were found at sueddeutsche.de
            if bmi < 18.50:
                print(
                    "Your weight status is classified as"
                    + Fore.BLUE
                    + " underweight"
                    + Fore.WHITE
                    + ". But please remember,\nthat the BMI is a very limited"
                    " calculation."
                )
            elif bmi < 25.0:
                print(
                    "Your weight status is classified as"
                    + Fore.BLUE
                    + " healthy weight"
                    + Fore.WHITE
                    + ". But please remember,\nthat the BMI is a very limited"
                    " calculation."
                )
            elif bmi < 30.0:
                print(
                    "Your weight status is classified as"
                    + Fore.BLUE
                    + " overweight"
                    + Fore.WHITE
                    + ". But please remember,\nthat the BMI is a very limited"
                    " calculation."
                )
            elif bmi >= 30.0:
                print(
                    "Your weight status is classified as"
                    + Fore.BLUE
                    + " obese"
                    + Fore.WHITE
                    + ". But please remember,\nthat the BMI is a very limited"
                    " calculation."
                )
        else:
            if bmi < 17.50:
                print(
                    "Your weight status is classified as "
                    + Fore.BLUE
                    + "underweight"
                    + Fore.WHITE
                    + ". But please remember,\nthat the BMI is a very limited"
                    " calculation."
                )
            elif bmi < 24.0:
                print(
                    "Your weight status is classified as "
                    + Fore.BLUE
                    + "healthy weight"
                    + Fore.WHITE
                    + ". But please remember,\nthat the BMI is a very limited"
                    " calculation."
                )
            elif bmi < 29.0:
                print(
                    "Your weight status is classified as "
                    + Fore.BLUE
                    + "overweight"
                    + Fore.WHITE
                    + ". But please remember,\nthat the BMI is a very limited"
                    " calculation."
                )
            elif bmi >= 29.0:
                print(
                    "Your weight status is classified as "
                    + Fore.BLUE
                    + "obese"
                    + Fore.WHITE
                    + ". But please remember,\nthat the BMI is a very limited"
                    " calculation."
                )

    return bmi


def calculate_life_expectancy():
    """
    Calculates the average life expectancy in weeks of a european male/female
    The current average life expectancy for europe was found at
    https://database.earth/
    """
    user_gender = user.gender
    user_age = user.age
    weeks_in_a_year = 52
    user_age_weeks = user_age * weeks_in_a_year
    # 76.8697(male) and 83.0172(female) was found at https://database.earth/
    average_age_male = 76.8697
    average_age_female = 83.0172
    weeks_male = round(average_age_male * weeks_in_a_year)
    weeks_female = round(average_age_female * weeks_in_a_year)
    print(Fore.YELLOW + "\nYears and Weeks\n")
    # calculate how many weeks a male person in europe has to live on average
    if user_gender == "m":
        print(
            "The average life expectancy of a person with the gender assigned"
            " at birth of\n'"
            + Fore.BLUE
            + "male"
            + Fore.WHITE
            + "' in Europe is currently"
            + Fore.BLUE
            + " 76,8697 years."
        )
        print(
            "So you only have about"
            + Fore.BLUE
            + f" {weeks_male} weeks"
            + Fore.WHITE
            + " to live your best life."
        )
        weeks_left_male = weeks_male - (user_age_weeks)
        if weeks_left_male > 0:
            print(
                "You have already experienced about"
                + Fore.BLUE
                + f" {user_age_weeks} weeks"
                + Fore.WHITE
                + " of it. Keep in mind \nthat you have approx."
                + Fore.BLUE
                + f" {weeks_left_male} weeks"
                + Fore.WHITE
                + " left to make your inner child happy. \nLet magic happen!"
            )
        else:
            print(
                "You have lived longer than the average person and you've been"
                " on this planet \nfor"
                + Fore.BLUE
                + f" {user_age_weeks} weeks"
                + Fore.WHITE
                + ". Congratulations. Continue to enjoy every day."
            )
    else:
        print(
            "The average life expectancy of a person with the gender assigned"
            " at birth of\n'"
            + Fore.BLUE
            + "female"
            + Fore.WHITE
            + "' in Europe is currently"
            + Fore.BLUE
            + " 83,0172 years."
        )
        print(
            f"So you only have about"
            + Fore.BLUE
            + f" {weeks_female} weeks"
            + Fore.WHITE
            + " to live your best life."
        )
        weeks_left_female = weeks_female - (user_age_weeks)
        if weeks_left_female > 0:
            print(
                f"You have already experienced about"
                + Fore.BLUE
                + f" {user_age_weeks} weeks"
                + Fore.WHITE
                + " of it. Keep in mind that you have \napprox."
                + Fore.BLUE
                + f" {weeks_left_female} weeks"
                + Fore.WHITE
                + " left to make your inner child happy. Let magic happen!"
            )
        else:
            print(
                f"You have lived longer than the average person and you've"
                " been on this planet \nfor"
                + Fore.BLUE
                + f" {user_age_weeks}"
                + Fore.WHITE
                + " weeks. Congratulations. Continue to enjoy every day"
            )


def mifflin_st_jeor_equation(weight, height, gender, age):
    """
    Calculates the resting metabolic rate(RMR)
    The calculation was found at the nasm blog

    Args:
        weight (float): The weight of the user
        height (float): The height of the user
        gender (str): The gender of the user
        age (int): The age of the user
    """
    print(Fore.YELLOW + "\nResting Metabolic Rate\n")
    # This is the Mifflin-St Jeor Equation. I found the numbers for this
    # calculation in the NASM blog
    rmr_plain = (10 * weight) + (6.25 * (height * 100)) - (5 * age)
    if gender == "m":
        rmr = rmr_plain + 5
    else:
        rmr = rmr_plain - 161
    print("The Resting Metabolic Rate (RMR) represents the total caloric"
          " expenditure when\nthe body is in a state of complete rest. RMR"
          " facilitates essential physio-\nlogical functions such as"
          " respiration, circulation, organ maintenance, and\nfundamental"
          " neurological processes."
          )
    typing_print("The RMR was calculated with the Mifflin-St Jeor equation.\n")
    time.sleep(1)  # time delay of 1 second
    print(
        "\nRegarding your weight, height, gender(GAAB/Current sex), and age,"
        " your RMR is:\n"
        + Fore.BLUE
        + f"{rmr}"
        + Fore.WHITE
        + " kcal/day. This is the energy your body needs daily to maintain"
        " normal \nphysiological function."
    )


def human_to_dog_years(age):
    """
    Calculates the age of the user into dog years.
    The calculation and the numbers were found at American Kennel Club

    Args:
        age (int): The age of the user
    """
    print(Fore.YELLOW + "\nDog Years\n")
    # The numbers for the steps of each dog year are from a table at
    # American Kennel Club
    if age == 1:
        dog_years = 15
    elif age == 2:
        dog_years = 15 + 9
    else:
        dog_years = 24 + (5 * age)
    print(
        "As a dog, you would already be "
        + Fore.BLUE
        + f"{dog_years}"
        + Fore.WHITE
        + " years old. 'Woof' to that!"
    )


def calculate_planet_age(planet,
                         planet_orbital_period,
                         planet_characteristic,
                         age):
    """
    Calculates the age on different planets.
    The Calculation was found on girlstart

    Args:
        planet (str): The name of the planet
        planet_orbital_period (float): The orbital period of the planet in
        Earth days
        planet_characteristic (str): The characteristic of the planet
        age (int): The age of the user
    """
    days_in_a_year = 365
    age_in_days = age * days_in_a_year
    planet_age = round(age_in_days / planet_orbital_period, 2)
    planet_age_days = round(planet_age * days_in_a_year)
    print(
        "If you lived on "
        + Fore.BLUE
        + f"{planet}"
        + Fore.WHITE
        + ", you'd have reached the age of "
        + Fore.BLUE
        + f"{planet_age}"
        + Fore.WHITE
        + f" {planet_characteristic} years,"
    )
    print(
        "which is about "
        + Fore.BLUE
        + f"{planet_age_days} "
        + Fore.WHITE
        + "days on Earth."
    )


def celestial_age(age_of_human):
    """
    Calculates the age of a human in terms of the orbital periods of various
    celestial bodies.

    Args:
        age_of_human (float) = The age of the human in Earth years.
    """
    # The numbers for the orbital time of the planets are from wikipedia.
    mercurian_orbital_period = 87.9691
    venusian_orbital_period = 224.7
    martian_orbital_period = 687
    jovian_orbital_period = 4331
    saturnian_orbital_period = 10747
    uranian_orbital_period = 30589
    neptunian_orbital_period = 59800
    calculate_planet_age("Mercury",
                         mercurian_orbital_period,
                         "Mercurian",
                         age_of_human)
    time.sleep(0.5)  # time delay of 0.5 second
    calculate_planet_age("Venus",
                         venusian_orbital_period,
                         "Venusian",
                         age_of_human)
    time.sleep(0.5)
    calculate_planet_age("Mars",
                         martian_orbital_period,
                         "Martian",
                         age_of_human)
    time.sleep(0.5)
    calculate_planet_age("Jupiter",
                         jovian_orbital_period,
                         "Jovian",
                         age_of_human)
    time.sleep(0.5)
    calculate_planet_age("Saturn",
                         saturnian_orbital_period,
                         "Saturnian",
                         age_of_human)
    time.sleep(0.5)
    calculate_planet_age("Uranus",
                         uranian_orbital_period,
                         "Uranian",
                         age_of_human)
    time.sleep(0.5)
    calculate_planet_age("Neptune",
                         neptunian_orbital_period,
                         "Neptunian",
                         age_of_human)


def update_user_worksheet(user, new_sheet_name):
    """
    Update user worksheet, adds new row with the list of data provided by the
    user from the class User. I used the instructions of the Code Institute
    love sandwiches walkthrough

    Args:
        user (User): The user object containing user data
        new_sheet_name (str): The name of the new created worksheet
    """
    print("Google Worksheet is currently being updated...")
    list_to_update = [
        user.name,
        user.year_of_birth,
        user.gender,
        user.height,
        user.weight,
        user.age,
    ]
    # Append a new row to the end of the new created worksheet with the list
    # items
    worksheets[new_sheet_name].append_row(list_to_update)


def get_last_entries():
    """
    Collects colums of data from a worksheet, adding the last 6 entries in
    a list and print this list for the user
    """
    headings = []
    columns = []
    for ind in range(1, 6):  # for loop iterates 5 times, ind is for loop index
        # col index begins with 1 not 0! col is used for columns
        column = worksheets[new_sheet_name].col_values(ind)
        columns.append(column[-1:])
        headings.append(column[0])
    print("You made the following entries:")
    # The Zip method to iterate through both lists was found on stack overflow
    for heading, col in zip(headings, columns):
        print(f"{heading}:" + Fore.BLUE + f" {col}")
        time.sleep(1)  # print each entry with a delay of 1 second
    time.sleep(2)


# MAIN
if __name__ == "__main__":
    program_start()
    # Give the worksheet a unique name by adding a timestamp to the name
    new_sheet_name = "Worksheet_" + datetime.now().strftime("%Y%m%d_%H%M%S")
    duplicate_worksheet(WORKSHEET_USER, new_sheet_name)
    name_input = get_name()
    birth_year_input = get_birth_year()
    gender_input = get_gender()
    # The average baby is born with a height of 0.49m and a weight of 3.3kg
    # Those numbers were in an article at sueddeutsche.de
    BABY_HEIGHT = 0.49
    BABY_WEIGHT = 3.3
    # The numbers for the highest/heaviest person was found at wikipedia
    TALLEST_HUMAN = 2.72
    HEAVIEST_HUMAN = 650.0
    height_input = validate_weight_and_height("height", "m", BABY_HEIGHT,
                                              TALLEST_HUMAN)
    weight_input = validate_weight_and_height("weight", "kg", BABY_WEIGHT,
                                              HEAVIEST_HUMAN)
    age_input = calculate_age(birth_year_input)
    # Collect user data and initialize the User object
    user = User(
        name_input,
        birth_year_input,
        gender_input,
        height_input,
        weight_input,
        age_input
    )
    # Update the new created worksheet with the user's data
    update_user_worksheet(user, new_sheet_name)
    get_last_entries()
    topic_question()
    # Deletes the new created worksheet
    delete_worksheet(new_sheet_name)
