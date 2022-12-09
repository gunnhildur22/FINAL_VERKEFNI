class Playerstats_UI:
    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection
    
    def menu_output(self):
        
        print("Please pick a league from the list:")
        counter = 1
        leagues = self.logic_wrapper.get_all_leagues()
        for league in leagues:
            print(f"{counter}. {league.name}")
            counter += 1
        print("q for quit")
        print("b for back")
        return counter
        
    def get_input(self):
        leagues = self.logic_wrapper.get_all_leagues()
        command = input("Input your command: ")
        if command == "b":
            return "b"
        elif command == "q":
            return "q"
        
        for league in leagues:
            if league.id == command:
                chosen_league = league
                
        
        print("Command not recognized")