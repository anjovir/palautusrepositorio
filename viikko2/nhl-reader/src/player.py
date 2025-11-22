class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
    
    def __str__(self):
        return self.name, self.team
