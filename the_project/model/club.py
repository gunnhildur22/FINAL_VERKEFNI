class Club:
    def __init__(self,id, name, address, phone, team_list) -> None:
        '''
        Makes a model for club
        '''
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone
        self.team_list = team_list