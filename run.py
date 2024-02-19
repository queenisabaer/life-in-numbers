# Import colorama for text editing
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True) # Reset the color and the style automatically

# Import the sys and time library (e.g. for text typing effects)
import time,sys 

# Import the os library (e.g. for clearing the screen)
import os

# Import datetime library (e.g. for validating the birth year)
import datetime

'''
For the import of the gspread library and setting up the APIs, I used the 
instructions of the Code Institute love sandwiches walkthrough
'''
# Import gspread library
import gspread
# Import the credentials class from google oauth library 
from google.oauth2.service_account import Credentials

# Const to list the APIs that the  program should access in order to run.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
# Load the credentials from the service account json file
CREDS = Credentials.from_service_account_file('creds.json')
# Define the scope and authenticate
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# Open the google spreadsheet and access the worksheets
SHEET = GSPREAD_CLIENT.open('life-in-numbers')
WORKSHEET_USER = SHEET.get_worksheet(0)

CURRENT_YEAR = int(str(datetime.datetime.now().year)) 

# Create a function to clear the screen. Code was found at altcademy
def clear_screen ():
    '''
    Clear the screen
    '''
    os.system('cls' if os.name == 'nt' else 'clear')

# To create this function I used a thread post at github by Anton Burnashev
def clear_worksheet(worksheet, clear_range):
    """
    Clear a worksheet from its values
    Parameters: 
        worksheet: specifies the worksheet to clear
        clear_range: specifies the range of the worksheet to be cleared
    """
    row_values = worksheet.range(clear_range)
    for row_value in row_values:
        row_value.value = ''
    worksheet.update_cells(row_values)

# Delay the display of text on screen. Tutorial was found at 101computing 
def typing_print(text):
    '''
    Print text character by character with a delay of 0.05 seconds
    Parameters: 
        text(str): Text to be printed to the console with time delay
    '''
    for character in text:
        sys.stdout.write(character) 
        sys.stdout.flush()
        time.sleep(0.025) # pause execution with a 0.025 seconds delay

# Start the program
def program_start():
    '''
    Start the Program, show welcome panel and Disclaimer
    '''
    # clear the worksheet, if the application wasn't finished properly
    clear_worksheet(WORKSHEET_USER, 'A2:F10')
    program_logo()
    typing_print(r"""In this application, you will learn some facts based on data related to your
life by entering some details about yourself. You have the option to select
from different topics.""" + "\n")
    disclaimer()

# Disclaimer
def disclaimer():
    """
    Show the disclaimer that informs the user about the storeage of the input and give the user the possibility to end application.
    """
    print(Fore.MAGENTA + "DISCLAIMER: ")
    print(r"""The data entered is stored in a Google Worksheet for the duration of use.
Once the application is complete, this data will automatically be deleted.""")
    while True:
        continue_answer = input(Fore.CYAN + "Do you want to continue?(y for yes / n for no)" + Fore.WHITE + "\n").lower().strip()
        try:
            if continue_answer == "y" or continue_answer == "yes":
                typing_print("Great, let's start with your name and your birth year.\n")
                break
            elif continue_answer == "n" or continue_answer == "no":
                print("Thank you for visiting this application. See you soon at " + Fore.GREEN + "Your Life in Numbers.")
                time.sleep(3) # Clear the screen after a 3 seconds delay
                clear_screen()
                sys.exit()
            elif not continue_answer:
                raise ValueError(Fore.RED + "You must give an answer if you would like to continue. y for yes or n for no")
            elif continue_answer not in ['n','y'] or continue_answer.isdigit(): 
                raise ValueError(Fore.RED + "Please enter only n or y")
        except ValueError as e:
            print(e)

# End the program
def program_end():
    """
    Function to display a goodbye message, clear screen and worksheet from its values and end the program
    """
    print(f"\n{user.name}, thank you for visiting this application.") 
    print("See you soon at " + Fore.GREEN + "Your life in Numbers.")
    typing_print("The program will end in 5 seconds and delete your inputs from the worksheet.")
    time.sleep(5) # Wait for 5 seconds until the screen is cleared and the appliacation ends
    clear_worksheet(WORKSHEET_USER, 'A2:F10')
    clear_screen()
    sys.exit() # terminate the program 

def program_logo():
     """
     Print an ASCII Art Logo for the application Your life in numbers
     """
     print(Fore.GREEN + r"""
 ____ ____ ____ ____ _________ ____ ____ ____ ____ _________ 
||Y |||o |||u |||r |||       |||L |||i |||f |||e |||       ||
||__|||__|||__|||__|||_______|||__|||__|||__|||__|||_______||
|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/_______\|
 ____ ____ _________ ____ ____ ____ ____ ____ ____ ____      
||i |||n |||       |||N |||u |||m |||b |||e |||r |||s ||     
||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||     
|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\| 
""")

def get_name():
    """
    Ask user for its name and validate the input.
        Parameters: None
        Returns: username as capitalized string
    """
    while True:
        try:
            username = input(Fore.CYAN + "Please enter your name(max. 15 letters, no numbers or special characters): " + Fore.WHITE + "\n").capitalize().strip()
            if len(username) > 15:
                raise ValueError(Fore.RED + "Sorry, your name is too long. Please use only 15 letters.")
            elif not username:
                raise ValueError(Fore.RED + "Sorry, you must add a name.")
            elif username.isalpha() == False:
                raise ValueError(Fore.RED + "Sorry, no spaces, numbers or special characters.")
            print("Welcome to " + Fore.GREEN + "Your Life in Numbers" + Fore.WHITE + f"! Nice to meet you, {username}.")
            break
        # Print an error message if input is invalid    
        except ValueError as e:
            print(e)
    
    return username

def get_birth_year():
    """
    Get users birth year and validate the input. 
        Parameter: None
        Returns: birth year as integer
    """
    while True:
        try: 
            birth_year = input(Fore.CYAN + "Please enter your birth year(format: xxxx): " + Fore.WHITE + "\n").strip()
            # Check if the year is within a reasonable range
            min_year = CURRENT_YEAR - 116 # The oldest person in the world as officially recognised by Guinness World Records was 116 years old.
            max_year = CURRENT_YEAR + 0
            if not birth_year:
                raise ValueError(Fore.RED + "Sorry, you must add a birth year")
            elif not birth_year.isdigit() or len(birth_year) != 4:
                raise ValueError(Fore.RED + "Sorry, wrong format. Your birthdate needs 4 numbers(e.g. 1999)" )
            birth_year_num = int(birth_year)
            if birth_year_num <= min_year:
                raise ValueError(Fore.RED + "Seems like you've lived for centuries; please enter a number in a reasonable range")
            elif birth_year_num >=  max_year:
                raise ValueError(Fore.RED + "Seems like you are a (future) baby. Please enter at least last year.")
            print(Fore.GREEN + f"Great age! {birth_year} is valid") # For better UX show the user the input was valid
            time.sleep(2) # pause for 2 seconds
            clear_screen()
            break
        # Print an error message if input is invalid
        except ValueError as e:
            print(e)
    return int(birth_year)

def get_gender():
    """
    Get users gender and validate input. 
    Parameters: None
    Returns: gender as lower string
    """
    program_logo()
    typing_print("Some of the predictions are based on scientific calculations that include gender")
    print(Fore.LIGHTYELLOW_EX + "\nATTENTION!\n" + Fore.WHITE + "Dear " + Fore.RED + "L" + Fore.MAGENTA + "G" + Fore.YELLOW + "B" + Fore.GREEN + "T" + Fore.BLUE + "Q" + Fore.CYAN + "+ " + Fore.WHITE + "Community,")
    print(r"""it's true that this isn't perfect, but since some of the calculations require
gender, a statement needs to be made for gender assigned at birth or current
physical sex. Be sure, that the information will not be used for a
discriminatory purpose. Please use m for male and f for female.""")
    while True:
        try:
            gender = input(Fore.CYAN + "Please enter your gender assigned at birth or your current physical sex(m/f):" + Fore.WHITE + "\n").lower().strip()
            if not gender:
                raise ValueError(Fore.RED + "Since some of the calculations require gender, please enter m or f.")
            elif gender.isdigit() or len(gender) != 1: 
                raise ValueError(Fore.RED + "Sorry wrong format. Please enter only m or f.")
            elif gender not in ['m', 'f']: 
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
    Parameters: 
        var: variable or quantity for which the user is expected to input a value
        units: units in which the variable or quantity is expected to be inputted
    Returns: the number input as a float
    """
    typing_print(f"Your {var} in {units} should be with a point for decimal.\n")
    while True:
        value = input(Fore.CYAN + f"Please enter your {var} in {units}:" + Fore.WHITE + "\n").strip()
        try:
            # Convert the input to a float
            float_input = float(value)
            return float_input
        except ValueError:
            # Print an error message if input is invalid
            print(Fore.RED + f"Invalid entry! Please enter your {var} in {units} with a point for decimal.")

def validate_weight_and_height(var, units, average_min, max_input):
    """
    Validate the users input for weight and height
    Parameters: 
        var: variable or quantity for which the user is expected to input a value
        units: units in which the variable or quantity is expected to be inputed
        average_min: minimum variable the user can give
        max_input: maximum input the user can give
    Returns: the validated number as a float
    """
    while True:
        values = get_weight_and_height(var, units)
        try:
            if values < average_min:
                raise ValueError(Fore.RED + f"{values} seems to be incorrect. The average {var} of a newborn is {average_min} {units}.")
            elif values > max_input:
                raise ValueError(Fore.RED + f"{values} seems to be incorrect. {max_input} {units} is the guiness world record.")
            else:
                print(Fore.GREEN + f"Well done. {values} is valid")
                return values
        except ValueError as e:
            print(e)    

# Create a class of the user
class User:
    """
    Represents the user who is utilizing the application
    """
    def __init__(self):
        """
        Initialize the properties of the instance
        Parameters: self
        """
        self.name = get_name()
        self.birthyear = get_birth_year()
        self.gender = get_gender()
        self.height = validate_weight_and_height('height', 'm', 0.49, 2.72)
        self.weight = validate_weight_and_height('weight', 'kg', 3.3, 650.0)
        self.age = calculate_age(self.birthyear)

def topic_question():
    '''
    Ask the user which topic should be calculated
    After validation of users input, display the corresponding function/message
    '''
    typing_print("Topics are currently beeing loaded...")
    time.sleep(2) # Wait for 2 seconds before the screen is cleared.
    clear_screen()
    program_logo()
    # print menu
    typing_print("Please choose a topic you are interested in getting some calculations on:\n")
    print("\n1. Health")
    print("2. Trivia")
    print("3. Exit\n")
    # Ask user for input and validate the input 
    while True:
        try: 
            account_selection = input(Fore.CYAN + "Enter your selection(1, 2 or 3): \n" + Fore.WHITE + "").strip()
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
                print(Fore.RED + "Sorry, invalid input. Please enter 1, 2 or 3!")
        except ValueError as e:
            print(f"Sorry {e}, please try again and click the \"Run Prgramm\" Button. \n")

def next_topic(topic):
    """
    Ask user for other topic depending 
    """
    while True:
        try:
            next_topic_input = input(Fore.CYAN + f"\nDo you want to know something about the other topic {topic}?(y/n)" + Fore.WHITE + "\n").lower().strip()
            if next_topic_input == "y" and topic == "trivia":
                time.sleep(30)
                program_end()
            elif next_topic_input == "y" and topic == "health":
                health()
                time.sleep(20)
                program_end()
                sys.exit()
            elif next_topic_input == "n":
                program_end()
                sys.exit()
            elif not next_topic_input:
                raise ValueError(Fore.RED + "You must give an answer. Please enter y for yes or n for no")
            elif next_topic_input not in ['n','y'] or next_topic_input.isdigit(): 
                raise ValueError(Fore.RED + "Please enter only y or n")
        except ValueError as e:
            print(e)

def health():
    """
    Stores all the calculations for the topic health, like calulating the bmi, life expectancy and calories
    """
    clear_screen()
    program_logo()
    typing_print("\nGet ready to learn something about the topic:\n")
    print(Fore.MAGENTA + "\nHEALTH")
    calculate_bmi(user.weight, user.height, user.gender, user.age) 
    calculate_life_expectancy()
    mifflin_st_jeor_equation(user.weight, user.height, user.gender, user.age)

def trivia():
    clear_screen()
    program_logo()
    typing_print("\nGet ready to learn something about the topic:\n")
    print(Fore.MAGENTA + "\nTRIVIA")
    # get the calculated age of the user from the worksheet
    user_age = WORKSHEET_USER.acell('F2').value 
    typing_print(f"Wow, seems like you are (turning) {user_age} this year.\n")

def calculate_age(birthyear):
    """
    Calculates the age of the user based on the input given
    parameters: 
        birthyear: takes the birth year as parameter
    Returns: calculated age
    """
    age = CURRENT_YEAR - birthyear
    return age                

def calculate_bmi(weight, height, gender, age):
    """
    Calculate the bmi of the user
    Parameters: 
        weight: weight of the user
        height: height of the user
        gender: gender of the user
        age: age of the user
    Return: bmi rounded by 2 decimal points
    """
    bmi = round(weight / (height * 2), 2) # Round the bmi on 2 decimal points
    print(Fore.YELLOW + "\nBMI\n")
    if age < 20:
        print(r"""To get a result for your BMI, you must be older than 19 years. For your age, 
this value is given in percentiles. We are currently working on implementing 
this calculation, so it is worth coming back.""")
    else:
        print("Your BMI is" + Fore.BLUE + f" {bmi}. ")    
        if gender == 'm':
            if bmi < 18.50:
                print("Your weight status is classified as" + Fore.BLUE + " underweight" + Fore.WHITE + ". But keep in mind,\nthat the BMI is a very limited calculation.")
            elif bmi < 25.0:
                print("Your weight status is classified as" + Fore.BLUE + "healthy weight" + Fore.WHITE + ". But keep in mind,\nthat the BMI is a very limited calculation.")
            elif bmi < 30.0:
                print("Your weight status is classified as" + Fore.BLUE + " overweight" + Fore.WHITE + ". But keep in mind,\nthat the BMI is a very limited calculation.")
            elif bmi >= 30.0:
                print("Your weight status is classified as" + Fore.BLUE + " obese" + Fore.WHITE + ". But keep in mind,\nthat the BMI is a very limited calculation.")
        else:
            if bmi < 17.50:
                print("Your weight status is classified as " + Fore.BLUE + "underweight" + Fore.WHITE + ". But keep in mind,\nthat the BMI is a very limited calculation.")
            elif bmi < 24.0:
                print("Your weight status is classified as " + Fore.BLUE + "healthy weight" + Fore.WHITE + ". But keep in mind,\nthat the BMI is a very limited calculation.")
            elif bmi < 29.0:
                print("Your weight status is classified as " + Fore.BLUE + "overweight" + Fore.WHITE + ". But keep in mind,\nthat the BMI is a very limited calculation.")
            elif bmi >= 29.0:
                print("Your weight status is classified as " + Fore.BLUE + "obese" + Fore.WHITE + ". But keep in mind,\nthat the BMI is a very limited calculation.")

    return bmi

def calculate_life_expectancy():
    user_gender = user.gender
    user_age = user.age
    user_age_weeks = user_age * 52
    # calculate how many weeks a male person in europe has to live on average
    weeks_male = round(76.8697 * 52)  # 76.8697 was found at https://database.earth/
    weeks_female = round(83.0172 * 52) 
    print(Fore.YELLOW + "\nYears and Weeks\n")
    if user_gender == "m":
        print("The average life expectancy of a person with a gender assigned at birth of")
        print(Fore.BLUE + "male " + Fore.WHITE + "in Europe is currently 76,8697 years.")
        print("So you only have about " + Fore.BLUE + f"{weeks_male} weeks" + Fore.WHITE + " to live your best life.")
        weeks_left_male = weeks_male - (user_age_weeks)
        if weeks_left_male > 0: 
            print("You have already experienced about " + Fore.BLUE + f"{user_age_weeks} weeks" + Fore.WHITE + " of it. Keep in mind \nthat you have approx." + Fore.BLUE + f" {weeks_left_male} weeks" + Fore.WHITE + " left to make your inner child happy.")
        else:
            print("You have lived longer than the average person and you've been on this planet \nfor" + Fore.BLUE + f" {user_age_weeks} weeks" + Fore.WHITE + ". Congratulations. Continue to enjoy every day.")
    else:
        print("The average life expectancy of a person with a gender assigned at birth of")
        print(Fore.BLUE + "female" + Fore.WHITE + " in Europe is currently" + Fore.BLUE + " 83,0172 years.")
        print(f"So you only have about " + Fore.BLUE + f"{weeks_female} weeks" + Fore.WHITE + " to live your best life.")
        weeks_left_female = weeks_female - (user_age_weeks)
        if weeks_left_female > 0:
            print(f"You have already experienced about " + Fore.BLUE + f"{user_age_weeks} weeks" + Fore.WHITE + " of it. Keep in mind that you have \napprox." + Fore.BLUE + f" {weeks_left_female} weeks" + Fore.WHITE + " left to make your inner child happy.")
        else:
            print(f"You have lived longer than the average person and you've been on this planet \nfor " + Fore.BLUE + f"{user_age_weeks}" + Fore.WHITE + " weeks. Congratulations. Continue to enjoy every day")

def mifflin_st_jeor_equation(weight, height, gender, age):
    """
    Calculate the resting metabolic rate
    """
    print(Fore.YELLOW + "\nResting Metabolic Rate\n")
    rmr_plain = (10*weight) + (6.25*(height*100)) - (5*age)
    if gender == "m":
        rmr = rmr_plain + 5
    else:
        rmr = rmr_plain - 161
    print(r"""The Resting Metabolic Rate (RMR) represents the total caloric expenditure when
the body is in a state of complete rest. RMR facilitates essential physio-
logical functions such as respiration, circulation, organ maintenance, and 
fundamental neurological processes. We calculated the RMR with the 
Mifflin-St Jeor equation.""")
    print("Regarding your weight, height, gender(GAAB/Current sex) and age your RMR is:\n"+ Fore.BLUE + f"{rmr}" + Fore.WHITE + " kcal/day. This is the energy your body needed daily to maintain normal \nphysiological function.")

# To update the google worksheet and get the data, I used the instructions of the Code Institute love sandwiches walkthrough
def update_user_worksheet(user): 
    """
    Update user worksheet, add new row with the list of data provided by the user from the class User.
    """
    print("Google Worksheet is currently being updated...")
    list = [user.name, user.birthyear, user.gender, user.height, user.weight, user.age]
    #  Append a new row to the end of the worksheet 'User' with the list items
    WORKSHEET_USER.append_row(list)

def get_last_entries():
    """
    Collects colums of data from User worksheet, adding the last 6 entries in a list
    and print this list for the user
    """
    headings = []
    columns = []
    for ind in range(1,6): #for loop iterates 5 times, ind is for loop index
        column = WORKSHEET_USER.col_values(ind) #col index begins with 1 not 0! col is used for columns
        columns.append(column[-1:])
        headings.append(column[0])
    print("You made the following entries:")
    # The Zip method to iterate through both lists was found on stack overflow
    for heading, col in zip(headings, columns):
        print(f"{heading}:" + Fore. CYAN + f" {col}")
        time.sleep(1) # print each entry with a delay of 1 second
    time.sleep(2)

# MAIN
if __name__ == "__main__":
    program_start()
    user = User() # Collect user data and initialize the User object
    update_user_worksheet(user) # Update the worksheet with the user's data
    get_last_entries()
    topic_question() 
