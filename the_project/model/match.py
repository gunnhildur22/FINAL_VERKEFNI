class Match:
    def __init__(self, id,league_id,match_id,h_team_id,a_team_id,date,h_results,a_results,S501_1,S501_2,S501_3,S501_4,d301,dC,T501) -> None:
        '''
        Makes a model for match
        '''
        self.id = id
        self.league_id = league_id
        self.match_id = match_id
        self.h_team_id = h_team_id
        self.a_team_id = a_team_id
        self.date = date
        self.h_results = h_results
        self.a_results = a_results
        self.S501_1 = S501_1
        self.S501_2 = S501_2
        self.S501_3 = S501_3
        self.S501_4 = S501_4
        self.d301 = d301
        self.dC = dC
        self.T501 = T501