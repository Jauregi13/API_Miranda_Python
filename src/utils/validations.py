from decimal import Decimal

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError("Object of type {} is not JSON serializable".format(type(obj)))

def validate_numbers(value_type):
    while True:
        try:
            data = int(input(f'Enter the %s: ' %(value_type)))
            return data
            break
        except ValueError:
            print(f'The %s is not a valid number. Please enter a valid number' %(value_type))

def validate_range_numbers(value_type, min,max):
    while True:
            try:
                data = int(input(f'Enter the %s if it exists; otherwise, write 0: ' % (value_type)))

                if data >= min and data < max:
                    return data
                    break
                else:
                    print(f'The %s must be between 0 and 100' % (value_type))
            except ValueError:
                print(f'The %s is not a valid number. Please enter a valid number' % (value_type))

def validate_strings(input_text):
    pass


def validate_value_in_list(input_text,list,multiple_values):
    pass