
class QP:
    def __init__(self,id,league_id,player_id, player_qp, player_insh, player_outsh) -> None:
        '''
        Makes a model of qp points
        '''
        self.id = id
        self.player_id = player_id
        self.league_id = league_id
        self.player_qp = player_qp
        self.player_insh = player_insh
        self.player_outsh = player_outsh