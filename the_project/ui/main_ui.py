import time
from logic.logic_wrapper import LogicWrapper
from logic.logic_wrapper import LogicWrapper
from ui.games_results_league_ui import Games_Results_Choose_League_UI
from ui.e_l_get_league import Edit_League_get_league_UI
from ui.view_leagues_ui import View_Leagues_UI
from ui.create_ui import Create_UI
from ui.player_stats_ui import Playerstats_UI
#from ui.view_league_ui import View_League_UI
#from ui.edit_league_ui import edit_league_UI
import os
from sys import platform

if platform == "linux" or platform == "linux2":
    print("program running on linux")
elif platform == "darwin":
    print("program running on mac")
elif platform == "win32":
    print("program running on windows")

class Menu_UI:
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()
        

    def menu_output(self):
        '''
        Prints out the main menu
        '''
        self.first_clear_screen(platform)

        '''for x in range (0,5):  
            b = "Loading" + "." * x
            print (b, end="\r")
            time.sleep(0.5)'''
        
        print(" _      _      __ _     _   ___  _  _  _    ")
        print("|_)| | |_) /\ (_ |_|\/||_|\ ||  / \|_)|_|\ | ")
        print("| \|_| |_)/--\__)|_|  ||_| \||  \_/|  |_| \|\n")
        
        
        txt = "MENU"
        x = txt.center(50)
        print(x)
        print()
        
        print("1. View league")
        print("2. Create")
        print("3. Register game result")
        print("4. Edit the league")
        print()
    
    def input_prompt(self):
        '''
        Calls the main menu
        Gets input from user and calls appropriate class
        '''

        command = ""
        while command != "q":
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            while self.get_correct_input(command) == False:
                self.clear_screen(platform)
                self.menu_output()
                print("Invalid input, try again")
                command = input("Enter your command: ")
                command = command.lower()

            
            if command == "1":
                self.clear_screen(platform)
                menu = View_Leagues_UI(self.logic_wrapper)
                back_method = menu.input_view_leagues()
                if back_method == "q":
                    return "q"
                
                
            elif command == "2":
                self.clear_screen(platform)
                menu = Create_UI(self.logic_wrapper)
                back_method = menu.input_create()
                if back_method == "q":
                    return "q"
                

            elif command == "3":
                self.clear_screen(platform)
                menu = Games_Results_Choose_League_UI(self.logic_wrapper)
                back_method = menu.input_games_results_get_league()
                if back_method == "q":
                    return "q"
    
            elif command == "4":
                self.clear_screen(platform)
                menu = Edit_League_get_league_UI(self.logic_wrapper)
                back_method = menu.input_get_league()
                if back_method == "q":
                    return "q"
            
            elif command == "q":
                print("Bye!")
                time.sleep(0.5)
                break
        return

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
    
    def first_clear_screen(self,platform):
        if platform == "linux" or platform == "linux2":
            os.system('clear')
        elif platform == "darwin":
            os.system('clear')
        elif platform == "win32":
            os.system('cls')
        
    def get_correct_input(self,command):
        if command == "1":
            return True
        elif command == "2":
            return True
        elif command == "3":
            return True
        elif command == "4":
            return True
        elif command == "q":
            return True
        else:
            return False