from datetime import date
from typing import Union
from .Model import Model

class User(Model):

    tableName = 'users'

    def __init__(self,user):
               
        self.user_id = user['user_id']
        self.name = user['name']
        self.user_image = user['user_image']
        self.email = user['email']
        self.start_date = user['start_date']
        self.description = user['description']
        self.contact = user['contact']
        self.active = user['active']
    
    @classmethod
    def create(cls):

        print('------CREATE USER-----------------')

        id = random.randint(10000,99999)

        data = {
            "user_id" : id
        }

