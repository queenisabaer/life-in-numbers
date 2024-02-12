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
    typing_print("In this application, you will learn some facts based on data related to your life by entering some details about yourself.\n")
    time.sleep(2) #Pause the application for 2 seconds so the User can read the welcome text
    get_birthyear()
    typing_print("Some of the predictions are based on scientific calculations that include gender.")
    print(Fore.LIGHTYELLOW_EX + "\nATTENTION!: " + Fore.WHITE + "Dear " + Fore.RED + "L" + Fore.MAGENTA + "G" + Fore.YELLOW + "B" + Fore.GREEN + "T" + Fore.BLUE + "Q" + Fore.CYAN + "+ " + Fore.WHITE + "Community,")
    typing_print("I know this is not perfect, but since some of the calculations require gender, an statement needs to be made.\n")
    typing_print("Be sure, that the information will not be used for a discriminatory purpose.\n")
    get_gender()




  
# def account_question():
#     '''
#     Ask user, if account already exists or new one needs to be created.
#     After validation of users input, display the corresponding function/message
#     '''
#     # print menu
#     print("1. Create new account")
#     print("2. Login to existing account")
#     print("3. I forgot my password")
#     print("4. Exit\n")
#     # Ask user for input and validate the input 
#     while True:
#         try: 
#             account_selection = input(Fore.YELLOW + "Enter your selection(1, 2, 3 or 4): \n" + Fore.WHITE + "")
#             if account_selection == "1":
#                 clear_screen()
#                 create_account()
#                 break
#             if account_selection == "2":
#                 print(Fore.WHITE + f"You choose {account_selection}")
#                 break
#             if account_selection == "3":
#                 print(Fore.WHITE + f"You choose {account_selection}")
#                 break
#             if account_selection == "4":
#                 print(Fore.WHITE + "Thank you for visiting this application. See you soon at " + Fore.GREEN + "Your life in Numbers" )
#                 time.sleep(5) # Wait for 5 seconds until the screen is cleared and the appliacation ends
#                 clear_screen()
#                 break
#             else:
#                 print(Fore.RED + "Sorry, invalid input. Please enter 1, 2, 3 or 4!")
#         except ValueError as e:
#             print(f"Sorry {e}, please try again and click the \"Run Prgramm\" Button. \n")

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
            if not username:
                raise ValueError(Fore.RED + "Sorry, you must add an name")
            if username.isalpha() == False:
                raise ValueError(Fore.RED + "Sorry, no spaces, numbers or special characters")
            break    
        except ValueError as e:
            print(e)
    
    return username

def get_birthyear():
    """
    Get users birthyear and validate the input. 
        Parameter: None
        Returns: birthyear
    """
    name = get_name()
    print("Welcome to " + Fore.GREEN + "Your Life in Numbers" + Fore.WHITE + f"! Nice to meet you, {name}.")
    while True:
        try: 
            birthyear = input(Fore.CYAN + "Please enter your birthyear(format: xxxx): " + Fore.WHITE + "\n")
            # Check if the year is within a reasonable range
            current_year = int(str(datetime.datetime.now().year)) 
            min_year = current_year - 100
            max_year = current_year + 0
            if not birthyear:
                raise ValueError(Fore.RED + "Sorry, you must add a birthyear")
            if not birthyear.isdigit() or len(birthyear) != 4:
                raise ValueError(Fore.RED + "Sorry, wrong format. Your birthdate needs 4 numbers(e.g. 1999)" )
            birthyear_num = int(birthyear)
            if birthyear_num <= min_year:
                raise ValueError(Fore.RED + "Seems like you already lived ages. Please enter a number less than 100 years into the past")
            if birthyear_num >=  max_year:
                raise ValueError(Fore.RED + "Pretty sure a (future) baby is not able to enter its birthyear")
            print(Fore.GREEN + "Great age!")
            break
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
            gender = input(Fore.CYAN + "Please enter your gender assigned at birth or your current pyhsical sex(m/w):" + Fore.WHITE + "\n")
            if not gender:
                raise ValueError(Fore.RED + "Since some of the calculations require gender, please enter m or w")
            if gender.isdigit() or len(gender) != 1: 
                raise ValueError(Fore.RED + "Sorry wrong format. Please enter only m or w.")
            if gender not in ['m', 'w', 'M', 'W']: 
                raise ValueError(Fore.RED + "Please enter only m or w")
            break
        except ValueError as e:
            print(e)
    return gender


programm_start()


