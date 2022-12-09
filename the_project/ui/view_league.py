from ui.view_best_players import View_Best_Players
from ui.league_standings import League_Standings
from ui.results_of_past_games import R_Past_Games
from ui.future_games_ui import Future_Games_UI
from sys import platform
import os
import time



class View_League_UI:
    def __init__(self, logic_connection, league):
        self.logic_wrapper = logic_connection
        self.league = league
    
    def menu_output(self):
        '''
        Prints view league menu
        '''
        print("View Leagues")
        print("1. Future games")
        print("2. Results of past games")
        print("3. League standings")
        print("4. List best players")
        print("q for quit")
        print("b for back")
        
    
    def input_view_league(self):
        self.clear_screen(platform)
        while True:
            self.menu_output()
            command = input("Enter your choose: ")
            command = command.lower()
            if command == "q":
                print("quitting")
                return "q"
            elif command == "b":
                return "b"
            elif command == "1":
                menu = Future_Games_UI(self.logic_wrapper, self.league)
                league_menu = menu.input_future_game()
            elif command == "2":
                menu = R_Past_Games(self.logic_wrapper, self.league)
                back_method = menu.input_results_of_past_games()
            elif command == "3":
                menu = League_Standings(self.logic_wrapper, self.league)
                back_method = menu.input_league_standings()
            elif command == "4":
                menu = View_Best_Players(self.logic_wrapper, self.league)
                back_method = menu.menu_output()
            else:
                print("invalid input, try again")
                self.clear_screen(platform)
                

    
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