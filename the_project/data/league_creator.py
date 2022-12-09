import csv
import string
import os
from model.league import League
import datetime


class League_data:
    def __init__(self):
        self.file_name = "FINAL_VERKEFNI/the_project/files/league.csv"
        
    def __len__(self):
        length = 1
        with open(self.file_name) as f:
            for _ in f:
                length += 1
        
        return length
    
    def get_all_leagues(self):
        '''
        Reads all leagues from the given file
        Returns a dictionary with the fieldnames as keys and rows 
        '''
        ret_list = []
        with open(self.file_name, newline = "", encoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(League(row["id"], row["name"], row["org_name"], row["phone"], row["email"], row["start_date"], eval(row["teams_list"]), eval(row["matches_list"])))
        return ret_list

    def create_league(self, league):
        id = len(self.get_all_leagues()) + 1
        with open(self.file_name, "a", newline = "", encoding = "utf-8") as csvfile:
            fieldnames = ["id", "name", "org_name" , "phone", "email", "start_date", "teams_list", "matches_list"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writerow({'id': id ,'name': league.name, "org_name": league.org_name , "phone": league.phone, "email": league.email, "start_date": league.start_date, "teams_list": league.teams_list, "matches_list": league.matches_list})
        
    
    def edit_dates_of_matches(self, league):
        with open(self.file_name, "r+",newline = "", encoding = "utf-8") as csvfile_r:
            reader = csv.DictReader(csvfile_r)
            with open("the_project/files/leagues_temp.csv", "a", newline = "", encoding = "utf-8") as csvfile_w:
                fieldnames = ["id", "name", "org_name" , "phone", "email", "start_date", "teams_list", "matches_list"]
                writer = csv.DictWriter(csvfile_w, fieldnames = fieldnames)
                counter = 0
                for row in reader:
                    if counter == 0:
                        writer.writerow({'id': "id" ,'name': "name", "org_name": "org_name", "phone": "phone", "email": "email", "start_date": "start_date", "teams_list": "teams_list", "matches_list": "matches_list"})
                    if row["id"] == league.id:
                        writer.writerow({'id': league.id ,'name': league.name, "org_name": league.org_name , "phone": league.phone, "email": league.email, "start_date": league.start_date, "teams_list": league.teams_list, "matches_list": league.matches_list})
                    else:
                        writer.writerow({'id': row["id"] ,'name': row["name"], "org_name": row["org_name"], "phone": row["phone"], "email": row["email"], "start_date": row["start_date"], "teams_list": row["teams_list"], "matches_list": row["matches_list"]})
                    counter += 1
        os.remove("the_project/files/league.csv")
        os.rename("the_project/files/leagues_temp.csv", "the_project/files/league.csv")
            