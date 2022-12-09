class Game_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_game(self, game):
        '''
        Sends to datawrapper
        '''
        self.data_wrapper.create_game(game)

    def get_all_games(self):
        '''
        Sends to datawrapper
        '''
        return self.data_wrapper.get_all_games()