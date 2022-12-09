class Team:
    def __init__(self, id, name, player_ids, captin_id) -> None:
        '''
        Makes a model for team
        '''
        self.id = id
        self.name = name
        self.player_ids = player_ids
        self.captin_id = captin_id