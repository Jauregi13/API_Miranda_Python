from decimal import Decimal
import re
from datetime import datetime, date
from urllib.parse import urlparse

def format_date(obj):
    if isinstance(obj, date):
        return str(obj)
    raise TypeError("Object of type {} is not JSON serializable".format(type(obj)))

def format_decimal(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError("Object of type {} is not JSON serializable".format(type(obj)))

def validate_value_required(data):

    if not(data):
        raise ValueError(f'You have to write a value')


def validate_number(value: int, min: int, max: int):

    if (min and value < min) or (max and value > max):
        raise ValueError(f'This number is not within the established range ({min},{max})')

    else:
        return value


def validate_string(value: str, length: int):

    if len(value) > length:
        raise ValueError('This string is longer than the required length')
    else:
        return value

def validate_boolean(value: str):

    if value == 'y' or value == 'yes':
        return True
    elif value == 'n' or value == 'no':
        return False
    else:
        raise ValueError('You have to write yes, y, no, or n')

def validate_value_in_list(value : str, list : list):


    if value in list:
        return value
    else:
        raise ValueError('%s not exist in this list' % (value))


def validate_regex(value: str, regex: str):
    
    if not(re.fullmatch(regex,value)):
        raise ValueError(f'{value} does not match the format')

def validate_date(value):

   datetime.fromisoformat(value)

def validate_url(value):

    url = urlparse(value)

    if not(all([url.scheme,url.netloc])):
        raise ValueError(f'{value} is not a valid url')

    