

from data.data_wrapper import Data_Wrapper
from logic.player_logic import Player_Logic
from logic.team_logic import Team_Logic
from logic.club_logic import Club_Logic
from logic.league_logic import League_Logic
from logic.game_logic import Game_Logic
from logic.match_logic import Match_Logic
from logic.point_logic import Point_Logic

class LogicWrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.player_logic = Player_Logic(self.data_wrapper)
        self.team_logic = Team_Logic(self.data_wrapper)
        self.club_logic = Club_Logic(self.data_wrapper)
        self.league_logic = League_Logic(self.data_wrapper)
        self.game_logic = Game_Logic(self.data_wrapper)
        self.match_logic = Match_Logic(self.data_wrapper)
        self.point_logic = Point_Logic(self.data_wrapper)
        

    def create_player(self, player):
        return self.player_logic.create_player(player)

    def get_all_players(self):
        return self.player_logic.get_all_players()

    def create_team(self, team):
        return self.team_logic.create_team(team)
    
    def get_all_teams(self):
        return self.team_logic.get_all_teams()
    
    def get_all_clubs(self):
        return self.club_logic.get_all_clubs()
    
    def create_club(self, club):
        return self.club_logic.create_club(club)

    def get_all_leagues(self):
        return self.league_logic.get_all_leagues()
    
    def create_league(self, league):
        return self.league_logic.create_league(league)
    
    def edit_dates_of_matches(self, league_id, chosen_match_id, new_date):
        league = self.league_logic.edit_dates_of_matches(league_id, chosen_match_id, new_date)
    
    def create_game(self, game):
        return self.game_logic.create_game(game)
    
    def get_all_games(self):
        return self.game_logic.get_all_games()
    
    def create_match(self, match):
        return self.match_logic.create_match(match)
    
    def get_all_matches(self):
        return self.match_logic.get_all_matches()
    
    def register_player_points(self, player_id, league_id, player_qp, player_insh, player_outsh):
        return self.point_logic.register_player_results(player_id, league_id, player_qp, player_insh, player_outsh)
    
    def edit_result_of_match(self, new_result, match):
        return self.match_logic.edit_result_of_match(new_result,match)
    
    def get_all_points(self):
        return self.point_logic.get_all_points()