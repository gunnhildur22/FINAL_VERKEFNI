class Club_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_club(self, club):
        '''
        Sends to datawrapper
        '''
        self.data_wrapper.create_club(club)

    def get_all_clubs(self):
        '''
        Sends to datawrapper
        '''
        return self.data_wrapper.get_all_clubs()