from .validations import (validate_number, validate_string, validate_value_required,
                        validate_boolean,validate_value_in_list,validate_regex,validate_date, validate_url)


def input_number(value_type:str,required: bool = False,min:int = None, max:int = None):

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


def input_string(value_type: str, required:bool = False, length: int = 255):

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


def input_boolean(value_type: str, required: bool = False):

    while True:

        try:
            data = input('Is %s?(y/n or yes/no)'%(value_type))

            if required:
                validate_value_required(data)

            if data:
                result = validate_boolean(data)
            
            return result
        
        except ValueError as e:
            print(e)

def input_list(value_type : str,list: list, multiple: bool = False,required: bool = False):

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

def input_phone(value_type: str, required:bool = False):

    regex = r"[6-9][0-9]{2} [0-9]{3} [0-9]{3}"

    while True:

        try:

            data = input(f'Enter the {value_type}:([6-9]99 999 999)')

            if required:
                validate_value_required(data)
            
            if data:
                validate_regex(data,regex=regex)
            
            return data
        
        except ValueError as e:
            print(e)

def input_email(required: bool = False):

    regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    while True:

        try:
            data = input('Enter the email: ')

            if required:
                validate_value_required(data)
            
            if data:
                validate_regex(data,regex_email)

            return data
            
        except ValueError as e:
            print(e)

def input_date(value_type,required:bool = False):
    
    while True:
        try:
            data = input(f'Enter the {value_type}:(YYYY-MM-DD)')
            
            if required:
                validate_value_required(data)
            
            if data:
                validate_date(data)
            
            return data


        except ValueError as e:
            print(e)

def input_url(value_type, required:bool = False):

    while True:
        try:
            data = input(f'Enter the {value_type} url: ')

            if required:
                validate_value_required(data)
            
            if data:
                validate_url(data)
            
            return data
        
        except ValueError as e:
            print(e)