
class League_Standings:
    def __init__(self,logic_connection, league) -> None:
        self.logic_wrapper = logic_connection
        self.league = league
    
    def menu_output(self):
        '''
        Prints out league standings
        '''
        print("{:>45}".format("League Standings!"))
        print("{:<20}{:<20}{:<20}{:<20}{:<20}".format("Name","Total Wins","Total losses","Total Matches","Total games won"))
                    
    
    def input_league_standings(self):
        self.menu_output()
        '''
        Calles the menu output
        Lists the league standings
        '''
        #makes dicts to store info in
        dict_total_games_won = {}
        dict_total_matches = {}
        dict_total_wins = {}
        dict_total_losses = {}
        dict_scores = {}
        already_played = []
        #gets all the teams
        teams = self.logic_wrapper.get_all_teams()
        #gets the results of past games
        results_of_matches = self.logic_wrapper.get_all_matches()
    
        for match_result in results_of_matches:
            #checks if the league id matches
            if match_result.league_id == self.league.id:
                #gets the total games won for both teams
                team_h_points = int(match_result.h_results)
                team_a_points = int(match_result.a_results)

                if team_h_points > team_a_points:

                    team_h_wins = 1
                    team_a_wins = 0
                else:
                    team_a_wins = 1
                    team_h_wins = 0
                #stores team id, total matches and total wins into the dicts
                if match_result.h_team_id not in dict_total_games_won:
                    already_played.append(match_result.h_team_id)
                    dict_total_games_won[match_result.h_team_id] = int(match_result.h_results)
                    dict_total_matches[match_result.h_team_id] = 1
                    dict_total_wins[match_result.h_team_id] = team_h_wins
                else:
                    dict_total_games_won[match_result.h_team_id] += int(match_result.h_results)
                    dict_total_matches[match_result.h_team_id] += 1
                    dict_total_wins[match_result.h_team_id] += team_h_wins
                if match_result.a_team_id not in dict_total_games_won:
                    already_played.append(match_result.a_team_id)
                    dict_total_games_won[match_result.a_team_id] = int(match_result.a_results)
                    dict_total_matches[match_result.a_team_id] = 1
                    dict_total_wins[match_result.a_team_id] = team_a_wins
                else:
                    dict_total_games_won[match_result.a_team_id] += int(match_result.a_results)
                    dict_total_matches[match_result.a_team_id] += 1
                    dict_total_wins[match_result.a_team_id] += team_a_wins
        
        #calcutaltes total losses for each team
        for key,val in dict_total_matches.items():
                dict_total_losses[key] = int(val) - dict_total_wins[key]
    
        #makes empthy dicts for the teams that have not played any matches
        for team in self.league.teams_list:
            if team not in already_played:
                dict_total_games_won[team] = 0
                dict_total_matches[team] = 0
                dict_total_wins[team] = 0
                dict_total_losses[team] = 0

        for key,val in dict_total_wins.items():
            for team in teams:
                if team.id == key:
                    #makes a new dict based on all the other dicts.
                    #Team name is the key, values are total wins, total losses, total matches played and total games won
                    dict_scores[team.name] = [val,dict_total_losses[key],dict_total_matches[key],dict_total_games_won[key]]
        #sorts the new dict by games won, total matches won and finally alfabetical order
        sorted_dict_scores = {k: v for k, v in sorted(dict_scores.items(), key=lambda item: item[0])}
        sorted_dict_scores = {k: v for k, v in sorted(dict_scores.items(), key=lambda item: item[1][0], reverse=True)}
        sorted_dict_scores = {k: v for k, v in sorted(dict_scores.items(), key=lambda item: item[1][3], reverse=True)}
        #prints out every team and their total wins, total losses, total matches played and total games won
        for key,val in sorted_dict_scores.items():
            print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(str(key),str(val[0]),str(val[1]),str(val[2]),str(val[3])))