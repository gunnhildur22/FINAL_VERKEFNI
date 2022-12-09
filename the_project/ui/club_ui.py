import os
from sys import platform
import time
from model.club import Club
from ui.team_ui import Create_Team_UI
from model.club import Club

class Create_Club_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def create_menu_output(self):
        print("Create a club")
    
    def input_create(self):
        name = input("Enter a name of club: ")
        while self.get_club_name(name) == False:
            self.clear_screen(platform)
            print("name to short")
            name = input("Enter a name of club: ")
            
        self.clear_screen(platform)
        
        address = input("Input address for club: ")
        while self.get_address(address) == False:
            self.clear_screen(platform)
            print("invalid address")
            address = input("Input address for club: ")

        self.clear_screen(platform)
        
        phone = input("Enter phone no. : ")
        while self.get_phonenumber(phone) == False:
            self.clear_screen(platform)
            print("Phonenumbers must contain 7 numbers, Try again")
            phone = input("Enter phone no. : ")

        team_list = []
        self.clear_screen(platform)
        while True:
            self.print_options()
            c_or_e = input("Enter your selection: ")
            while self.get_correct_input(c_or_e) == False:
                self.clear_screen(platform)
                self.print_options()
                print("invalid input")
                c_or_e = input("Enter your selection: ")
                
            if c_or_e == "q":
                print("bye")
                quit()
            elif c_or_e == "1":
                self.clear_screen(platform)
                menu = Create_Team_UI(self.logic_wrapper)
                team_name = menu.input_create()
                teams = self.logic_wrapper.get_all_teams()
                for team in teams:
                    if team_name == team.name:
                        team_list.append(team.id)
            elif c_or_e == "2":
                self.clear_screen(platform)
                teams = self.logic_wrapper.get_all_teams()
                for team in teams:
                    print(team.id, team.name)
                team = input("choose a team by no. : ")
                team_list.append(team)
            done = input("Do you want to add another team to the club? (y/n) ? ")
            done = done.lower()
            while self.get_y_or_n(done) == False:
                self.clear_screen(platform)
                print('invalid input choose either, "y" or "n"')
                done = input("Do you want to add another team to the club? (y/n) ? ")
                done = done.lower()
            self.clear_screen(platform)

            if done == "n":
                break
        id = ""
        club = Club(id, name, address, phone, team_list)
        self.logic_wrapper.create_club(club)
        print("Club created successfully!")
        self.clear_screen(platform)

    def get_club_name(self,name):
        if len(name) < 2:
            return False
        elif name.isdigit() or name.isalpha():
            return True 

    def get_address(self, address):
        if len(address) < 2:
            return False
        return True
    
    def get_phonenumber(self, phonenumber):
        for n in phonenumber:
            if n.isalpha():
                return False
            elif len(phonenumber) !=7:
                return False
        return True
    
    def get_correct_input(self,command):
        if command == "1":
            return True
        elif command == "2":
            return True
        elif command == "q":
            return True
        else:
            return False

    def print_options(self):
        print("Teams of the club")
        print("1. Create a team")
        print("2. Choose a team from excisting list")
    
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
    
    def get_y_or_n(self,choice):
        if choice == "y" or choice == "n":
            return True
        else:
             return False