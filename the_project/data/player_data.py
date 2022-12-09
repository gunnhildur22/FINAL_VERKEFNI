import csv

from model.player import Player


class Player_data:
    def __init__(self) -> None:
        self.file_name = "./the_project/files/players.csv"

    def read_all_players(self):
        '''
        Reads all players from the given file
        '''
        ret_list = list()
        with open(self.file_name, "r", newline = "", encoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Player(row['id'], row['name'], row['social_security'], row['phonenumber'], row['address'], row['email']))
        return ret_list

    def create_player(self, player):
        id = len(self.read_all_players()) + 1
        with open(self.file_name, "a", newline = "", encoding = "utf-8") as csvfile:
            fieldnames = ["id", "name", "social_security", "phonenumber", "address", "email"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writerow({'id': id ,'name': player.name, 'social_security': player.social_security, 'phonenumber': player.phonenumber, 'address': player.address, 'email': player.email})