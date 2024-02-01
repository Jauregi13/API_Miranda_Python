
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

    def update(self):
        print('-----UPDATE ROOM------------')
        print('To update the data, enter information into the inputs; otherwise, leave them blank')

        room_type = input('Enter the new type of room: ')
        if room_type:
            self.room_type = room_type
        
        room_number = input('Enter the new room number: ')
        if room_number:
            self.room_number = room_number
        
        description = input('Enter the new description of the room: ')
        if description:
            self.description = description
        
        while True:
            try:
                price = input('Enter the new price: ')
                if price:
                    priceInt = int(price)
                    self.price = priceInt
                break
            except ValueError:
                print('The price is not a valid number. Please enter a valid number')
        
        while True:
            try:
                offer = input('Enter the new room offer: ')

                if offer:
                    offerInt = int(offer)
                    if offerInt >= 0 and offerInt < 100:
                        self.offer = offerInt
                        break
                    else:
                        print('The percentage of the room offer must be between 0 and 100')
                else:
                    break 
                
            except ValueError:
                print('The price is not a valid number. Please enter a valid number')
        
        cancellation = input('Introduce the new cancellation policy: ')
        if cancellation:
            self.cancellation = cancellation
        
        amenitiesString = input('Enter new amenities separated by commas: ')
        amenities = []
        if amenitiesString:
            for amenity in amenitiesString.split(','):

                amenities.append(amenity)
            self.amenities = amenities

        while True:

            status = input('Change the room status, it can only be Available or Booked: ')
            if status:
                if status.capitalize() == 'Available' or status.capitalize() == 'Booked':
                    self.status = status.capitalize()
                    break
                else:
                    print('You have not entered available or booked for the status.')
        
        
        data = {
            "id": self.id,
            "room_type": self.room_type,
            "room_number": self.room_number,
            "description": self.description,
            "price": self.price,
            "offer": self.offer,
            "cancellation": self.cancellation,
            "amenities": self.amenities,
            "status": self.status
        }

        print(json.dumps(data,indent=4))

    @classmethod
    def create(cls, connection):
        print('-----CREATE ROOM------------')

        id = random.randint(1000,9999)

        cursor = connection.cursor(dictionary=True)

        cursor.execute('SELECT name FROM amenities')

        amenities = [amenity['name'] for amenity in cursor.fetchall()]

        data = {
            "room_id": id,
            "room_type": validate_value_in_list('room type',['Single Bed','Double Bed','Double Superior','Suite']),
            "room_number": validate_range_numbers('room number',min=100,max=999),
            "description": input('Enter the description of the room: '),
            "price": validate_numbers('price'),
            "offer": validate_range_numbers('room offer',min=0,max=100),
            "cancellation": input('Enter the cancellation policy: '),
            "amenities": validate_multiple_values_in_list('amenity',amenities),
            "available": validate_booleans('available')
        }

        room = Room(data)

        super(Room,room).create()