import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.nationality = dict['nationality']
        self.id = dict['id']
        self.games = dict['games']
        self.goals = dict['goals']
        self.assists = dict['assists']
    
    def __str__(self):
        return f"{self.name}, {self.team}"

class PlayerReader:
    def __init__(self, url):
        self.url = url
        response = requests.get(url).json()
