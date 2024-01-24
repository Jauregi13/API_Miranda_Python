from abc import ABC

class Model(ABC):

    @classmethod
    def list(cls):
        
        with open(cls.path, encoding='utf-8') as file:
            print(file.read())
    
    def view(cls,id):
        pass

    def create():
        pass

    def update():
        pass

    def delete():
        pass
