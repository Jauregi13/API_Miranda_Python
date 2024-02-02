
from .models import Model
import json
import random
from ..utils.validations import (validate_numbers, 
                                validate_range_numbers, 
                                validate_value_in_list, 
                                validate_multiple_values_in_list,
                                validate_booleans)

class Room(Model):

    tableName = 'rooms'
    fields = {
            'room_id': '',
            'room_type': '',
            'room_number': '',
            'description': '',
            'price': 0,
            'offer': 0,
            'cancellation': '',
            'amenities': [],
            'available': False
    }

    def __init__(self,room):

        self.fields['room_id'] = room['room_id']
        self.fields['room_type'] = room['room_type']
        self.fields['room_number'] = room['room_number']
        self.fields['description'] = room['description']
        self.fields['price'] = room['price']
        self.fields['offer'] = room['offer']
        self.fields['cancellation'] = room['cancellation']
        self.fields['amenities'] = room['amenities']
        self.fields['available'] = room['available']

    
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
            "room_type": validate_value_in_list('room type',list=['Single Bed','Double Bed','Double Superior','Suite'], required=False),
            "room_number": validate_numbers('room number', required=False),
            "description": input('Enter the description of the room: '),
            "price": validate_numbers('price', required=False),
            "offer": validate_range_numbers('room offer',required=False, min=0,max=100),
            "cancellation": input('Enter the cancellation policy: '),
            "amenities": validate_multiple_values_in_list('amenity',required=False,list=cls.getAmenities(connection)),
            "available": validate_booleans('available', required=False)
        }

        room = Room(data)

        super(Room,room).update()
        
    @classmethod
    def create(cls, connection):
        print('-----CREATE ROOM------------')

        id = random.randint(1000,9999)

        data = {
            "room_id": id,
            "room_type": validate_value_in_list(value_type='room type', list=['Single Bed','Double Bed','Double Superior','Suite'], required=False),
            "room_number": validate_range_numbers('room number',min=100,max=999, required=False),
            "description": input('Enter the description of the room: '),
            "price": validate_numbers('price'),
            "offer": validate_range_numbers('room offer',min=0,max=100),
            "cancellation": input('Enter the cancellation policy: '),
            "amenities": validate_multiple_values_in_list('amenity',cls.getAmenities(connection)),
            "available": validate_booleans('available', required=True)
        }

        room = Room(data)

        super(Room,room).create()