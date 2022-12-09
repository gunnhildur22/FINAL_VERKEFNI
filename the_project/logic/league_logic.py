from datetime import timedelta, datetime, date
from math import factorial
from itertools import combinations
import datetime
from model.league import League

class League_Logic:
    def __init__(self, data_connection):
         self.data_wrapper = data_connection

    def create_league(self, league):
        '''
        Builds a list of matches and adds it to the league
        Sends to datawrapper
        '''
        #makes the dates of the matches
        #one match every week, first match is on the starting date
        starting_date = league.start_date.split("/")
        dates_list = []
        d_starting_date = datetime.date(int(starting_date[2]), int(starting_date[1]), int(starting_date[0]))
        dates_list.append(d_starting_date)
        last_date = d_starting_date
        #calculates how many matches will be
        total_matches = (len(league.teams_list)*(len(league.teams_list)-1))//2
        for i in range(total_matches-1):
            #every week, last match+7
            match_date = last_date + timedelta(days= 7)
            dates_list.append(match_date)
            last_date = match_date
        
        #makes every team play with every team once
        matches = list(combinations(league.teams_list, 2))
        counter = 0
        #makes a list of lists of the matches
        #the list containes match_id, date of match and two team id's
        for match in matches:
            sublist = []
            sublist.append(counter)
            sublist.append(dates_list[counter])
            sublist.append(match)
            league.matches_list.append(sublist)
            counter += 1
    
        self.data_wrapper.create_league(league)

    def get_all_leagues(self):
        '''
        Sends to datawrapper
        '''
        return self.data_wrapper.get_all_leagues()
    
    def edit_dates_of_matches(self, league_id, match_id, new_date):
        '''
        Finds the league and edits the date of match
        Makes new model for league
        Sends to Data wrapper
        '''
        leagues = self.get_all_leagues()
        for league in leagues:
            if league.id == league_id:
                the_league = league
                the_league.matches_list = list(the_league.matches_list[1:-1])
                for match in the_league.matches_list:
                    if match[0] == match_id:
                        match[1] = new_date
        league = League(the_league.id, the_league.name, the_league.org_name , the_league.phone, the_league.email, the_league.start_date, the_league.teams_list, the_league.matches_list)
        return self.data_wrapper.edit_dates_of_matches(league)