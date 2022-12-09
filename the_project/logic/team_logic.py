class Team_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_team(self, team):
        '''
        Sends to datawrapper
        '''
        self.data_wrapper.create_team(team)

    def get_all_teams(self):
        '''
        Sends to datawrapper
        '''
        return self.data_wrapper.get_all_teams()