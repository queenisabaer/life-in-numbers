# Import colorama for text editing
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True) # Reset the color and the style automatically

# Import the sys and time library (e.g. for text typing effects)
import time,sys 

# Import the os library (e.g for clearing the screen)
import os

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
        time.sleep(0.05) # pause execution with a 0.05 seconds delay

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
    print("Welcome to " + Fore.GREEN + "Your Life in numbers" + Fore.WHITE + "!\n")
    print("In this application you learn some facts based on data around your life.")
    print("Since this is sensiblere data, you need an account.")
    print("Please choose from the following options: \n")
    account_question()
    
def account_question():
    '''
    Ask user, if account already exists or new one needs to be created.
    After validation of users input, display the corresponding function/message
    '''
    # print menu
    print("1. Create new account")
    print("2. Login to existing account")
    print("3. I forgot my password")
    print("4. Exit\n")
    # Ask user for input and validate the input 
    while True:
        try: 
            account_selection = input(Fore.YELLOW + "Enter your selection(1, 2, 3 or 4): \n" + Fore.WHITE + "")
            if account_selection == "1":
                clear_screen()
                create_account()
                break
            if account_selection == "2":
                print(Fore.WHITE + f"You choose {account_selection}")
                break
            if account_selection == "3":
                print(Fore.WHITE + f"You choose {account_selection}")
                break
            if account_selection == "4":
                print(Fore.WHITE + "Thank you for visiting this application. See you soon at " + Fore.GREEN + "Your life in Numbers" )
                time.sleep(5) # Wait for 5 seconds until the screen is cleared and the appliacation ends
                clear_screen()
                break
            else:
                print(Fore.RED + "Sorry, invalid input. Please enter 1, 2, 3 or 4!")
        except ValueError as e:
            print(f"Sorry {e}, please try again and click the \"Run Prgramm\" Button. \n")

def create_account():
    """
    Create a new account
    """
    typing_print("To create a new account you need to choose a username and a password. \n")
    username=input(Fore.CYAN + "Please enter a username: ")
    print(username)

programm_start()


