from decimal import Decimal

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError("Object of type {} is not JSON serializable".format(type(obj)))

def validate_numbers(value_type, required):
    while True:
        try:
            data = input(f'Enter the %s: ' %(value_type))
            if required and not(data):
                raise ValueError(f'You have to write a %s' % (value_type))
            elif not(data):
                return data

            return int(data)
        except ValueError as e:
            print(e)

def validate_range_numbers(value_type,required, min, max):
    while True:
            try:
                data = input(f'Enter the %s if it exists; otherwise, write 0: ' % (value_type))
                if required and not(data):
                    raise ValueError(f'You have to write a %s' % (value_type))
                elif not(data):
                    return data
                elif int(data) >= min and int(data) < max:
                    return int(data)
                else:
                    print(f'The %s must be between 0 and 100' % (value_type))
            except ValueError:
                print(f'The %s is not a valid number. Please enter a valid number' % (value_type))

def validate_strings(value_type, required, length):
    pass

def validate_booleans(value_type, required):

    while True:

        try:
            data = input('Is %s?(y/n or yes/no)'%(value_type))
            if required and not(data):
                raise ValueError('You have to decide between yes or no')
            elif not(data):
                return data
            elif data == 'y' or data == 'yes':
                return True
            elif data == 'n' or data == 'no':
                return False
            else:
                raise ValueError('You have to write yes, y, no, or n')
                
        except ValueError as e:
            print(e)


def validate_value_in_list(value_type, list, required):

    print('This is the list of %s you have to follow' % (value_type))
    for item in list:
        print(item)

    while True:
        try:
             
            data = input('Enter the %s that exist in this list: ' % (value_type))
            if required and not(data):
                raise ValueError('You have to add one from the list')
            elif data in list or not(data):
                return data
            else:
                raise ValueError('%s not exist in this list' % (data))
        except ValueError as e:
            print(e)

def validate_multiple_values_in_list(value_type, required, list):

    print('This is the list of %s you have to follow' % (value_type))
    for item in list:
        print(item)
    items = []
    while True:

        try:
            item = input('Enter the %s that exist in this list, to exit this input, press Enter: ' % (value_type))
            if item in list:
                items.append(item)
            elif required and item and len(items) == 0:
                raise ValueError('You have to add one from the list')
            elif item == '':
                return items
            else:
                raise ValueError('%s not exist in this list' % (item))

        except ValueError as e:
            print(e)
            
            