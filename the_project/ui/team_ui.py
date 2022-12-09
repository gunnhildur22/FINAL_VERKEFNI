import csv
from model.team import Team

from ui.player_ui import Create_Player_UI

class Create_Team_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def create_menu_output(self):
        '''
        Prints out the create team menu
        '''
        print("Create a team")
        print("q for quit")
        print("b for back")
    
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
            print("team name is to short")
            name = input("Enter team name: ")

        player_list = []
        player_list_for_captin = []
        while True:
            print("1. Create a new player")
            print("2. Choose an excisting player")
            new_or_existing_player = input("Enter your selection: ")
            if new_or_existing_player == "2":
                #prints out all the players and lets user choose player
                players = self.logic_wrapper.get_all_players()
                for player in players:
                    print(f"{player.id}. {player.name}")
                input_player = input("choose a player by no. : ")
                #finds what player the user choose and adds player id to a list
                for player in players:
                    if player.id == input_player:
                        player_list_for_captin.append(player.name)
                        player_list.append(player.id)
            elif new_or_existing_player == "1":
                menu = Create_Player_UI(self.logic_wrapper)
                #creates a player and returns the player name
                player_name = menu.input_create()
                #finds the player that was created and adds him to the list
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
        #lists all the selected players
        for player in player_list_for_captin:
            print(f"{counter}. {player}")
            counter += 1
        #asks the user to pick a captin from the list
        choose_captin = input("Choose team captin by no. : ")
        #finds the player the user choose for captin
        players = self.logic_wrapper.get_all_players()
        for player in players:
            if player.name == player_list_for_captin[int(choose_captin)-1]:
                captin = player.id
        id = ""
        #Makes a model of team
        team = Team(id,name, player_list, captin)
        #calls the logic wrapper with the model of team
        self.logic_wrapper.create_team(team)
        print("Team created successfully!")
        return name

    
    def get_team_name(self, name):
        if len(name) < 2:
           return False
        return True