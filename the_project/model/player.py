class Player:
    def __init__(self, id, name, social_security, phonenumber, address, email)-> None:
        '''
        Makes a model for player
        '''
        self.id = id
        self.name = name
        self.social_security = social_security
        self.phonenumber = phonenumber
        self.address = address
        self.email = email