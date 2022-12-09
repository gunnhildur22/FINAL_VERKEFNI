import os
from sys import platform
import time
from model.game import Game
MatchId = 0
MatchDate = 1
MatchTeams = 2
HomeTeam = 0
AwayTeam = 1

class G_R_Get_Results_C_UI:
    def __init__(self, logic_connection, match):
        self.logic_wrapper = logic_connection
        self.match = match

    def input_results_C(self):
        '''
        Gets results of Cricket game from user
        Returns a model object of the game result
        '''
        teams = self.logic_wrapper.get_all_teams()
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
        
        #lists all the players from the home team
        self.print_team(h_team,all_players,h_player_ids)
        #asks the user to choose a player from the list
        HP1 = input(f"Choose a player 1 from {h_team} (with no.): ")
        #error check
        while self.get_player_no(HP1,h_player_ids) == False:
            self.clear_screen(platform)
            self.print_team(h_team,all_players,h_player_ids)
            print("must choose one player")
            HP1 = input(f"Choose a player 1 from {h_team} (with no.): ")
        self.clear_screen(platform)
        
        #asks repeatetly for players

        self.clear_screen(platform) 
        self.print_team(h_team,all_players,h_player_ids)    
        
        HP2 = input(f"Choose a player 2 from {h_team} (with no.): ")
        while self.get_player_no(HP2,h_player_ids) == False:
            self.clear_screen(platform)
            self.print_team(h_team,all_players,h_player_ids)
            print("choose one player")
            HP2 = input(f"Choose a player 2 from {h_team} (with no.): ")
        
        self.clear_screen(platform) 
        self.print_team(a_team,all_players,a_player_ids)

        AP1 = input(f"Choose a player 1 from {a_team} (with no.): ")
        while self.get_player_no(AP1,a_player_ids) == False:
            self.clear_screen(platform)
            self.print_team(a_team,all_players,a_player_ids)
            print("choose one player")
            AP1 = input(f"Choose a player 1 from {a_team} (with no.): ")
        
        self.clear_screen(platform) 
        self.print_team(a_team,all_players,a_player_ids)

        AP2 = input(f"Choose a player 2 from {a_team} (with no.): ")
        while self.get_player_no(AP2,a_player_ids) == False:
            self.clear_screen(platform)
            self.print_team(a_team,all_players,a_player_ids)
            print("choose one player")
            AP2 = input(f"Choose a player 2 from {a_team} (with no.): ")

        self.clear_screen(platform)
        #gets results of the game from user
        score = input(f"Enter result for this game (f.ex. 2-1): ")
        while self.get_correct_result(score) == False:
            self.clear_screen(platform)
            print("input must be x-x format")
            score = input(f"Enter result for this game (f.ex. 2-1): ")
        self.clear_screen(platform)
        
        #gets the game id
        all_games = self.logic_wrapper.get_all_games()
        id = len(all_games)+1
        game_type = "dC"
        #empty because there are only two players playing from each team
        HP3 = ""
        HP4 = ""
        AP3 = ""
        AP4 = ""
        #gets model of the game result
        dC = Game(id,game_type,score,HP1,HP2,HP3,HP4,AP1,AP2,AP3,AP4)
        #sends the model to the logic layer
        self.logic_wrapper.create_game(dC)
        return dC

    def print_team(self,team,all_players,player_ids):
        '''
        Lists out all the players for the given team
        '''
        print()
        print("Two players C")
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
