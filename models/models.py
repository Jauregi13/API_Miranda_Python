from abc import ABC, abstractmethod
import json

class Model(ABC):

    @classmethod
    def list(cls):
        
        with open(cls.path, encoding='utf-8') as file:
            print(file.read())
    
    @classmethod
    def view(cls,id):
        object_exist = {}
        with open(cls.path, encoding='utf-8') as file:
            list = json.load(file)
            for elem in list:
                if id == elem['id']:
                    return json.dumps(elem, indent=4)
        return f'Id of {cls.__name__} not exist'

    @abstractmethod
    def create(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    @classmethod
    def delete(cls):
        pass
