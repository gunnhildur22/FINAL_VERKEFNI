import csv, os
from model.qp import QP


class Points_data:
    def __init__(self) -> None:
        self.file_name = "the_project/files/qp.csv"
    
    def get_all_points(self) -> list:
        '''
        Reads all QP from the given file
        '''
        ret_list = list()
        with open(self.file_name, "r", newline = "", encoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(QP(row['id'], row['league_id'], row['player_id'], row['qp'],row['inshot'], row['outshot']))
        return ret_list
        
    def create_id(self) -> int:
        '''loops though all records in database to create an ID one larger than the highest one
            Returns the new ID as an integer'''
        with open(self.file_name, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            counter = 1
            for _ in reader:
                counter +=1
            return counter
        
    def update_points(self, player_id, league_id, player_qp, player_insh, player_outsh, this_id) -> None:
        '''Updates the points of a selected player in a given league, returns None'''
        
        with open(self.file_name, "r+",newline = "", encoding = "utf-8") as csvfile_r:
            reader = csv.DictReader(csvfile_r)
            with open("the_project/files/qp_temp.csv", "a", newline = "", encoding = "utf-8") as csvfile_w:
                fieldnames = ["id", "league_id", "player_id" , "qp", "inshot", "outshot"]
                writer = csv.DictWriter(csvfile_w, fieldnames = fieldnames)
                counter = 0
                for row in reader:
                    if counter == 0:
                        writer.writerow({'id': "id" ,'league_id': "league_id", "player_id": "player_id", "qp": "qp", "inshot": "inshot", "outshot": "outshot"})
                    if row["id"] == this_id:
                        writer.writerow({'id': this_id ,'league_id': league_id, "player_id": player_id , "qp": int(row["qp"]) + int(player_qp), "inshot": player_insh, "outshot": player_outsh})
                    else:
                        writer.writerow({'id': row["id"] ,'league_id': row["league_id"], "player_id": row["player_id"], "qp": row["qp"], "inshot": row["inshot"], "outshot": row["outshot"]})
                    counter += 1
        os.remove("the_project/files/qp.csv")
        os.rename("the_project/files/qp_temp.csv", "the_project/files/qp.csv")
        return
        
    def new_points(self, league_id,player_id, player_qp, player_insh, player_outsh) -> None:
        '''Writes a new record of a player and their points to the database, returns None'''
        id = self.create_id()
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "league_id", "player_id", "qp", "inshot", "outshot"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writerow({'id': id, 'league_id': league_id, 'player_id': player_id, 'qp': player_qp, 'inshot': player_insh, 'outshot': player_outsh})
            return
            
    def write_points(self, player_id, league_id, player_qp, player_insh, player_outsh) -> None:
        '''Calls read_stats. If a record exists calls update_points, else calls new_points'''
        with open(self.file_name, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["league_id"] == league_id and row["player_id"] == player_id:
                    this_id = row["id"]
                    csvfile.close()
                    self.update_points(player_id, league_id, player_qp, player_insh, player_outsh, this_id)
                    return
            else:
                self.new_points(player_id, league_id, player_qp, player_insh, player_outsh)
                return
                
    def read_stats(self, league_id, player_id):
        '''Loops through all records in database. Returns record if it exists, else returns None'''
        with open(self.file_name, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["league_id"] == league_id and row["player_id"] == player_id:
                    return row
            else:
                return None

    
