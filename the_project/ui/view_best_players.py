


import os
from sys import platform
import time


class View_Best_Players:
    def __init__(self,logic_connection, league) -> None:
        self.logic_wrapper = logic_connection
        self.league = league
    
    def menu_output(self):
        self.clear_screen(platform)
        print("Best Players!")
        dict_qp = {}
        dict_inshot = {}
        dict_outshot = {}
        dict_points = {}
        all_points = self.logic_wrapper.get_all_points()
        players = self.logic_wrapper.get_all_players()
        for point in all_points:
            if point.league_id == self.league.id:
                dict_qp[point.player_id] = int(point.player_qp)
                dict_inshot[point.player_id] = int(point.player_insh)
                dict_outshot[point.player_id] = int(point.player_outsh)
    
        for key,val in dict_qp.items():
            for player in players:
                if player.id == key:
                    dict_points[player.name] = [dict_qp[key],dict_inshot[key],dict_outshot[key]]
        
        #sorted_dict_points = {k: v for k, v in sorted(dict_points.items(), key=lambda item: item[1][2], reverse=True)}
        #sorted_dict_points = {k: v for k, v in sorted(dict_points.items(), key=lambda item: item[1][1], reverse=True)}
        sorted_dict_points = {k: v for k, v in sorted(dict_points.items(), key=lambda item: item[1][2], reverse=True)}
        sorted_dict_points = {k: v for k, v in sorted(dict_points.items(), key=lambda item: item[1][1], reverse=True)}
        sorted_dict_points = {k: v for k, v in sorted(dict_points.items(), key=lambda item: item[1][0], reverse=True)}

        print("{:<20}{:<20}{:<20}{:<20}".format("Name","QP","Inshot","Outshot"))
        for key,val in sorted_dict_points.items():
            print("{:<20}{:<20}{:<20}{:<20}".format(str(key),str(val[0]),str(val[1]),str(val[2])))
        

        print("q for quit")
        command = input("press enter to return ")
        if command == "q":
            print("bye")
            self.clear_screen(platform)
            quit()
        else:
            self.clear_screen(platform)
            return
        
    def clear_screen(self,platform):
        if platform == "linux" or platform == "linux2":
            time.sleep(0.5)
            os.system('clear')
        elif platform == "darwin":
            time.sleep(0.5)
            os.system('clear')
        elif platform == "win32":
            time.sleep(0.5)
            os.system('cls')
                    

