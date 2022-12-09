import os
from sys import platform
import time
MatchId = 0
MatchDate = 1
MatchTeams = 2

class R_Past_Games:
    def __init__(self,logic_connection, league) -> None:
        self.logic_wrapper = logic_connection
        self.league = league
    
    def menu_output(self):
        print("Results of past games:")
        '''
        Prints out all past games of that league
        ''' 
        #gets all teams
        teams = self.logic_wrapper.get_all_teams()
        #gets all results of matches
        results_of_matches = self.logic_wrapper.get_all_matches()
        #gets the match list
        matches = self.league.matches_list
        print("{:>40}".format("Results of past matches!"))
        for match in matches:
            for match_result in results_of_matches:
                if match[MatchId] == int(match_result.match_id):
                    for team in teams:
                        if team.id == match_result.h_team_id:
                            home_team = team.name
                        if team.id == match_result.a_team_id:
                            away_team = team.name
                    print("{:<20}{:<20}{}-{:<10}{:>10}".format(match_result.date,home_team,match_result.h_results,match_result.a_results,away_team))
        print("q for quit")

        command = input("press enter to return ")
        if command == "q":
            print("bye")
            self.clear_screen(platform)
            quit()
        else:
            self.clear_screen(platform)
            return
    
    def input_results_of_past_games(self):
        '''
        Calls the menu output for results of past games
        '''
        self.menu_output()

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