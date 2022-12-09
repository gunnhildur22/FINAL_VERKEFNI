import os 
from sys import platform
import time
from ui.view_league import View_League_UI


class View_Leagues_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("View Leagues")
        counter = 1
        leagues = self.logic_wrapper.get_all_leagues()
        for league in leagues:
            print(f"{counter}. {league.name}")
            counter += 1
        print("q for quit")
        print("b for back")
    
    def input_view_leagues(self):
        leagues = self.logic_wrapper.get_all_leagues()
        self.menu_output()
        
        while True:
            command = input("Choose a league by no. : ")
            command = command.lower()
            if command == "q":
                print("quitting")
                self.clear_screen(platform)
                return "q"
            elif command == "b":
                self.clear_screen(platform)
                return "b"
            for league in leagues:
                if league.id == command:
                    chosen_league = league
                    menu = View_League_UI(self.logic_wrapper, chosen_league)
                    league_menu = menu.input_view_league()
            else:
                print("invalid input, try again")

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