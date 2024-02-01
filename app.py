import argparse
import json
from src.utils.connectionMySQL import connection
from src.models.Room import Room
from src.models.Booking import Booking
from src.models.User import User
from src.utils.validations import decimal_default

parser = argparse.ArgumentParser()
parser.add_argument('-action', type=str, required=True, choices=['read-bookings','read-rooms','read-users','read-room',
                    'read-booking','read-user','update-room','create-room'])
args = parser.parse_args()

connect = connection()

def readRooms():
    
    rooms = Room.list(connect)

    print(json.dumps(rooms,indent=4,default=decimal_default))
    
def readBookings():
    print(Booking.list())

def readUsers():
    print(User.list())

def roomById():
    connect = connection()
    roomId = input('Introduce id of room: ')
    room = Room.view(roomId,connect)

    if room:
        print(json.dumps(room,indent=4,default=decimal_default))
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
    
    Room.create(connect)

actions = {'read-rooms' : readRooms,'read-bookings' : readBookings,'read-users' : readUsers, 'read-room': roomById,
            'read-booking': bookingById, 'read-user': userById, 'update-room' : updateRoom, 'create-room': createRoom}

actions[args.action]()