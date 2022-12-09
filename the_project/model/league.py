class League:
    def __init__(self, id, name, org_name , phone, email, start_date, teams_list, matches_list):
        '''
        Makes a model for league
        '''
        self.id = id
        self.name = name
        self.org_name = org_name
        self.phone = phone
        self.email = email
        self.start_date = start_date
        self.teams_list = teams_list
        self.matches_list = matches_list
