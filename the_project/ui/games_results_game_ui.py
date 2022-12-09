
import os
from sys import platform
import time
from ui.game_results import Game_Results
import datetime

HOME_TEAM = 0
AWAY_TEAM = 1

class G_R_Choose_Game_UI:
    def __init__(self, logic_connection, league):
        self.logic_wrapper = logic_connection
        self.league = league

    def menu_output(self):
        '''
        Lists all the matches of the given league
        '''
        print('List of the matches:')
        matches = self.league.matches_list
        games = []
        counter = 1
        all_teams = self.logic_wrapper.get_all_teams()
        for match in matches:
            teams_in_match = []
            for team_id in match[2]:
                for team in all_teams:
                    if team_id == team.id:
                        teams_in_match.append(team.name)
            print(f"{match[1]}\t", end="")
            print(f"{counter}. {teams_in_match[HOME_TEAM]} VS {teams_in_match[AWAY_TEAM]}")
            counter += 1
            
        print()
        print("q for quit")
        print("b for back")
        return matches

    def input_get_game(self):
        '''
        Calls the menu output
        Asks the user to choose a match of the given league
        Sends the chosen match to the game result ui
        '''
        matches = self.menu_output()
        match = None
        while not match:
            selection = input("Select the match by typing number located next to the selected match: ")
            if selection.isnumeric():
                if int(selection) in range(1, len(matches)+1):
                    match = matches[int(selection)-1]
                    menu = Game_Results(self.logic_wrapper, self.league, match)
                    back_method = menu.input_game_results()
                else:
                    self.clear_screen(platform)
                    matches = self.menu_output()
                    print("Match ID not in list")
            elif back_method == "q":
                print("bye")
                self.clear_screen(platform)
                quit()
            elif back_method == "b":
                return "b"
            else:
                self.clear_screen(platform)
                matches = self.menu_output()
                print("Match ID must be a number")

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

