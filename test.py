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
        text(str): Text to be printed to the console with time delay
    '''
    for character in text:
        sys.stdout.write(character) 
        sys.stdout.flush()
        time.sleep(0.025) # pause execution with a 0.025 seconds delay


def get_name():
    """
    Ask user for its name and validate the input.
        Parameters: None
        Returns: username
    """
    username = input(Fore.CYAN + "Please enter your name(max. 15 letters, no numbers or special characters): " + Fore.WHITE + "\n").capitalize()
    return username

class User:
    """
    Represents the user who is utilizing the application
    """
    def __init__(self):
        """
        Initialize the properties of the instance
        Parameters: self, name, birthyear, gender, height and weight
        """
        self.name = get_name()
    
    def validat_user_name():
        """
        Ask user for its name and validate the input.
            Parameters: None
            Returns: username
        """
        while True:
            try:
                if len(user.name) > 15:
                    raise ValueError(Fore.RED + "Sorry, your name is to long. Please use only 15 letters.")
                elif not user.name:
                    raise ValueError(Fore.RED + "Sorry, you must add an name")
                elif user.name.isalpha() == False:
                    raise ValueError(Fore.RED + "Sorry, no spaces, numbers or special characters")
                break
            # Print an error message if input is invalid    
            except ValueError as e:
                print(e)
    
        return user.name

user = User()

print(f"Well done {user.name}")
