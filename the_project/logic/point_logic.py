

class Point_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def register_player_results(self, player_id, league_id, player_qp, player_insh, player_outsh):
        self.data_wrapper.register_player_results(player_id, league_id, player_qp, player_insh, player_outsh)
    
    def get_all_points(self):
        return self.data_wrapper.get_all_points()