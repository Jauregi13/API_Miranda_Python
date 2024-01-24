import argparse
from models.Room import Room
from models.Booking import Booking

parser = argparse.ArgumentParser()
parser.add_argument('-action', type=str, required=True, choices=['read-bookings','read-rooms','read-users'])
args = parser.parse_args()

actions = {'read-rooms' : Room.list(),'read-bookings' : Booking.list()}

actions[args.action]