from ui.edit_league import Edit_League_UI


class Edit_League_get_league_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        '''
        
        '''
        print("Edit League")
        counter = 1
        leagues = self.logic_wrapper.get_all_leagues()
        for league in leagues:
            print(f"{counter}. {league.name}")
            counter += 1
        print("q for quit")
        print("b for back")
    
    def input_get_league(self):
        leagues = self.logic_wrapper.get_all_leagues()
        self.menu_output()
        command = input("Choose a league by no. : ")
        command = command.lower()
        while True:
        
            if command == "q":
                print("quitting")
                return "q"
            elif command == "b":
                return "b"
            for league in leagues:
                if league.id == command:
                    chosen_league = league
                    menu = Edit_League_UI(self.logic_wrapper, chosen_league)
                    back_method = menu.input_edit_league()
                    if back_method == "q":
                        return "q"
                    break
            else:
                print("invalid input, try again")