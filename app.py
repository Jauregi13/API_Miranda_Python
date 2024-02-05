import argparse
import json
from src.utils.connectionMySQL import connection
from src.models.Room import Room
from src.models.Booking import Booking
from src.models.User import User
from src.utils.validations import format_date, format_decimal

parser = argparse.ArgumentParser()
parser.add_argument('-action', type=str, required=True, choices=['read-bookings','read-rooms','read-users','read-room',
                    'read-booking','read-user','update-room','update-user','create-room','create-user','delete-room'])
args = parser.parse_args()

connect = connection()

def readRooms():
    
    rooms = Room.list(connect)

    print(json.dumps(rooms,indent=4,default=format_decimal))
    
def readBookings():

    bookings = Booking.list(connect)
    print(json.dumps(bookings,indent=4,default=format_date))

def readUsers():

    users = User.list(connect)
    '''for user in users:
        print(type(str(user['start_date'])))'''
    print(json.dumps(users,indent=4,default=format_date))

def roomById():

    roomId = input('Introduce id of room: ')
    room = Room.view(roomId,connect)

    if room:
        print(json.dumps(room,indent=4,default=format_decimal))
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
    roomExist = Room.view(roomId,connection=connect)

    if roomExist:
        Room.update(id=roomExist['room_id'],connection=connect)
    else:
        print('id of room not exist')

def updateUser():

    userId = input('Introduce id of user: ')
    userExist = User.view(userId,connection=connect)

    if userExist:
        User.update(id=userExist['room_id'])
    else:
        print('id of user not exist')


def createRoom():
    
    Room.create(connect)

def createUser():

    User.create()

def deleteRoom():
    
    roomId = input('Introduce id of room: ')
    roomExist = Room.view(roomId,connection=connect)

    if roomExist:
        Room.delete(id=roomExist['id'])
    else:
        print('id of room not exist')


actions = {'read-rooms' : readRooms,'read-bookings' : readBookings,'read-users' : readUsers, 'read-room': roomById,
            'read-booking': bookingById, 'read-user': userById, 'update-room' : updateRoom, 'update-user': updateUser,
            'create-room': createRoom,'create-user': createUser, 'delete-room': deleteRoom}

actions[args.action]()