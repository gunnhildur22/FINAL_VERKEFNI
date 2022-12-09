from model.match import Match
class Match_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_match(self, match):
        '''
        Sends to datawrapper
        '''
        self.data_wrapper.create_match(match)

    def get_all_matches(self):
        '''
        Sends to datawrapper
        '''
        return self.data_wrapper.get_all_matches()
    
    def edit_result_of_match(self, new_result, match):
        '''
        Edits the result in match
        Makes a new model for match
        Sends to datawrapper
        '''
        new_result = new_result.split("-")
        match.h_results = new_result[0]
        match.a_results = new_result[1]
        match = Match(match.id,match.league_id,match.match_id,match.h_team_id,match.a_team_id,match.date,match.h_results,match.a_results,match.S501_1,match.S501_2,match.S501_3,match.S501_4,match.d301,match.dC,match.T501)
        return self.data_wrapper.edit_result_of_match(match)
