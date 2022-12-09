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
            print()
            print("1. Edit game date")
            print('2. Edit the game result ')
            print("b for back")
            print("q for quit")
            print()
            command = input("Enter your selection: ")
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

            
        