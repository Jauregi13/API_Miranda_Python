
from .validations import (validate_number, validate_string, validate_value_required,
                        validate_boolean,validate_value_in_list)


def input_number(value_type:str,required: bool,min:int = None, max:int = None):

    while True:

        try:

            data = input(f'Enter the %s: ' %(value_type))
            
            if required:
                validate_value_required(data)

            if data:
                return validate_number(int(data),min,max)
            
            return data
        
        except ValueError as e:
            print(e)


def input_string(value_type: str, required:bool, length: int = 255):

    while True:

        try:
            data = input(f'Enter the %s: ' %(value_type))

            if required:
                validate_value_required(data)
                
            if data:
                validate_string(data,length)

            return data

        except ValueError as e:
            print(e)


def input_boolean(value_type: str):

    while True:

        try:
            data = input('Is %s?(y/n or yes/no)'%(value_type))

            if required:
                validate_value_required(data)

            if data:
                validate_boolean(data)
            
            return data
        
        except ValueError as e:
            print(e)

def input_list(value_type : str,required: bool,list: list, multiple: bool):

    print('This is the list of %s you have to follow' % (value_type))
    for item in list:
        print(item)
    
    items = []

    while True:

        try:
            data = input('Enter the %s that exist in this list: ' % (value_type))

            if required and len(items) == 0:
                validate_value_required(data)

            if data:
                result = validate_value_in_list(data,list)

                if multiple:
                    items.append(result)
                else:
                    return result

            if not(multiple) or (multiple and not(data)):

                return data

        except ValueError as e:
            print(e)
    pass