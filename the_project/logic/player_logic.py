class Player_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_player(self, player):
        '''
        Sends to datawrapper
        '''
        self.data_wrapper.create_player(player)

    def get_all_players(self):
        '''
        Sends to datawrapper
        '''
        return self.data_wrapper.get_all_players()