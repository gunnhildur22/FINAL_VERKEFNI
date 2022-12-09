import datetime
import os
from sys import platform
import time
MatchId = 0
MatchDate = 1
MatchTeams = 2
class Future_Games_UI:
    def __init__(self, logic_connection, league):
        self.logic_wrapper = logic_connection
        self.league = league

    def menu_output(self):
        '''
        Prints out furure games
        '''
        self.clear_screen(platform)
        print("Future Games!")
        #gets all the matches of the league
        matches = self.league.matches_list
        teams_in_match = []
        for match in matches:
            #if the match is in the future
            if match[MatchDate] > datetime.date.today():
                teams_in_match = []
                #gets the teams from the match
                for team_id in match[MatchTeams]:
                    teams = self.logic_wrapper.get_all_teams() 
                    for team in teams:
                        if team_id == team.id:
                            teams_in_match.append(team.name)
                #prints the match date
                print(f"{match[MatchDate]}    ", end="")
            counter = 0
            #prints both teams that play the match
            for team in teams_in_match:
                if counter == 0:
                    print(team, end="")
                else:
                    print(f"  VS  {team}")
                counter+= 1

    def input_future_game(self):
        '''
        Calls the future game menu
        '''
        self.menu_output()
        print("b for back")
        print("q for quit")
        command = input("Enter your command: ")
        while True:
            if command == "q":
                print("bye")
                self.clear_screen(platform)
                quit()
            elif command == "b":
                self.clear_screen(platform)
                break
            else:
                self.clear_screen(platform)
                self.menu_output()
                print("b for back")
                print("q for quit")
                print('invalid input choose "q" or "b"')
                command = input("Enter your command: ")

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
            

