class Get_QP:
    def __init__(self, logic_connection, match, league) -> None:
        self.logic_wrapper = logic_connection
        self.match = match
        self.league = league
    
    def input_qp(self):
        teams = self.logic_wrapper.get_all_teams()
        all_players = self.logic_wrapper.get_all_players()
        for team in teams:
            if team.id == self.match[2][0]:
                for player in all_players:
                    if player.id in team.player_ids:
                        player_qp = input(f"Please enter Quality Points for {player.name}: ")
                        player_insh = input(f"Please enter highest inshot for {player.name} as a whole number: ")
                        player_outsh = input(f"Please enter highest outshot for {player.name} as a whole number: ")
                        self.logic_wrapper.register_player_points(player.id, self.league.id, player_qp, player_insh, player_outsh)
                    
            if team.id == self.match[2][1]:
                for player in all_players:
                    if player.id in team.player_ids:
                        player_qp = input(f"Please enter Quality Points for {player.name}: ")
                        player_insh = input(f"Please enter highest inshot for {player.name} as a whole number: ")
                        player_outsh = input(f"Please enter highest outshot for {player.name} as a whole number: ")
                        self.logic_wrapper.register_player_points(player.id, self.league.id, player_qp, player_insh, player_outsh)