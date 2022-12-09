import os
from sys import platform
import time
from ui.e_game_result import Edit_Game_Results
from ui.e_game_date import Edit_Game_Date_UI



class Edit_League_UI:
    def __init__(self, logic_connection, league):
        self.logic_wrapper = logic_connection
        self.league = league

    def input_edit_league(self):
        '''
        Asks the user what he wants to edit
        Calls a appropriate function from appropriate class
        '''
        while True:
            self.print_menu()
            command = input("Enter your selection: ")
            command = command.lower()
            while self.get_correct_input(command) == False:
                self.clear_screen(platform)
                self.print_menu()
                print("invalid input")
                command = input("Enter your selection: ")
                command = command.lower()

            if command == "b":
                return "b"
            elif command == 'q':
                return "q"
            elif command == "1":
                menu = Edit_Game_Date_UI(self.logic_wrapper, self.league)
                back_method = menu.input_edit_game_date()
                if back_method == "q":
                    return "q"
            elif command == "2":
                menu = Edit_Game_Results(self.logic_wrapper, self.league)
                back_method = menu.input_edit_game_date()
                if back_method == "q":
                    return "q"

    def get_correct_input(self,command):
        if command == "1":
            return True
        elif command == "2":
            return True
        elif command == "b":
            return True
        elif command == "q":
            return True
        else:
            return False

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
    
    def print_menu(self):
        print()
        print("1. Edit game date")
        print('2. Edit the game result ')
        print("b for back")
        print("q for quit")
        print()