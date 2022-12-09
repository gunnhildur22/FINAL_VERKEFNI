from model.game import Game
import csv

class Game_data:
    def __init__(self) -> None:
        self.file_name = "./the_project/files/games.csv"

    def get_all_games(self):
        '''
        Reads all games from the given file
        '''
        ret_list = list()
        with open(self.file_name, "r", newline = "", encoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Game(row['id'], row['game_type'], row['score'], row['HP1'], row['HP2'], row['HP3'], row['HP4'], row['AP1'], row['AP2'], row['AP3'], row['AP4']))
        return ret_list

    def create_game(self, game):
        id = len(self.get_all_games()) + 1
        with open(self.file_name, "a", newline = "", encoding = "utf-8") as csvfile:
            fieldnames = ["id","game_type","score","HP1","HP2","HP3","HP4","AP1","AP2","AP3","AP4"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writerow({'id': id ,'game_type': game.game_type, 'score': game.score, 'HP1': game.HP1,'HP2': game.HP2,'HP3': game.HP3,'HP4': game.HP4,'AP1': game.AP1,'AP2': game.AP2,'AP3': game.AP3,'AP4': game.AP4})

