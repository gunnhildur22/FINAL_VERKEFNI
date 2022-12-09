from data.player_data import Player_data
from data.team_data import Team_data
from data.club_data import Club_data
from data.league_creator import League_data
from data.game_data import Game_data
from data.match_data import Match_data
from data.points_data import Points_data


class Data_Wrapper:
    def __init__(self):
        self.player_data = Player_data()
        self.team_data = Team_data()
        self.club_data = Club_data()
        self.league_creator = League_data()
        self.game_data = Game_data()
        self.match_data = Match_data()
        self.points_data = Points_data()

    def get_all_players(self):
        return self.player_data.read_all_players()

    def create_player(self, player):
        return self.player_data.create_player(player)

    def get_all_teams(self):
        return self.team_data.read_all_teams()
    
    def create_team(self,team):
        return self.team_data.create_team(team)
    
    def get_all_clubs(self):
        return self.club_data.read_all_clubs()
    
    def create_club(self,club):
        return self.club_data.create_club(club)

    def get_all_leagues(self):
        return self.league_creator.get_all_leagues()
    
    def create_league(self, league):
        return self.league_creator.create_league(league)
    
    def create_club(self,club):
        return self.club_data.create_club(club)
    
    def edit_dates_of_matches(self, league):
        return self.league_creator.edit_dates_of_matches(league)
    
    def create_game(self, game):
        return self.game_data.create_game(game)
    
    def get_all_games(self):
        return self.game_data.get_all_games()
    
    def create_match(self, match):
        return self.match_data.create_match(match)
    
    def get_all_matches(self):
        return self.match_data.get_all_matches()

    def register_player_results(self, player_id, league_id, player_qp, player_insh, player_outsh):
        return self.points_data.write_points(player_id, league_id, player_qp, player_insh, player_outsh)
    
    def get_player_stats(self, league_id, player_id):
        return self.points_data.read_stats(league_id, player_id)
    
    def edit_result_of_match(self, match):
        return self.match_data.edit_result_of_match(match)
    
    def edit_result_of_match(self, match):
        return self.match_data.edit_result_of_match(match)
    
    def get_all_points(self):
        return self.points_data.get_all_points()