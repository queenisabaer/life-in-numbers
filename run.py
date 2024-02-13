# Import colorama for text editing
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True) # Reset the color and the style automatically

# Import the sys and time library (e.g. for text typing effects)
import time,sys 

# Import the os library (e.g. for clearing the screen)
import os

# Import datetime library (e.g. for validating the birthyear)
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
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# Access the google sheet
SHEET = GSPREAD_CLIENT.open('life-in-numbers')

# Create a function to clear the screen. Code was found at altcademy
def clear_screen ():
    '''
    Clear the screen
    '''
    os.system('cls' if os.name == 'nt' else 'clear')

# Delay the display of text on screen. Tutorial was found at 101computing 
def typing_print(text):
    '''
    Print text character by character with a delay of 0.05 seconds
    Parameters: 
        text(str): Text to be printed to the console
    '''
    for character in text:
        sys.stdout.write(character) 
        sys.stdout.flush()
        time.sleep(0.025) # pause execution with a 0.05 seconds delay

# Start the programm
def programm_start():
    '''
    Start the Programm, show welcome panel and login information
    '''
    programm_logo()
    typing_print("In this application, you will learn some facts based on data related to your\n")
    typing_print("life by entering some details about yourself. You have the option to select\n")
    typing_print("from different topics. But first, let's start with your name and birthyear.\n")
    time.sleep(2) #Pause the application for 2 seconds so the User can read the welcome text

def programm_logo():
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

def get_user_input():
    get_birthyear()
    typing_print("Some of the predictions are based on scientific calculations that include gender")
    print(Fore.LIGHTYELLOW_EX + "\nATTENTION!: " + Fore.WHITE + "Dear " + Fore.RED + "L" + Fore.MAGENTA + "G" + Fore.YELLOW + "B" + Fore.GREEN + "T" + Fore.BLUE + "Q" + Fore.CYAN + "+ " + Fore.WHITE + "Community,")
    typing_print("I know this is not perfect, but since some of the calculations require gender,\n")
    typing_print("an statement needs to be made for gender assigned at birth or current pyhsical\n")
    typing_print("sex. Be sure, that the information will not be used for a discriminatory\n")
    typing_print("purpose. Please use m for male and f for female.\n")
    get_gender()
    typing_print("Now the app needs your height in meters(e.g. 1.75)\n")
    height = get_weight_and_height('height', 'meters')
    typing_print("And finally your weight in kg(e.g. 69.4)\n")
    eight = get_weight_and_height('weight', 'kg')
    time.sleep(2)
    clear_screen()

def get_name():
    """
    Ask user for its name and validate the input.
        Parameters: None
        Returns: username
    """
    while True:
        try:
            username = input(Fore.CYAN + "Please enter your name(max. 15 letters, no numbers or special characters): " + Fore.WHITE + "\n").capitalize()
            if len(username) > 15:
                raise ValueError(Fore.RED + "Sorry, your name is to long. Please use only 15 letters.")
            elif not username:
                raise ValueError(Fore.RED + "Sorry, you must add an name")
            elif username.isalpha() == False:
                raise ValueError(Fore.RED + "Sorry, no spaces, numbers or special characters")
            break
        # Print an error message if input is invalid    
        except ValueError as e:
            print(e)
    
    return username

def get_birthyear():
    """
    Get users birthyear and validate the input. 
        Parameter: None
        Returns: birthyear
    """
    # Show the user that the input was valid by using the name before the next question
    name = get_name()
    print("Welcome to " + Fore.GREEN + "Your Life in Numbers" + Fore.WHITE + f"! Nice to meet you, {name}.")
    while True:
        try: 
            birthyear = input(Fore.CYAN + "Please enter your birthyear(format: xxxx): " + Fore.WHITE + "\n")
            # Check if the year is within a reasonable range
            current_year = int(str(datetime.datetime.now().year)) 
            min_year = current_year - 116 # The oldest person in the world as officially recognised by Guinness World Records was 116 years old.
            max_year = current_year + 0
            if not birthyear:
                raise ValueError(Fore.RED + "Sorry, you must add a birthyear")
            elif not birthyear.isdigit() or len(birthyear) != 4:
                raise ValueError(Fore.RED + "Sorry, wrong format. Your birthdate needs 4 numbers(e.g. 1999)" )
            birthyear_num = int(birthyear)
            if birthyear_num <= min_year:
                raise ValueError(Fore.RED + "Seems like you've lived centuries, please enter a number in a reasonable range")
            elif birthyear_num >=  max_year:
                raise ValueError(Fore.RED + "Seems like you are a (future) baby. Please enter at least last year.")
            print(Fore.GREEN + f"Great age! {birthyear} is valid") # For better UX show the user the input was valid
            break
        # Print an error message if input is invalid
        except ValueError as e:
            print(e)
    return birthyear

def get_gender():
    """
    Get users gender and validate input. 
    Parameters: None
    Returns: gender
    """
    while True:
        try:
            gender = input(Fore.CYAN + "Please enter your gender assigned at birth or your current pyhsical sex(m/f):" + Fore.WHITE + "\n")
            if not gender:
                raise ValueError(Fore.RED + "Since some of the calculations require gender, please enter m or f")
            elif gender.isdigit() or len(gender) != 1: 
                raise ValueError(Fore.RED + "Sorry wrong format. Please enter only m or f.")
            elif gender not in ['m', 'f', 'M', 'F']: 
                raise ValueError(Fore.RED + "Please enter only m or f")
            print(Fore.GREEN + "Your input can be used for the calculations.")
            break
        # Print an error message if input is invalid
        except ValueError as e:
            print(e)
    return gender

def get_weight_and_height(var, units):
    """
    Get user input for a float number and validate the input
    Parameters: 
        var: variable or quantity for which the user is expected to input a value
        units: units in which the variable or quantity is expected to be inputted
    Returns: the number input as a float
    """
    while True:
        value = input(Fore.CYAN + f"Please enter your {var} in {units}:" + Fore.WHITE + "\n")
        try:
            # Convert the input to a float and print the success message only if it succeeds
            float_input = float(value)
            print(Fore.GREEN + f"Well done. {float_input} is valid")
            return float_input
        except ValueError:
            # Print an error message if input is invalid
            print(Fore.RED + f"Invalid entry! Please enter your {var} in {units} with a point for decimal.")

def topic_question():
    '''
    Ask the user which topic should be played
    After validation of users input, display the corresponding function/message
    '''
    programm_logo()
    # print menu
    typing_print("Please choose a topic you are interested in getting some calculations on:\n")
    print("1. Health")
    print("2. Trivia")
    print("3. Exit\n")
    # Ask user for input and validate the input 
    while True:
        try: 
            account_selection = input(Fore.CYAN + "Enter your selection(1, 2 or 3): \n" + Fore.WHITE + "")
            if account_selection == "1":
                print("Well done, 1 ")
                break
            elif account_selection == "2":
                print(Fore.WHITE + f"You choose {account_selection}")
                break
            elif account_selection == "3":
                print(Fore.WHITE + "\nThank you for visiting this application. See you soon at " + Fore.GREEN + "Your life in Numbers.")
                typing_print("This application will end in 5 seconds.")
                time.sleep(5) # Wait for 3 seconds until the screen is cleared and the appliacation ends
                clear_screen()
                break
            else:
                print(Fore.RED + "Sorry, invalid input. Please enter 1, 2 or 3!")
        except ValueError as e:
            print(f"Sorry {e}, please try again and click the \"Run Prgramm\" Button. \n")

def main():
    programm_start()
    get_user_input()
    topic_question()

main()
