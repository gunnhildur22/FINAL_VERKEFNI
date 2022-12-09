MatchId = 0
class Edit_Game_Results:
    def __init__(self, logic_connection, league):
        self.logic_wrapper = logic_connection
        self.league = league

    def menu_output(self):
        '''
        Lists all results of past matches
        '''
        #gets all teams
        teams = self.logic_wrapper.get_all_teams()
        #gets all results of matches
        results_of_matches = self.logic_wrapper.get_all_matches()
        #gets the match list
        matches = self.league.matches_list
        print("{:>40}".format("Results of past matches!"))
        counter = 1
        for match in matches:
            for match_result in results_of_matches:
                if match[MatchId] == int(match_result.match_id):
                    for team in teams:
                        if team.id == match_result.h_team_id:
                            home_team = team.name
                        if team.id == match_result.a_team_id:
                            away_team = team.name
                    print("{}.  {:<20}{:<20}{}-{:<10}{:>10}".format(match_result.id,match_result.date,home_team,match_result.h_results,match_result.a_results,away_team))
                    counter += 1

    def input_edit_game_date(self):
        '''
        Calls the menu output
        Lets user choose a match to edit
        Gets new result from user
        Sends new result and match to logic layer
        '''
        self.menu_output()
        results_of_matches = self.logic_wrapper.get_all_matches()
        choose_a_match = input("Choose a match by no. :")
        for match in results_of_matches:
            if match.id == choose_a_match:
                new_result = input("Enter new result of match (f.ex. 3-4): ")
                self.logic_wrapper.edit_result_of_match(new_result, match)
        print("Result changed successfully!")
        


    