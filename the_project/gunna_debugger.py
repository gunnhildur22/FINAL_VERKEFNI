


from logic.logic_wrapper import LogicWrapper
from ui.view_leagues_ui import View_Leagues_UI
from ui.create_ui import Create_UI
from ui.main_ui import Menu_UI
logic_wrapper = LogicWrapper()

#ui = View_League_UI(logic_wrapper)
#ui.input_view_league()
leagues = logic_wrapper.get_all_leagues()
for league in leagues:
    the_league = league
matches = the_league.matches_list
print(matches)