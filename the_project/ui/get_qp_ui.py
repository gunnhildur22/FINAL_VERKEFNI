import os
import time


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
                        player_qp = self.get_qp(player.name)
                        player_insh = self.get_insh(player.name)
                        player_outsh = self.get_outsh(player.name)
                        self.logic_wrapper.register_player_points(player.id, self.league.id, player_qp, player_insh, player_outsh)
                    
            if team.id == self.match[2][1]:
                for player in all_players:
                    if player.id in team.player_ids:
                        player_qp = self.get_qp(player.name)
                        player_insh = self.get_insh(player.name)
                        player_outsh = self.get_outsh(player.name)
                        self.logic_wrapper.register_player_points(player.id, self.league.id, player_qp, player_insh, player_outsh)
    
    def get_qp(self, player):
        while True:
            player_points = input(f"Please enter Quality Points for {player.name}: ")
            if player_points.isnumeric():
                if player_points >= 0:
                    return player_points
                else:
                    print("Please provide a non negative integer..")
            else:
                print("Please provide a non negative integer..")
                
    def get_insh(self, player):
        while True:
            player_points = input(f"Please enter highest inshot for {player.name}: ")
            if player_points.isnumeric():
                if player_points >= 0:
                    return player_points
                else:
                    print("Please provide a non negative integer..")
            else:
                print("Please provide a non negative integer..")
                
    def get_outsh(self, player):
        while True:
            player_points = input(f"Please enter highest outshot for {player.name}: ")
            if player_points.isnumeric():
                if player_points >= 0:
                    return player_points
                else:
                    print("Please provide a non negative integer..")
            else:
                print("Please provide a non negative integer..")
                        
    def clear_screen(self,platform):
        if platform == "linux" or platform == "linux2":
            time.sleep(0.5)
            os.system('clear')
        elif platform == "darwin":
            time.sleep(0.5)
            os.system('clear')
        elif platform == "win32":
            time.sleep(0.5)
            os.system('cls')