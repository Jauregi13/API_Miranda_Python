
from models.models import Model

class Room(Model):

    path = 'data/roomsData.json'

    def __init__(self):
        print(self)

