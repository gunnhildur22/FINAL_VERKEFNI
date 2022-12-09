import datetime
import os
from sys import platform
import time

from ui.games_results_game_ui import G_R_Choose_Game_UI
class Games_Results_Choose_League_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection
    
    def menu_output(self):
        '''
        Lists out all the leagues
        '''
        print('List of the leagues:')
        leagues = self.logic_wrapper.get_all_leagues() 
        for league in leagues:
            print(f"{league.id}. {league.name}")
        print()
        print("q for quit")
        print("b for back")
        return leagues
    
    def input_games_results_get_league(self):
        '''
        Calls the menu output
        Asks the user to choose a league
        Sends the league to the game ui
        '''
        
        leagues = self.menu_output()
        select = input("Select the league by typing number located next to the selected league: ")
        while True:
            if select.lower() == "b":
                self.clear_screen(platform)
                return "b"
            elif select.lower() == "q":
                print("bye")
                self.clear_screen(platform)
                quit()
            else:
                try:
                    for league in leagues:
                        if int(league.id) == int(select):
                            self.clear_screen(platform)
                            the_league = league
                    menu = G_R_Choose_Game_UI(self.logic_wrapper, the_league)
                    back_method = menu.input_get_game()
                except:
                    self.clear_screen(platform)
                    leagues = self.menu_output()
                    print("Choose one league")
                    select = input("Select the league by typing number located next to the selected league: ")

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