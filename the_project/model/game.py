class Game:
    def __init__(self,id,game_type,score,HP1,HP2,HP3,HP4,AP1,AP2,AP3,AP4) -> None:
        '''
        Makes a model for game
        '''
        self.id = id
        self.game_type = game_type
        self.HP1 = HP1
        self.HP2 = HP2
        self.HP3 = HP3
        self.HP4 = HP4
        self.AP1 = AP1
        self.AP2 = AP2
        self.AP3 = AP3
        self.AP4 = AP4
        self.score = score