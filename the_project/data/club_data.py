import csv

from model.club import Club


class Club_data:
    def __init__(self) -> None:
        self.file_name = "the_project/files/clubs.csv"

    def read_all_clubs(self):
        '''
        Reads all clubs from the given file
        '''
        ret_list = list()
        with open(self.file_name, "r", newline = "", encoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Club(row['id'], row['name'], row['address'], row['phone'], eval(row['team_list'])))
        return ret_list

    def create_club(self, club):
        id = len(self.read_all_clubs()) + 1
        with open(self.file_name, "a", newline = "", encoding = "utf-8") as csvfile:
            fieldnames = ["id", "name", "address", "phone", "team_list"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writerow({'id': id ,'name': club.name, 'address': club.address, 'phone': club.phone, 'team_list': club.team_list})            