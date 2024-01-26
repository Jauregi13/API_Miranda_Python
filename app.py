import argparse
import json
import random
from models.Room import Room
from models.Booking import Booking
from models.User import User

parser = argparse.ArgumentParser()
parser.add_argument('-action', type=str, required=True, choices=['read-bookings','read-rooms','read-users','read-room',
                    'read-booking','read-user','update-room','create-room'])
args = parser.parse_args()

def roomById():
    roomId = input('Introduce id of room: ')
    print(Room.view(roomId))

def bookingById():
    bookingId = input('Introduce id of booking: ')
    Booking.view(bookingId)

def userById():
    userId = input('Introduce id of user: ')
    User.view(userId)

def updateRoom():
    roomId = input('Introduce id of room: ')
    roomExist = Room.view(roomId)

    if roomExist:
        room = Room(json.loads(roomExist))
        room.update()
    else:
        print('hola')

def createRoom():
    id = random.randint(1000,9999)
    room = Room(id)
    room.create()

actions = {'read-rooms' : Room.list,'read-bookings' : Booking.list,'read-users' : User.list, 'read-room': roomById,
            'read-booking': bookingById, 'read-user': userById, 'update-room' : updateRoom, 'create-room': createRoom}

actions[args.action]()