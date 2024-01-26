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

def readRooms():
    print(Room.list())

def readBookings():
    print(Booking.list())

def readUsers():
    print(User.list())

def roomById():
    roomId = input('Introduce id of room: ')
    room = Room.view(roomId)
    if room:
        print(room)
    else:
        print('id of room not exist')

def bookingById():
    bookingId = input('Introduce id of booking: ')
    booking = Booking.view(bookingId)
    if booking:
        print(booking)
    else:
        print('id of booking not exist')

def userById():
    userId = input('Introduce id of user: ')
    user = User.view(userId)
    if user:
        print(user)
    else:
        print('Id of user not exist')
        
def updateRoom():
    roomId = input('Introduce id of room: ')
    roomExist = Room.view(roomId)

    if roomExist:
        room = Room(json.loads(roomExist))
        room.update()

def createRoom():
    id = random.randint(1000,9999)
    room = Room(id)
    room.create()

actions = {'read-rooms' : readRooms,'read-bookings' : readBookings,'read-users' : readUsers, 'read-room': roomById,
            'read-booking': bookingById, 'read-user': userById, 'update-room' : updateRoom, 'create-room': createRoom}

actions[args.action]()