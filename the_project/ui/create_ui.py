
import os
import time
from ui.league_ui import Create_League_UI
from ui.club_ui import Create_Club_UI
from ui.team_ui import Create_Team_UI
from ui.player_ui import Create_Player_UI
from sys import platform

class Create_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def create_menu_output(self):
        '''
        Prints out the menu
        '''
        print("1. Create a league")
        print("2. Create a club")
        print("3. Create a team")
        print("4. Create a player")
        print("q for quit")
        print("b for back")
    
    def input_create(self):
        '''
        Calls the menu
        Gets input from user and calls appropriate fuction from appropriate class
        '''
        while True:
            self.create_menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                return "b"
            elif command == "q":
                print("bye")
                self.clear_screen(platform)
                return "q"
            elif command == "1":
                self.clear_screen(platform)
                menu = Create_League_UI(self.logic_wrapper)
                back_method = menu.input_create()
                if back_method == "q":
                    return "q"

            elif command == "2":
                self.clear_screen(platform)
                menu = Create_Club_UI(self.logic_wrapper)
                back_method = menu.input_create()
                if back_method == "q":
                    return "q"

            elif command == "3":
                self.clear_screen
                menu = Create_Team_UI(self.logic_wrapper)
                back_method = menu.input_create()
                if back_method == "q":
                    return "q"

            elif command == "4":
                self.clear_screen(platform)
                menu = Create_Player_UI(self.logic_wrapper)
                back_method = menu.input_create()
                if back_method == "q":
                    return "q"
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