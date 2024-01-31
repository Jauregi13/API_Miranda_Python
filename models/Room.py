
from models.models import Model
import json

class Room(Model):

    path = 'data/roomsData.json'
    tableName = 'rooms'
    id = ''
    room_type = ''
    room_number = ''
    description = ''
    price = 0
    offer = 0
    cancellation = ''
    amenities = []
    status = ''

    def __init__(self,id=None, room=None):

        if room:
            self.id = room['id']
            self.room_type = room['room_type']
            self.room_number = room['room_number']
            self.description = room['description']
            self.price = room['price']
            self.offer = room['offer']
            self.cancellation = room['cancellation']
            self.amenities = room['amenities']
            self.status = room['status']
        elif id:
            self.id = id

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


    def create(self):
        print('-----CREATE ROOM------------')
        self.room_type = input('Enter the type of room: ')
        self.room_number = input('Enter the room number: ')
        self.description = input('Enter the description of the room: ')

        while True:
            try:
                price = int(input('Enter the price: '))
                self.price = price
                break
            except ValueError:
                print('The price is not a valid number. Please enter a valid number')
        
        while True:
            try:
                offer = int(input('Enter the room offer if it exists; otherwise, write 0: '))

                if offer >= 0 and offer < 100:
                    self.offer = offer
                    break
                else:
                    print('The percentage of the room offer must be between 0 and 100')
            except ValueError:
                print('The price is not a valid number. Please enter a valid number')

        self.cancellation = input('Introduce the cancellation policy: ')

        amenitiesString = input('Enter the amenities separated by commas: ')
        
        for amenity in amenitiesString.split(','):

            self.amenities.append(amenity)

        while True:

            status = input('Enter the room status, it can only be Available or Booked: ')

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

