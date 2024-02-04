
from .Model import Model
import json
import random
from typing import Union
from ..utils.inputs import input_number,input_string,input_list,input_boolean

class Room(Model):

    tableName = 'rooms'

    def __init__(self,room):

        self.room_id = room['room_id']
        self.room_type = room['room_type']
        self.room_number = room['room_number']
        self.description = room['description']
        self.price = room['price']
        self.offer = room['offer']
        self.cancellation = room['cancellation']
        self.amenities = room['amenities']
        self.available = room['available']

    
    def getAmenities(connection):

        cursor = connection.cursor(dictionary=True)

        cursor.execute('SELECT name FROM amenities')

        amenities = [amenity['name'] for amenity in cursor.fetchall()]

        return amenities

    @classmethod
    def update(cls,id,connection):
        print('-----UPDATE ROOM------------')
        print('To update the data, enter information into the inputs; otherwise, leave them blank')

        data = {
            "room_id": id,
            "room_type": input_list('room type',list=['Single Bed','Double Bed','Double Superior','Suite']),
            "room_number": input_number('room number', min=10,max=20),
            "description": input_string('description'),
            "price": input_number('price'),
            "offer": input_number('room offer', min=0,max=100),
            "cancellation": input('Enter the cancellation policy: '),
            "amenities": input_list('amenity',list=cls.getAmenities(connection),multiple=True),
            "available": input_boolean('available')
        }

        room = Room(data)

        super(Room,room).update()
        
    @classmethod
    def create(cls, connection):
        print('-----CREATE ROOM------------')

        id = random.randint(10000,99999)

        data = {
            "room_id": id,
            "room_type": validate_value_in_list(value_type='room type', list=['Single Bed','Double Bed','Double Superior','Suite'], required=False),
            "room_number": input_number('room number',min=100,max=999, required=True),
            "description": input('Enter the description of the room: '),
            "price": input_number('price',required=True,min=50,max=500),
            "offer": input_number('room offer',min=0,max=100),
            "cancellation": input('Enter the cancellation policy: '),
            "amenities": validate_multiple_values_in_list('amenity',cls.getAmenities(connection)),
            "available": validate_booleans('available', required=True)
        }

        room = Room(data)

        super(Room,room).create()