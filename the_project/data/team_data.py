import csv

from model.team import Team


class Team_data:
    def __init__(self) -> None:
        self.file_name = "FINAL_VERKEFNI/the_project/files/teams.csv"

    def read_all_teams(self):
        '''
        Reads all teams from the given file
        '''
        ret_list = list()
        with open(self.file_name, "r", newline = "", encoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Team(row['id'], row['name'], eval(row['player_ids']), row['captin_id']))
        return ret_list

    def create_team(self, team):
        id = len(self.read_all_teams()) + 1
        with open(self.file_name, "a", newline = "", encoding = "utf-8") as csvfile:
            fieldnames = ["id", "name", "player_ids", "captin_id"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writerow({'id': id ,'name': team.name, 'player_ids': team.player_ids, 'captin_id': team.captin_id})