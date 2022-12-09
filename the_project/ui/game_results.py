from model.match import Match
from ui.game_results_T501 import G_R_Get_Results_T501_UI
from ui.game_results_c import G_R_Get_Results_C_UI
from ui.game_results_301 import G_R_Get_Results_301_UI
from ui.game_results_S501 import G_R_Get_Results_S501_UI
from ui.get_qp_ui import Get_QP
import datetime

class Game_Results:
    def __init__(self, logic_connection, league, match):
        self.logic_wrapper = logic_connection
        self.league = league
        self.match = match
    
    def input_game_results(self):
        '''
        Calls different files to get the results of the games in the match
        Sends a model of the game results to the logic layer
        '''
        #gets model of the results of the 501 single player games
        menu = G_R_Get_Results_S501_UI(self.logic_wrapper, self.match)
        S501_1 = menu.input_results_S501(1)
        S501_2 = menu.input_results_S501(2)
        S501_3 = menu.input_results_S501(3)
        S501_4 = menu.input_results_S501(4)
        #gets model of the result of the 301 game
        menu = G_R_Get_Results_301_UI(self.logic_wrapper, self.match)
        d301 = menu.input_results_301()
        #gets model of the result of the Cricked game
        menu = G_R_Get_Results_C_UI(self.logic_wrapper, self.match)
        dC = menu.input_results_C()
        #gets model of the result of the 4 player 501 game
        menu = G_R_Get_Results_T501_UI(self.logic_wrapper, self.match)
        T501 = menu.input_results_T501()

        league_id = self.league.id
        match_id = self.match[0]
        #gets the QP points for the players
        menu = Get_QP(self.logic_wrapper, self.match, self.league)
        menu.input_qp()
        score = 0
        #calls a function to get the total games won for home team and away team
        h_results,a_results = self.get_scores(S501_1,S501_2,S501_3,S501_4,d301,dC,T501)
        
        #gets the id's of the games
        S501_1 = S501_1.id
        S501_2 = S501_2.id
        S501_3 = S501_3.id
        S501_4 = S501_4.id
        d301 = d301.id
        dC = dC.id
        T501 = T501.id
        id = ""
        #gets the team ids of home- and away team
        h_team_id = self.match[2][0]
        a_team_id = self.match[2][1]
        #gets the date of the match
        date = self.match[1]
        #gets a model of the match
        match = Match(id,league_id,match_id,h_team_id,a_team_id,date,h_results,a_results,S501_1,S501_2,S501_3,S501_4,d301,dC,T501)
        #takes the model of the match to the logic layer
        self.logic_wrapper.create_match(match)
        print("Results written down successfully")

    def get_scores(self,S501_1,S501_2,S501_3,S501_4,d301,dC,T501):
        '''
        Calculates who won and returns total wins for home- and away team
        '''
        h_total = 0
        a_total = 0
        leg_score = S501_1.score.split("-")
        h_score = int(leg_score[0])

        a_score = int(leg_score[1])
        if h_score>a_score:
            h_total += 1
        else:
            a_total += 1
        leg_score = S501_2.score.split("-")
        h_score = int(leg_score[0])
        a_score = int(leg_score[1])
        if h_score>a_score:
            h_total += 1
        else:
            a_total += 1
        leg_score = S501_3.score.split("-")
        h_score = int(leg_score[0])
        a_score = int(leg_score[1])
        if h_score>a_score:
            h_total += 1
        else:
            a_total += 1
        leg_score = S501_4.score.split("-")
        h_score = int(leg_score[0])
        a_score = int(leg_score[1])
        if h_score>a_score:
            h_total += 1
        else:
            a_total += 1
        leg_score = d301.score.split("-")
        h_score = int(leg_score[0])
        a_score = int(leg_score[1])
        if h_score>a_score:
            h_total += 1
        else:
            a_total += 1
        leg_score = dC.score.split("-")
        h_score = int(leg_score[0])
        a_score = int(leg_score[1])
        if h_score>a_score:
            h_total += 1
        else:
            a_total += 1
        leg_score = T501.score.split("-")
        h_score = int(leg_score[0])
        a_score = int(leg_score[1])
        if h_score>a_score:
            h_total += 1
        else:
            a_total += 1
        score = f"{h_total}-{a_total}"
        return h_total,a_total
