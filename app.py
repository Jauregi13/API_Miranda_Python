import argparse
from models.Room import Room
from models.Booking import Booking
from models.User import User

parser = argparse.ArgumentParser()
parser.add_argument('-action', type=str, required=True, choices=['read-bookings','read-rooms','read-users','read-room',
                    'read-booking','read-user'])
args = parser.parse_args()

def roomById():
    roomId = input('Introduce id of room: ')
    Room.view(roomId)

def bookingById():
    bookingId = input('Introduce id of booking: ')
    Booking.view(bookingId)

def userById():
    userId = input('Introduce id of user: ')
    User.view(userId)

actions = {'read-rooms' : Room.list,'read-bookings' : Booking.list,'read-users' : User.list, 'read-room': roomById,
            'read-booking': bookingById, 'read-user': userById}

actions[args.action]()