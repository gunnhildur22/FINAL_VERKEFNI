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
class G_R_Get_Results_T501_UI:
    def __init__(self, logic_connection, match):
        self.logic_wrapper = logic_connection
        self.match = match

    def input_results_T501(self):
        '''
        Gets results of the 4 player 501 game from user
        Returns a model object of the game result
        '''
        #get all the teams
        teams = self.logic_wrapper.get_all_teams()
        #get all the players
        all_players = self.logic_wrapper.get_all_players()
        #finds the home- and away team names and player id's
        for team in teams:
            if team.id == self.match[MatchTeams][HomeTeam]:
                h_team = team.name
                h_player_ids = team.player_ids
            if team.id == self.match[MatchTeams][AwayTeam]:
                a_team = team.name
                a_player_ids = team.player_ids
        
        #lists all the players from the home team
        self.print_teams(h_team,all_players,h_player_ids)
        #asks the user to choose a player from the list
        HP1 = input(f"Choose a player 1 from {h_team} (with no.): ")
        #error check
        while self.get_player_no(HP1,h_player_ids) == False:
            self.clear_screen(platform)
            self.print_teams(h_team,all_players,h_player_ids)
            print("must choose one player")
            HP1 = input(f"Choose a player 1 from {h_team} (with no.): ")
        self.clear_screen(platform)

        #asks repeatetly for players
        self.print_teams(h_team,all_players,h_player_ids)
        HP2 = input(f"Choose a player 2 from {h_team} (with no.): ")
        while self.get_player_no(HP2,h_player_ids) == False:
            self.clear_screen(platform)
            self.print_teams(h_team,all_players,h_player_ids)
            print("must choose one player")
            HP2 = input(f"Choose a player 2 from {h_team} (with no.): ")

        self.clear_screen(platform)
        self.print_teams(h_team,all_players,h_player_ids)
        HP3 = input(f"Choose a player 3 from {h_team} (with no.): ")
        while self.get_player_no(HP3,h_player_ids) == False:
            self.clear_screen(platform)
            self.print_teams(h_team,all_players,h_player_ids)
            print("must choose one player")
            HP3 = input(f"Choose a player 3 from {h_team} (with no.): ")
        
        self.clear_screen(platform)
        self.print_teams(h_team,all_players,h_player_ids)
        HP4 = input(f"Choose a player 4 from {h_team} (with no.): ")
        while self.get_player_no(HP4,h_player_ids) == False:
            self.clear_screen(platform)
            self.print_teams(h_team,all_players,h_player_ids)
            print("must choose one player")
            HP4 = input(f"Choose a player 4 from {h_team} (with no.): ")
        
        self.clear_screen(platform)
        self.print_teams(a_team,all_players,a_player_ids)
        AP1 = input(f"Choose a player 1 from {a_team} (with no.): ")
        while self.get_player_no(AP1,a_player_ids) == False:
            self.clear_screen(platform)
            self.print_teams(a_team,all_players,a_player_ids)
            print("must choose one player")
            AP1 = input(f"Choose a player 1 from {a_team} (with no.): ")
        
        self.clear_screen(platform)
        self.print_teams(a_team,all_players,a_player_ids)    
        AP2 = input(f"Choose a player 2 from {a_team} (with no.): ")
        while self.get_player_no(AP2,a_player_ids) == False:
            self.clear_screen(platform)
            self.print_teams(a_team,all_players,a_player_ids)
            print("must choose one player")
            AP2 = input(f"Choose a player 2 from {a_team} (with no.): ")

        self.clear_screen(platform)
        self.print_teams(a_team,all_players,a_player_ids)
        AP3 = input(f"Choose a player 3 from {a_team} (with no.): ")
        while self.get_player_no(AP3,a_player_ids) == False:
            self.clear_screen(platform)
            self.print_teams(a_team,all_players,a_player_ids)
            print("must choose one player")
            AP3 = input(f"Choose a player 3 from {a_team} (with no.): ")

        self.clear_screen(platform)
        self.print_teams(a_team,all_players,a_player_ids)
        AP4 = input(f"Choose a player 4 from {a_team} (with no.): ")
        while self.get_player_no(AP4,a_player_ids) == False:
            self.clear_screen(platform)
            self.print_teams(a_team,all_players,a_player_ids)
            print("must choose one player")
            AP4 = input(f"Choose a player 4 from {a_team} (with no.): ")
        
        #asks the user how the game went
        score = input(f"Enter result for this game (f.ex. 2-1): ")
        while self.get_correct_result(score) == False:
            self.clear_screen(platform)
            self.print_teams(a_team,all_players,a_player_ids)
            print("input must be x-x format")
            score = input(f"Enter result for this game (f.ex. 2-1): ")

        print("score registerd")
        self.slower_clean_screen(platform)
        #gets the game id
        all_games = self.logic_wrapper.get_all_games()
        id = len(all_games)+1

        game_type = "T501"
        #makes a model of the game result
        T501 = Game(id,game_type,score,HP1,HP2,HP3,HP4,AP1,AP2,AP3,AP4)
        #takes the model to the logic layer
        self.logic_wrapper.create_game(T501)
        print("score registerd")
        #returns a model of the game
        return T501

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
        
    def print_teams(self,team,all_players,player_ids,):
        '''
        Prints out the teams and their players
        '''
        print()
        print(f"4 players 501")
        print()

        print(team,":")
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
    
    def slower_clean_screen(self,platform):
        if platform == "linux" or platform == "linux2":
                time.sleep(1)
                os.system('clear')
        elif platform == "darwin":
            time.sleep(1)
            os.system('clear')
        elif platform == "win32":
            time.sleep(1)
            os.system('cls')