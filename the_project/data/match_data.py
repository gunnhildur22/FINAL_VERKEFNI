from model.match import Match
import csv
import os
class Match_data:
    def __init__(self) -> None:
        self.file_name = "FINAL_VERKEFNI/the_project/files/match_results.csv"

    def get_all_matches(self):
        '''
        Reads all matches from the given file
        '''
        ret_list = list()
        with open(self.file_name, "r", newline = "", encoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Match(row['id'], row['league_id'], row['match_id'], row['h_team_id'],row['a_team_id'], row['date'], row['h_results'],row['a_results'], row['S501_1'], row['S501_2'], row['S501_3'], row['S501_4'], row['d301'], row['dC'], row['T501']))
        return ret_list

    def create_match(self, match):
        id = len(self.get_all_matches()) + 1
        with open(self.file_name, "a", newline = "", encoding = "utf-8") as csvfile:
            fieldnames = ["id","league_id","match_id","h_team_id","a_team_id","date","h_results","a_results","S501_1","S501_2","S501_3","S501_4","d301","dC","T501"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writerow({'id': id ,'league_id': match.league_id, 'match_id': match.match_id, 'h_team_id': match.h_team_id,'a_team_id': match.a_team_id, 'date': match.date, 'h_results': match.h_results,'a_results': match.a_results,'S501_1': match.S501_1,'S501_2': match.S501_2,'S501_3': match.S501_3,'S501_4': match.S501_4,'d301': match.d301,'dC': match.dC,'T501': match.T501})
    
    def edit_result_of_match(self, match):
        with open(self.file_name, "r+", newline = "", encoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            with open("the_project/files/match_results_temp.csv", "a", newline = "", encoding = "utf-8") as csvfile:
                fieldnames = ["id","league_id","match_id","h_team_id","a_team_id","date","h_results","a_results","S501_1","S501_2","S501_3","S501_4","d301","dC","T501"]
                writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
                counter = 0
                for row in reader:
                    if counter == 0:
                        writer.writerow({'id': "id" ,'league_id': "league_id", 'match_id': "match_id", 'h_team_id': "h_team_id",'a_team_id': "a_team_id", 'date': "date", 'h_results': "h_results",'a_results': "a_results",'S501_1': "S501_1",'S501_2': "S501_2",'S501_3': "S501_3",'S501_4': "S501_4",'d301': "d301",'dC': "dC",'T501':"T501"})
                    if row["id"] == match.id:
                        writer.writerow({'id': match.id ,'league_id': match.league_id, 'match_id': match.match_id, 'h_team_id': match.h_team_id,'a_team_id': match.a_team_id, 'date': match.date, 'h_results': match.h_results,'a_results': match.a_results,'S501_1': match.S501_1,'S501_2': match.S501_2,'S501_3': match.S501_3,'S501_4': match.S501_4,'d301': match.d301,'dC': match.dC,'T501': match.T501})
                    else:
                        writer.writerow({'id': row["id"] ,'league_id': row["league_id"], 'match_id': row["match_id"], 'h_team_id': row["h_team_id"],'a_team_id': row["a_team_id"], 'date': row["date"], 'h_results': row["h_results"],'a_results': row["a_results"],'S501_1': row["S501_1"],'S501_2': row["S501_2"],'S501_3': row["S501_3"],'S501_4': row["S501_4"],'d301': row["d301"],'dC': row["dC"],'T501':row["T501"]})
                    counter+= 1
        os.remove("the_project/files/match_results.csv")
        os.rename("the_project/files/match_results_temp.csv", "the_project/files/match_results.csv")

