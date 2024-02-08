# Import colorama for text editing
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True) # Reset the color and the style automatically

'''
For the import of the gspread library and setting up the APIs, I used the 
instructions of the Code Institute love sandwiches walkthrough
'''
# Import gspread library
import gspread
# Import the credentials class from google oauth library 
from google.oauth2.service_account import Credentials

# Import the sys library
import sys 

# Import the os library
import os

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


# Creat a function to clear the screen. Code was found at altcademy
def clear_screen ():
    '''
    Clear the screen
    '''
    os.system('cls' if os.name == 'nt' else 'clear')

# Start the programm
def programm_start():
    '''
    Start the Programm, show the welcome panel and login information
    Parameters: 
        None
    Return:
        None
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
    print("Welcome to " + Fore.GREEN + "Your Life in numbers" + Fore.WHITE + "!")
    print("In this application you can learn some facts based on figures about your life.")
    print("Since this is sensiblere data, you must first create an account.")
    
def account_question():
    '''
    Ask user if account already exists or new one needs to be created.
    After validation of users input, display the corresponding function
    '''
    # print menu
    print("1. Create new account")
    print("2. Login to account")
    print("3. Forget my password")
    #ask user for input and validate the input 
    while True:
        try: 
            account_selection = input(Fore.YELLOW + "Please enter your selection(1,2 or 3): \n")
            if account_selection == "1":
                print(Fore.WHITE + f"You choose {account_selection}")
                break
            if account_selection == "2":
                print(Fore.WHITE + f"You choose {account_selection}")
                break
            if account_selection == "3":
                print(Fore.WHITE + f"You choose {account_selection}")
                break
            else:
                print(Fore.RED + "Sorry, invalid input.")
        except ValueError as e:
            print(f"Sorry {e}, please try again. \n")


programm_start()
account_question()

