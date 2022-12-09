import os
from sys import platform
import time
from logic.player_logic import Player_Logic
from model.player import Player


class Create_Player_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def create_menu_output(self):
        '''
        Prints out the create player menu
        '''
        print("Create a player")

    
    def input_create(self):
        '''
        Calls the menu
        Gets all the input needed to make a player from user
        Calls the logic wrapper with a player model object
        '''
        while True:
            self.create_menu_output()
            name = input("Enter player name: ")
            while self.get_valid_name(name) == False:
                self.clear_screen(platform)
                self.create_menu_output
                print("The name cannot contain numbers or is to short, please try again.")
                name = input("Enter player name: ")
            
            self.clear_screen(platform)
            social_security = input("Enter social security number: ")
            while self.get_social_security(social_security) == False:
                self.clear_screen(platform)
                self.create_menu_output
                print("The Social security number has to contain 10 numbers!")
                social_security = input("Enter social security number: ")
            
            self.clear_screen(platform)
            phonenumber = input("Enter player phonenumber: ")
            while self.get_phonenumber(phonenumber) == False:
                self.clear_screen(platform)
                self.create_menu_output
                print("Phonenumbrs must contain 7 numbers, try again")
                phonenumber = input("Enter player phonenumber: ")
            
            self.clear_screen(platform)
            address = input("Enter player address: ")
            while self.get_address(address) == False:
                self.clear_screen(platform)
                self.create_menu_output
                print("invalid address")
                address = input("Enter player address: ")

            self.clear_screen(platform)
            email = input("Enter a player email: ")
            while self.get_email(email) == False:
                self.clear_screen(platform)
                self.create_menu_output
                print("invalid email address")
                email = input("Enter a player email: ")

            id = ""
            #makes a model object of player
            player = Player(id,name, social_security, phonenumber, address, email)
            #calls the logic wrapper with the model object of player
            self.logic_wrapper.create_player(player)

            print("Player created successfully!")
            #returns the player name if called from the team_ui
            return name

    def get_valid_name(self, name):
        for char in name:
            if char.isdigit():
                return False
        if len(name) < 2:
            return False
        return True

    def get_social_security(self, ssn):
        for n in ssn:
            if n.isalpha():
                return False
            elif len(ssn) != 10:
                return False 
        return True
    
    def get_phonenumber(self, phonenumber):
        for n in phonenumber:
            if n.isalpha():
                return False
            elif len(phonenumber) !=7:
                return False
        return True


    def get_address(self, address):
        if len(address) < 2:
            return False
        elif address.isdigit():
            return False
            
        return True
        
        
    def get_email(self, email):
        split_mail = email.split("@")
        if "@" not in email:
            return False
        elif "." not in email:
            return False
        elif len(email) < 4:
            return False
        elif "." not in split_mail[1]:
            return False 
        return True 

    def clear_screen(self,platform):
        if platform == "linux" or platform == "linux2":
            time.sleep(0.5)
            os.system('clear')
        elif platform == "darwin":
            time.sleep(0.5)
            os.system('clear')
        elif platform == "win32":
            time.sleep(0.5)
            os.system('cls')