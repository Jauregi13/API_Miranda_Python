from decimal import Decimal

def decimal_default(obj):
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

    if data == 'y' or data == 'yes':
        return True
    elif data == 'n' or data == 'no':
        return False
    else:
        raise ValueError('You have to write yes, y, no, or n')

def validate_value_in_list(value, list):


    if value in list:
        return value
    else:
        raise ValueError('%s not exist in this list' % (value))
            
            