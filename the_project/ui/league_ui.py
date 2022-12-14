import csv
import os
from sys import platform
from model.league import League
import time
import datetime
from ui.team_ui import Create_Team_UI

class Create_League_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def create_menu_output(self):
        print("Create a league")

    def input_create(self):
        '''
        Gets all the userinput needed to make a league
        '''

        self.clear_screen(platform)
        name = input("Enter a name of league: ")
        while self.get_league_name(name) == False:
            self.clear_screen(platform)
            print("Name invalid, Try again")
            name = input("Enter a name of league: ")
        
        self.clear_screen(platform)   
        org_name = input("Enter name of organizer: ")
        while self.get_org_name(org_name) == False:
            self.clear_screen(platform)
            print("Invalid name for organizer, Try again")
            org_name = input("Enter name of organizer: ")
        
        self.clear_screen(platform)
        phone = input("Enter phone no. : ")
        while self.get_phonenumber(phone) == False:
            self.clear_screen(platform)
            print("Phonenumbers must contain 7 numbers, Try again")
            phone = input("Enter phone no. : ")

        self.clear_screen(platform)
        email = input("Enter email of organizer: ")
        while self.get_email(email) == False:
                self.clear_screen(platform)
                print("invalid email address")
                email = input("Enter email of organizer: ")
        
        self.clear_screen(platform)
        print("Enter start date of league: ")
        start_date = input("dd/mm/yyyy\t")
        while self.get_startdate(start_date) == False:
            self.clear_screen(platform)
            print("Invalid date, Try again")
            start_date = input("dd/mm/yyyy\t")
            self.clear_screen(platform)
        
        self.clear_screen(platform)
        team_list = []
        #get all the teams for the league
        while True:
            self.clear_screen(platform)
            self.print_teams_of_the_league_menu()
        
            c_or_e = input("Enter your selection: ")
            while self.get_correct_input(c_or_e) == False:
                self.clear_screen(platform)
                self.print_teams_of_the_league_menu()
                print("invaldi input")
                c_or_e = input("Enter your selection: ")
            
            if c_or_e == "q":
                print("bye")
                quit()
                
            if c_or_e == "1":
                self.clear_screen(platform)

            print("Teams of the League")
            print("1. Create a team")
            print("2. Choose an excisting team")
            create_or_excisting_team = input("Enter your selection: ")
            if create_or_excisting_team == "1":
                #calls the create team function and creates team
                menu = Create_Team_UI(self.logic_wrapper)
                #returns the team name to add it to the league
                team_name = menu.input_create()
                teams = self.logic_wrapper.get_all_teams()
                #finds the team id to add it to the list
                for team in teams:
                    if team_name == team.name:
                        team_list.append(team.id)
            elif c_or_e == "2":
                self.clear_screen(platform)

            elif create_or_excisting_team == "2":
                #lists all the teams
                teams = self.logic_wrapper.get_all_teams()
                for team in teams:
                    print(team.id, team.name)
                team = input("choose a team by no. : ")
                #adds the selected team to the list
                team_list.append(team)
            done = input("Do you want to add another team to the League? (y/n) ? ")
            done = done.lower()
            if done == "n":
                break
        id = ""
        matches_list = []
        #Makes a model object of the league
        league = League(id, name, org_name , phone, email, start_date, team_list, matches_list)
        #calls the logic wrapper with the model object
        self.logic_wrapper.create_league(league)
        print("League created successfully!")
        

    def get_league_name(self,name):
        if len(name) < 2:
            return False
        return True    
    
    def get_org_name(self,org_name):
        if len(org_name) < 2:
            return False
        return True 

    def get_phonenumber(self, phonenumber):
        for n in phonenumber:
            if n.isalpha():
                return False
            elif len(phonenumber) !=7:
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
    
    def get_startdate(self,startdate):
        date_today = datetime.datetime.now()
        try:
            datetime_object = datetime.datetime.strptime(startdate, '%d/%m/%Y')
        except ValueError:
            return False
        if datetime_object < date_today:
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
        
    def get_correct_input(self,command):
        if command == "1":
            return True
        elif command == "2":
            return True
        elif command == "q":
            return True
        else:
            return False

    def print_teams_of_the_league_menu(self):
        print("Teams of the League")
        print("1. Create a team")
        print("2. Choose an excisting team")