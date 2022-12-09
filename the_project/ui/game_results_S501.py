import os
from sys import platform
import time
from model.game import Game
import datetime
MatchId = 0
MatchDate = 1
MatchTeams = 2
HomeTeam = 0
AwayTeam = 1
class G_R_Get_Results_S501_UI:
    def __init__(self, logic_connection, match):
        self.logic_wrapper = logic_connection
        self.match = match

    def input_results_S501(self, no):
        '''
        Gets results of the single player 501 game from user
        Returns a model object of the game result
        '''
        #get all team
        teams = self.logic_wrapper.get_all_teams()
        #get all players
        all_players = self.logic_wrapper.get_all_players()

        #finds the home- and away team names and player id's
        for team in teams:
            if team.id == self.match[MatchTeams][HomeTeam]:
                h_team = team.name
                h_player_ids = team.player_ids
            if team.id == self.match[MatchTeams][AwayTeam]:
                a_team = team.name
                a_player_ids = team.player_ids
        
        self.clear_screen(platform)
        #lists out all the players of the home team
        self.print_teams(h_team,all_players,h_player_ids,no)
        #lets user choose a player that played the game
        HP1 = input(f"Choose a player from {h_team} (with no.): ")
        #error check
        while self.get_player_no(HP1, h_player_ids) == False:
            self.clear_screen(platform)
            self.print_teams(h_team,all_players,h_player_ids,no)
            print("must choose one player")
            HP1 = input(f"Choose a player 1 from {h_team} (with no.): ")

        self.clear_screen(platform)
        #lists out all the players of the home team
        self.print_teams(a_team,all_players,a_player_ids,no)
        #lets the user choose a player
        AP1 = input(f"Choose a player from {a_team} (with no.): ")
        #error check
        while self.get_player_no(AP1,a_player_ids) == False:
            self.clear_screen(platform)
            self.print_teams(a_team,all_players,a_player_ids,no)
            print("must choose one player")
            AP1 = input(f"Choose a player 1 from {a_team} (with no.): ")
        
        self.clear_screen(platform)
        #asks the user for result of the game
        score = input(f"Enter result for this game (f.ex. 2-1): ")
        while self.get_correct_result(score) == False:
            self.clear_screen(platform)
            print("input must be x-x format")
            score = input(f"Enter result for this game (f.ex. 2-1): ")
        #gets game id
        all_games = self.logic_wrapper.get_all_games()
        id = len(all_games)+1
        game_type = "S501"
        #empty because there was only one player playing for each team
        HP2 = ""
        HP3 = ""
        HP4 = ""
        AP2 = ""
        AP3 = ""
        AP4 = ""
        #gets model of the game result
        S501 = Game(id,game_type,score,HP1,HP2,HP3,HP4,AP1,AP2,AP3,AP4)
        #sends the model to logic layer
        self.logic_wrapper.create_game(S501)
        #returns the model
        return S501

    def print_teams(self,team,all_players,player_ids,no):
        '''
        Lists out all the players for the given team
        '''
        print()
        print(f"Single player 501 {no}")
        print()
        print(team)
        counter = 1
        for player in all_players:
            if player.id in player_ids:
                print(f"{counter}.\t{player.name}")
                counter += 1


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


    def get_player_no(self, player, player_ids):
        counter = 0
        listi = []
        for id in player_ids:
            counter += 1
            listi.append(str(counter))

        if player not in listi:
            return False
        else:
            return True

    def get_correct_result(self, result):

        if "-" not in result:
            return False
        
        split_result = result.split("-")
        if len(split_result) != 2:
            return False
        elif split_result[0].isalpha() or split_result[1].isalpha():
                return False
        elif split_result[0] == "1" and split_result[1] == "2":
            return True
        elif split_result[0] == "2" and split_result[1] == "1":
            return True
        elif split_result[0] == "0" and split_result[1] == "2":
            return True 
        elif split_result[0] == "2" and split_result [1] == "0":
            return True 
        else:
            return False
    