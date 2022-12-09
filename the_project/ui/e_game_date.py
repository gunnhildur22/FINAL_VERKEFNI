import datetime

MatchId = 0
MatchDate = 1
MatchTeams = 2
class Edit_Game_Date_UI:
    def __init__(self, logic_connection, league):
        self.logic_wrapper = logic_connection
        self.league = league

    def menu_output(self):
        
        print("Edit Game Date")
        print("Future Games!")
        matches = self.league.matches_list
        games = []
        nr = 1
        played_matches = 0
        for match in matches:
            if match[1] > datetime.date.today():
                teams_in_match = []
                for team_id in match[2]:
                    teams = self.logic_wrapper.get_all_teams() 
                    for team in teams:
                        if team_id == team.id:
                            teams_in_match.append(team.name)
            
                print(f"{nr}. {match[1]}    ", end="")
                counter = 0
                for team in teams_in_match:
                    if counter == 0:
                        print(team, end="")
                    else:
                        print(f"  VS  {team}")
                    counter+= 1
                nr += 1
            else:
                played_matches += 1
        return played_matches

    def input_edit_game_date(self):
        played_matches = self.menu_output()
        while True:
            command = input("Enter no. of game to change date: ")
            if command == "b":
                return "b"
                break
            elif command == 'q':
                return "q"
                break
            matches = self.league.matches_list
            for match in matches:
                if (int(command)-1+played_matches) == int(match[0]):
                    chosen_match_id = match[0]
                    print("Enter a new date for the match: ")
                    new_date = input("dd/mm/yyyy")
                    new_date = new_date.split("/")
                    new_date_ = datetime.date(int(new_date[2]), int(new_date[1]), int(new_date[0]))
                    league_id = self.league.id
                    self.logic_wrapper.edit_dates_of_matches(league_id, chosen_match_id, new_date_)




            
            else:
                print("Incorrect input, try again")