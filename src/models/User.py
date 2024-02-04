from datetime import date
import random
from typing import Union
from .Model import Model
from ..utils.inputs import input_string,input_boolean, input_phone,input_email, input_date, input_url


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
            "user_id" : id,
            "name": input_string('name',length=30),
            "user_image": input_url('image'),
            "email": input_email(),
            "start_date": input_date('start_date'), 
            "description": input_string('description'),
            "contact": input_phone('contact'),
            "active": input_boolean('active')
        }

