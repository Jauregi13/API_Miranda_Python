from abc import ABC, abstractmethod
import json

class Model(ABC):

    @classmethod
    def list(cls):
        
        with open(cls.path, encoding='utf-8') as file:
            print(file.read())
    
    @classmethod
    def view(cls,id):
        with open(cls.path, encoding='utf-8') as file:
            list = json.load(file)
            for elem in list:
                if id == elem['id']:
                    print(json.dumps(elem, indent=4))
                    break

    @abstractmethod
    def create():
        pass
    
    @abstractmethod
    def update():
        pass
    
    @classmethod
    def delete():
        pass
