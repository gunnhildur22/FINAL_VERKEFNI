
import csv
import os
from sys import platform
import time
from model.team import Team

from ui.player_ui import Create_Player_UI

class Create_Team_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def create_menu_output(self):
        self.clear_screen(platform)
        print("Create a team")
        
        '''
        Prints out the create team menu
        '''


    
    def input_create(self):
        '''
        Calls the menu function
        Gets all the input needed to make a team from user
        Lets the user choose a player to add to the team or create player
        Makes user choose a team captin
        Calls the logic wrapper with a team model object
        '''
        self.create_menu_output()
        name = input("Enter team name: ")
        
        while self.get_team_name(name) == False:
            self.clear_screen(platform)
            print("team name is to short")
            name = input("Enter team name: ")
            

        player_list = []
        player_list_for_captin = []
        while True:
            self.clear_screen(platform)
            print("1. Create a new player")
            print("2. Choose an excisting player")
            n_or_e = input("Enter your selection: ")
            while self.get_choice(n_or_e) == False:
                self.clear_screen(platform)
                print("1. Create a new player")
                print("2. Choose an excisting player")
                print("Must select one option")
                n_or_e = input("Enter your selection: ")
            self.clear_screen(platform)

            if n_or_e == "2":
                print("List of all players")
                players = self.logic_wrapper.get_all_players()
                for player in players:
                    print(f"{player.id}. {player.name}")
                input_player = input("choose a player by no. : ")
                
                for player in players:
                    if player.id == input_player:
                        player_list_for_captin.append(player.name)
                        player_list.append(player.id)
            elif n_or_e == "1":
                menu = Create_Player_UI(self.logic_wrapper)
                player_name = menu.input_create()
                players = self.logic_wrapper.get_all_players()
                for player in players:
                    if player.name == player_name:
                        player_list.append(player.id)
                        player_list_for_captin.append(player.name)
            add_new_player = input("Do you want to add a another player (y/n)? ")
            add_new_player = add_new_player.lower()
            if add_new_player == "n":
                break
        counter = 1
        for player in player_list_for_captin:
            print(f"{counter}. {player}")
            counter += 1
        choose_captin = input("Choose team captin by no. : ")
        players = self.logic_wrapper.get_all_players()
        for player in players:
            if player.name == player_list_for_captin[int(choose_captin)-1]:
                captin = player.id
        try:
            for player in players:
                if player.name == player_list_for_captin[int(choose_captin)-1]:
                    captin = player.id
        except:
            self.clear_screen(platform)


        id = ""
        team = Team(id,name, player_list, captin)
        self.logic_wrapper.create_team(team)
        print("Team created successfully!")
        self.clear_screen(platform)
        return name

    
    def get_team_name(self, name):
        if len(name) < 2:
           return False
        else:

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
    
    def get_choice(self,choice):
        if choice == "1" or choice == "2":
            return True

        else: 
            return False
    
    #def get_player_pick(self,players):
        